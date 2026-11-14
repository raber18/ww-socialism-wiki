#!/usr/bin/env python3
"""
verify_slides.py — 教學型 HTML 簡報自動化硬性驗收腳本

僅使用 Python 標準函式庫（re、html.parser、pathlib、sys、argparse），
檢查目標簡報檔（預設為根目錄 index.html）是否同時符合以下 4 項條件：
  1. 投影片總頁數（<section class="slide"> 數量）介於 10～14 頁之間。
  2. 每一頁投影片皆包含明確資料來源標註（如「來源：」或「[0...」來源檔名標記）。
  3. 單頁投影片扣除 HTML 標籤後的純文字字數不超過 380 字。
  4. HTML 結構完整（包含 <!DOCTYPE html> 與 </html>），且不包含 <img 標籤。
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

MIN_SLIDES = 10
MAX_SLIDES = 14
MAX_CHARS_PER_SLIDE = 380

# 允許之明確資料來源標註樣式：
# 1) 「來源：...」或「來源:...」（後方須有實質內容）
# 2) 「[0...」開頭之專案原始來源引用標記（例如 [01_russian_civil_war.md, 導言]）
SOURCE_LABEL_RE = re.compile(r"來源\s*[：:]\s*\S+")
SOURCE_FILE_RE = re.compile(r"\[0\d+[^\]]*\]")

DOCTYPE_RE = re.compile(r"<!doctype\s+html\b[^>]*>", re.IGNORECASE)
HTML_OPEN_RE = re.compile(r"<html\b[^>]*>", re.IGNORECASE)
HTML_CLOSE_RE = re.compile(r"</html\s*>", re.IGNORECASE)
IMG_TAG_RE = re.compile(r"<img\b", re.IGNORECASE)


class SlideDeckParser(HTMLParser):
    """以標準函式庫 HTMLParser 解析 <section class="slide"> 與頁面純文字內容。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides: list[dict[str, object]] = []
        self.img_count_parsed: int = 0
        self.unclosed_slide_error: bool = False

        self._in_slide: bool = False
        self._section_depth: int = 0
        self._ignored_tag_stack: list[str] = []
        self._heading_capture_tag: str | None = None
        self._current_heading_parts: list[str] = []
        self._first_heading: str = ""
        self._current_text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_lower = tag.lower()
        attr_map = {k.lower(): (v or "") for k, v in attrs}

        if tag_lower == "img":
            self.img_count_parsed += 1

        if tag_lower in ("script", "style"):
            self._ignored_tag_stack.append(tag_lower)
            return

        if tag_lower == "section":
            classes = attr_map.get("class", "").split()
            if "slide" in classes and not self._in_slide:
                self._in_slide = True
                self._section_depth = 1
                self._heading_capture_tag = None
                self._current_heading_parts = []
                self._first_heading = ""
                self._current_text_parts = []
                return
            if self._in_slide:
                self._section_depth += 1

        if self._in_slide and not self._ignored_tag_stack:
            if tag_lower in ("h1", "h2", "h3") and not self._first_heading:
                self._heading_capture_tag = tag_lower
                self._current_heading_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag_lower = tag.lower()

        if tag_lower in ("script", "style"):
            if self._ignored_tag_stack and self._ignored_tag_stack[-1] == tag_lower:
                self._ignored_tag_stack.pop()
            elif tag_lower in self._ignored_tag_stack:
                self._ignored_tag_stack.remove(tag_lower)
            return

        if self._in_slide and self._heading_capture_tag == tag_lower:
            heading = re.sub(r"\s+", " ", "".join(self._current_heading_parts)).strip()
            if heading and not self._first_heading:
                self._first_heading = heading
            self._heading_capture_tag = None
            self._current_heading_parts = []

        if self._in_slide and tag_lower == "section":
            self._section_depth -= 1
            if self._section_depth <= 0:
                raw_text = "".join(self._current_text_parts)
                normalized_text = re.sub(r"\s+", " ", raw_text).strip()
                # 純文字字數（扣除 HTML 標籤與排版縮排空白後的實際可視字元數）
                char_count = len(re.sub(r"\s+", "", raw_text))
                self.slides.append(
                    {
                        "heading": self._first_heading,
                        "plain_text": normalized_text,
                        "char_count": char_count,
                    }
                )
                self._in_slide = False
                self._section_depth = 0
                self._heading_capture_tag = None
                self._current_heading_parts = []
                self._first_heading = ""
                self._current_text_parts = []

    def handle_data(self, data: str) -> None:
        if not self._in_slide or self._ignored_tag_stack:
            return
        self._current_text_parts.append(data)
        if self._heading_capture_tag:
            self._current_heading_parts.append(data)

    def handle_comment(self, data: str) -> None:
        # 註解不計入投影片純文字
        return

    def finalize(self) -> None:
        if self._in_slide:
            self.unclosed_slide_error = True


def extract_source_matches(plain_text: str) -> list[str]:
    """萃取投影片內的資料來源標註摘要，便於報表印出。"""
    matches: list[str] = []
    file_matches = SOURCE_FILE_RE.findall(plain_text)
    if file_matches:
        matches.extend(file_matches)
    else:
        label_m = SOURCE_LABEL_RE.search(plain_text)
        if label_m:
            snippet = plain_text[label_m.start() : label_m.start() + 48].strip()
            matches.append(snippet)
    return matches


def resolve_target_path(cli_path: str | None) -> Path:
    if cli_path:
        return Path(cli_path)
    cwd_target = Path("index.html")
    if cwd_target.exists():
        return cwd_target
    repo_root = Path(__file__).resolve().parent.parent
    return repo_root / "index.html"


def verify_html_file(target_path: Path) -> tuple[bool, list[str]]:
    """執行 4 項硬性檢查並印出逐頁明細；回傳 (是否全數通過, 錯誤訊息清單)。"""
    if not target_path.exists():
        msg = f"找不到目標簡報檔：{target_path}"
        print(f"[ERROR] {msg}")
        return False, [msg]

    raw_html = target_path.read_text(encoding="utf-8")

    # 條件 4：HTML 結構完整性與禁止 <img 標籤檢查
    has_doctype = bool(DOCTYPE_RE.search(raw_html))
    has_html_open = bool(HTML_OPEN_RE.search(raw_html))
    has_html_close = bool(HTML_CLOSE_RE.search(raw_html))
    raw_img_match = IMG_TAG_RE.search(raw_html)

    parser = SlideDeckParser()
    parser.feed(raw_html)
    parser.close()
    parser.finalize()

    has_img = bool(raw_img_match) or (parser.img_count_parsed > 0)

    slides = parser.slides
    total_slides = len(slides)
    count_ok = MIN_SLIDES <= total_slides <= MAX_SLIDES

    errors: list[str] = []
    if not has_doctype:
        errors.append("缺少 <!DOCTYPE html> 宣告。")
    if not has_html_open:
        errors.append("缺少 <html> 起始標籤。")
    if not has_html_close:
        errors.append("缺少 </html> 結尾標籤。")
    if parser.unclosed_slide_error:
        errors.append("偵測到未正確閉合的 <section class=\"slide\"> 標籤。")
    if has_img:
        errors.append(
            f"偵測到禁止使用的 <img> 標籤（HTMLParser 計數={parser.img_count_parsed}，"
            f"原始掃描={'發現 <img' if raw_img_match else '無'}）。"
        )
    if not count_ok:
        errors.append(
            f"投影片總頁數為 {total_slides} 頁，未落在允許範圍 {MIN_SLIDES}～{MAX_SLIDES} 頁之間。"
        )

    print("=== 教學簡報自動化驗收報告 ===")
    print(f"檢查目標：{target_path}")
    print(
        f"[條件 4] HTML 結構檢查："
        f"<!DOCTYPE html>={'PASS' if has_doctype else 'FAIL'}, "
        f"<html>={'PASS' if has_html_open else 'FAIL'}, "
        f"</html>={'PASS' if has_html_close else 'FAIL'}, "
        f"無 <img>={'PASS' if not has_img else 'FAIL'}"
    )
    print(
        f"[條件 1] 投影片總頁數（<section class=\"slide\">）：{total_slides} 頁"
        f"（標準：{MIN_SLIDES}～{MAX_SLIDES} 頁）-> {'PASS' if count_ok else 'FAIL'}"
    )
    print("\n--- 逐頁檢查明細（條件 2：資料來源標註｜條件 3：純文字字數 <= 380）---")

    if total_slides == 0:
        print("  （無任何 <section class=\"slide\"> 投影片可檢查）")
    else:
        for idx, slide in enumerate(slides, 1):
            heading = str(slide["heading"] or "(無標題)")
            if len(heading) > 28:
                heading = heading[:27] + "…"
            plain_text = str(slide["plain_text"])
            char_count = int(slide["char_count"])  # type: ignore[arg-type]

            chars_ok = char_count <= MAX_CHARS_PER_SLIDE
            source_matches = extract_source_matches(plain_text)
            source_ok = len(source_matches) > 0
            slide_ok = chars_ok and source_ok

            if not source_ok:
                errors.append(
                    f"第 {idx} 頁（{heading}）缺少明確資料來源標註（須含「來源：」或「[0...」來源檔名標記）。"
                )
            if not chars_ok:
                errors.append(
                    f"第 {idx} 頁（{heading}）扣除 HTML 標籤後純文字為 {char_count} 字，超過上限 {MAX_CHARS_PER_SLIDE} 字。"
                )

            src_preview = "; ".join(source_matches[:2]) if source_matches else "無"
            if len(src_preview) > 55:
                src_preview = src_preview[:54] + "…"

            status_tag = "PASS" if slide_ok else "FAIL"
            print(
                f"  Slide {idx:02d} [{status_tag}] | 字數: {char_count:3d}/{MAX_CHARS_PER_SLIDE} "
                f"({'OK' if chars_ok else 'OVER'}) | 來源標註: {'OK' if source_ok else 'MISSING'} "
                f"({src_preview}) | 標題: {heading}"
            )

    print("\n=== 總結 ===")
    if errors:
        print(f"結果：FAIL（共 {len(errors)} 項未通過）")
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}")
        return False, errors

    print(f"結果：PASS（全部 4 項驗收條件及 {total_slides} 頁投影片皆通過）")
    return True, []


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    arg_parser = argparse.ArgumentParser(
        description="驗證 index.html 教學簡報頁數、資料來源標註、字數上限與 HTML 結構完整性。"
    )
    arg_parser.add_argument(
        "html_path",
        nargs="?",
        default=None,
        help="待檢查之 HTML 檔案路徑（預設檢查根目錄 index.html）",
    )
    args = arg_parser.parse_args()

    target = resolve_target_path(args.html_path)
    if not target.exists():
        print(f"[ERROR] 找不到目標簡報檔：{target}")
        return 2

    passed, _ = verify_html_file(target)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
