#!/usr/bin/env python3
"""
verify_slides.py — 多冊教學型 HTML 簡報系列自動化硬性驗收腳本

僅使用 Python 標準函式庫（argparse、dataclasses、html.parser、pathlib、re、sys），
驗證「1 個系列策展總入口（index.html）＋ 6 份跨連結簡報（deck_00_framework.html 至
deck_05_yugoslavia.html）」是否同時符合以下所有硬性條件：
  1. 根目錄 index.html 存在且 HTML 結構完整（不要求包含 <section class="slide">），
     並包含連向全部 6 份獨立簡報的有效相對路徑連結。
  2. 6 份獨立簡報（deck_00_framework.html～deck_05_yugoslavia.html）皆存在，
     且每份簡報的投影片總頁數（<section class="slide"> 數量）介於 5～8 頁之間。
  3. 每一頁投影片正文區（排除 <footer> 與 HTML 標籤）純文字不超過 260 個中文字
     （以 CJK 中文字元 [\\u4e00-\\u9fff] 計數）。
  4. 每一頁投影片皆包含 <footer> 標籤與明確資料來源標註（如「來源：」或「[0...」來源檔名標記）。
  5. 所有檔案之 HTML 結構完整（含 <!DOCTYPE html>、<html>、</html>），且所有
     <img src="..."> 皆使用相對路徑並指向本機 assets/ 內真實存在的非空圖片檔。
  6. 所有跨簡報連結（href="deck_..." 或 href="index.html"，含 #slide-N 錨點）
     皆使用相對路徑，且指向真實存在的目標檔案、有效頁碼（1 <= N <= 目標總頁數）
     與目標 HTML 內真實存在的 id="slide-N" 屬性。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

MIN_SLIDES_PER_DECK = 5
MAX_SLIDES_PER_DECK = 8
MAX_CJK_CHARS_PER_SLIDE = 260

ENTRY_HTML = "index.html"
DECK_FILES: tuple[str, ...] = (
    "deck_00_framework.html",
    "deck_01_russia.html",
    "deck_02_germany.html",
    "deck_03_china.html",
    "deck_04_spain.html",
    "deck_05_yugoslavia.html",
)
SERIES_HTML_FILES: set[str] = {ENTRY_HTML, *DECK_FILES}

CJK_CHAR_RE = re.compile(r"[\u4e00-\u9fff]")

# 允許之明確資料來源標註樣式：
# 1) 「來源：...」或「來源:...」（後方須有實質內容）
# 2) 「[0...」開頭之專案原始來源引用標記（例如 [01_russian_civil_war.md, 導言]）
SOURCE_LABEL_RE = re.compile(r"來源\s*[：:]\s*\S+")
SOURCE_FILE_RE = re.compile(r"\[0\d+[^\]]*\]")

DOCTYPE_RE = re.compile(r"<!doctype\s+html\b[^>]*>", re.IGNORECASE)
HTML_OPEN_RE = re.compile(r"<html\b[^>]*>", re.IGNORECASE)
HTML_CLOSE_RE = re.compile(r"</html\s*>", re.IGNORECASE)
URI_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
SLIDE_ANCHOR_RE = re.compile(r"^slide-(\d+)$")


@dataclass
class ParsedHtml:
    """儲存單一 HTML 檔案解析後的結構、投影片、圖片、連結與 ID 集合。"""

    path: Path
    has_doctype: bool
    has_html_open: bool
    has_html_close: bool
    unclosed_slide_error: bool
    slides: list[dict[str, object]]
    images: list[dict[str, object]]
    links: list[dict[str, object]]
    all_ids: set[str]
    slide_ids: dict[str, int]
    duplicate_slide_ids: list[str]


class SlideDeckParser(HTMLParser):
    """以標準函式庫 HTMLParser 解析投影片、正文／頁尾、<img>、<a> 與元素 id。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides: list[dict[str, object]] = []
        self.images: list[dict[str, object]] = []
        self.links: list[dict[str, object]] = []
        self.all_ids: set[str] = set()
        self.slide_ids: dict[str, int] = {}
        self.duplicate_slide_ids: list[str] = []
        self.unclosed_slide_error: bool = False

        self._in_slide: bool = False
        self._section_depth: int = 0
        self._footer_depth: int = 0
        self._has_footer: bool = False
        self._ignored_tag_stack: list[str] = []
        self._heading_capture_tag: str | None = None
        self._current_heading_parts: list[str] = []
        self._first_heading: str = ""
        self._current_slide_id: str = ""
        self._current_body_parts: list[str] = []
        self._current_footer_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_lower = tag.lower()
        attr_map = {k.lower(): (v if v is not None else "") for k, v in attrs}

        if tag_lower in ("script", "style"):
            self._ignored_tag_stack.append(tag_lower)
            return

        if self._ignored_tag_stack:
            return

        elem_id = attr_map.get("id", "").strip()
        if elem_id:
            if elem_id.startswith("slide-") and elem_id in self.all_ids:
                self.duplicate_slide_ids.append(elem_id)
            self.all_ids.add(elem_id)

        current_slide_idx = (len(self.slides) + 1) if self._in_slide else None

        if tag_lower == "img":
            self.images.append(
                {
                    "src": attr_map.get("src", ""),
                    "has_src": "src" in attr_map,
                    "slide_index": current_slide_idx,
                }
            )

        if tag_lower == "a" and "href" in attr_map:
            self.links.append(
                {
                    "href": attr_map.get("href", ""),
                    "slide_index": current_slide_idx,
                }
            )

        if tag_lower == "section":
            classes = attr_map.get("class", "").split()
            if "slide" in classes and not self._in_slide:
                self._in_slide = True
                self._section_depth = 1
                self._footer_depth = 0
                self._has_footer = False
                self._heading_capture_tag = None
                self._current_heading_parts = []
                self._first_heading = ""
                self._current_slide_id = elem_id
                self._current_body_parts = []
                self._current_footer_parts = []
                if elem_id:
                    self.slide_ids[elem_id] = len(self.slides) + 1
                return
            if self._in_slide:
                self._section_depth += 1

        if self._in_slide:
            if tag_lower == "footer":
                self._footer_depth += 1
                self._has_footer = True
                return
            if (
                self._footer_depth == 0
                and tag_lower in ("h1", "h2", "h3")
                and not self._first_heading
            ):
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

        if self._ignored_tag_stack:
            return

        if self._in_slide and self._heading_capture_tag == tag_lower:
            heading = re.sub(r"\s+", " ", "".join(self._current_heading_parts)).strip()
            if heading and not self._first_heading:
                self._first_heading = heading
            self._heading_capture_tag = None
            self._current_heading_parts = []

        if self._in_slide and tag_lower == "footer":
            if self._footer_depth > 0:
                self._footer_depth -= 1
            return

        if self._in_slide and tag_lower == "section":
            self._section_depth -= 1
            if self._section_depth <= 0:
                body_raw_text = "".join(self._current_body_parts)
                body_normalized = re.sub(r"\s+", " ", body_raw_text).strip()
                # 正文區純文字僅計算 CJK 中文字元，排除 <footer>、HTML 標籤與原文括號附註
                cjk_char_count = len(CJK_CHAR_RE.findall(body_raw_text))
                visible_char_count = len(re.sub(r"\s+", "", body_raw_text))

                footer_raw_text = "".join(self._current_footer_parts)
                footer_normalized = re.sub(r"\s+", " ", footer_raw_text).strip()

                self.slides.append(
                    {
                        "id": self._current_slide_id,
                        "heading": self._first_heading,
                        "body_text": body_normalized,
                        "cjk_char_count": cjk_char_count,
                        "visible_char_count": visible_char_count,
                        "has_footer": self._has_footer,
                        "footer_text": footer_normalized,
                        "unclosed_footer": self._footer_depth > 0,
                    }
                )
                self._in_slide = False
                self._section_depth = 0
                self._footer_depth = 0
                self._has_footer = False
                self._heading_capture_tag = None
                self._current_heading_parts = []
                self._first_heading = ""
                self._current_slide_id = ""
                self._current_body_parts = []
                self._current_footer_parts = []

    def handle_data(self, data: str) -> None:
        if not self._in_slide or self._ignored_tag_stack:
            return
        if self._footer_depth > 0:
            self._current_footer_parts.append(data)
            return
        self._current_body_parts.append(data)
        if self._heading_capture_tag:
            self._current_heading_parts.append(data)

    def handle_comment(self, data: str) -> None:
        # HTML 註解不計入投影片純文字
        return

    def finalize(self) -> None:
        if self._in_slide:
            self.unclosed_slide_error = True


def parse_html_file(target_path: Path) -> ParsedHtml:
    """讀取並解析單一 HTML 檔案，回傳結構化 ParsedHtml。"""
    raw_html = target_path.read_text(encoding="utf-8")
    parser = SlideDeckParser()
    parser.feed(raw_html)
    parser.close()
    parser.finalize()
    return ParsedHtml(
        path=target_path,
        has_doctype=bool(DOCTYPE_RE.search(raw_html)),
        has_html_open=bool(HTML_OPEN_RE.search(raw_html)),
        has_html_close=bool(HTML_CLOSE_RE.search(raw_html)),
        unclosed_slide_error=parser.unclosed_slide_error,
        slides=parser.slides,
        images=parser.images,
        links=parser.links,
        all_ids=parser.all_ids,
        slide_ids=parser.slide_ids,
        duplicate_slide_ids=parser.duplicate_slide_ids,
    )


def load_series_map(base_dir: Path) -> dict[str, ParsedHtml | None]:
    """預載系列根目錄下 index.html 與 6 份簡報的解析結果，供跨簡報錨點檢查。"""
    parsed_map: dict[str, ParsedHtml | None] = {}
    for fname in (ENTRY_HTML, *DECK_FILES):
        fpath = base_dir / fname
        parsed_map[fname] = parse_html_file(fpath) if fpath.is_file() else None
    return parsed_map


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


def validate_local_image(
    img_info: dict[str, object],
    target_path: Path,
    repo_root: Path,
) -> tuple[bool, str]:
    """嚴格驗證 <img> 的 src 必須指向本機 assets/ 內真實存在的非空檔案。"""
    src = str(img_info.get("src", "")).strip()
    has_src = bool(img_info.get("has_src"))
    slide_idx = img_info.get("slide_index")
    loc = f"第 {slide_idx} 頁" if slide_idx is not None else "投影片外全域區"

    if not has_src or not src:
        return False, f"{loc} 發現 <img> 標籤缺少有效的 src 屬性。"

    if src.startswith("//") or URI_SCHEME_RE.match(src):
        return (
            False,
            f"{loc} 圖片禁止使用外部網址或 URI scheme（src={src}），必須先下載至本機 assets/。",
        )

    if src.startswith("/") or src.startswith("\\"):
        return (
            False,
            f"{loc} 圖片必須使用相對路徑 assets/...（禁止絕對路徑：{src}）。",
        )

    if "?" in src or "#" in src:
        return (
            False,
            f"{loc} 本機圖片路徑不得包含查詢字串或錨點（src={src}）。",
        )

    norm_src = src.replace("\\", "/")
    if norm_src.startswith("./"):
        norm_src = norm_src[2:]

    parts = norm_src.split("/")
    if parts[0] != "assets" or len(parts) < 2 or any(p in ("", ".", "..") for p in parts):
        return (
            False,
            f"{loc} 圖片 src 必須指向本機 assets/ 目錄下的檔案（收到：{src}）。",
        )

    target_dir = target_path.resolve().parent
    assets_dir = target_dir / "assets"
    if not assets_dir.exists() and target_dir == (repo_root / "workflow_output").resolve():
        assets_dir = repo_root / "assets"

    resolved_base = assets_dir.resolve()
    resolved_file = (assets_dir / Path(*parts[1:])).resolve()
    if not resolved_file.is_relative_to(resolved_base):
        return False, f"{loc} 圖片路徑跳脫本機 assets/ 目錄（src={src}）。"
    if not resolved_file.is_file():
        return False, f"{loc} 圖片指向的本機檔案不存在：{norm_src}（預期位置：{resolved_file}）。"
    if resolved_file.stat().st_size == 0:
        return False, f"{loc} 圖片指向的本機檔案為空（0 bytes）：{norm_src}。"

    return True, f"{loc} -> {norm_src}"


def _is_external_series_reference(href: str) -> bool:
    """判斷帶協定前綴的 URL 是否誤用於指向本地簡報（deck_... 或 index.html）。"""
    lower = href.lower()
    if lower.startswith("file:"):
        return True
    path_no_frag = lower.split("#", 1)[0].split("?", 1)[0]
    if path_no_frag.endswith("/index.html") or "/deck_" in path_no_frag:
        return True
    return "localhost" in path_no_frag or "127.0.0.1" in path_no_frag


def _validate_slide_fragment(
    fragment: str,
    target_name: str,
    target_parsed: ParsedHtml,
    loc: str,
    href: str,
) -> tuple[bool, str]:
    """驗證連向簡報檔的 #slide-N 錨點頁碼範圍與對應 id="slide-N" 屬性。"""
    if fragment == "":
        return False, f"{loc} 跨簡報連結包含空的錨點片段（href={href}）。"

    match = SLIDE_ANCHOR_RE.match(fragment)
    if not match:
        return (
            False,
            f"{loc} 連向簡報 {target_name} 的錨點須採用 #slide-N 格式（收到 #{fragment}，href={href}）。",
        )

    slide_num = int(match.group(1))
    total_slides = len(target_parsed.slides)
    if slide_num < 1 or slide_num > total_slides:
        return (
            False,
            f"{loc} 連結 {href} 指向 {target_name} 第 {slide_num} 頁，但該簡報實際僅有 {total_slides} 頁（有效範圍 1～{total_slides}）。",
        )

    if fragment not in target_parsed.all_ids:
        return (
            False,
            f"{loc} 連結 {href} 的錨點 #{fragment} 在 {target_name} 中缺少對應 id=\"{fragment}\" 屬性。",
        )

    if fragment in target_parsed.slide_ids and target_parsed.slide_ids[fragment] != slide_num:
        actual_idx = target_parsed.slide_ids[fragment]
        return (
            False,
            f"{loc} 連結 {href} 的錨點 #{fragment} 在 {target_name} 中位於第 {actual_idx} 頁，與頁碼 {slide_num} 不符。",
        )

    return True, f"{loc} -> {target_name}#{fragment}（第 {slide_num}/{total_slides} 頁）"


def validate_cross_link(
    link_info: dict[str, object],
    source_name: str,
    source_parsed: ParsedHtml,
    parsed_map: dict[str, ParsedHtml | None],
) -> tuple[bool, str | None, str | None]:
    """
    驗證跨簡報／總入口超連結與頁碼錨點。

    回傳 (是否通過, 報表訊息或 None, 解析後之目標簡報檔名或 None)。
    純外部參考連結（如 Wikimedia Commons URL、mailto: 等）回傳 (True, None, None)。
    """
    href = str(link_info.get("href", "")).strip()
    slide_idx = link_info.get("slide_index")
    loc = f"第 {slide_idx} 頁" if slide_idx is not None else "投影片外區域"

    if not href:
        return False, f"{loc} 發現空的 <a href=\"\"> 連結。", None

    if href.startswith("//") or URI_SCHEME_RE.match(href):
        if _is_external_series_reference(href):
            return (
                False,
                f"{loc} 跨簡報連結必須使用同層相對路徑，禁止外部網址或 file://（href={href}）。",
                None,
            )
        return True, None, None

    if href.startswith("/") or href.startswith("\\"):
        return (
            False,
            f"{loc} 跨簡報連結必須使用相對路徑，禁止以 / 或 \\ 開頭（href={href}）。",
            None,
        )

    # 同頁內部錨點（#...）
    if href.startswith("#"):
        fragment = href[1:]
        if fragment == "":
            return False, f"{loc} 發現無效的空錨點連結 href=\"#\"。", None
        if fragment.startswith("slide"):
            if source_name == ENTRY_HTML:
                return (
                    False,
                    f"{loc} {ENTRY_HTML} 為導覽入口頁，不支援 #slide-N 投影片錨點（href={href}）。",
                    None,
                )
            ok, msg = _validate_slide_fragment(fragment, source_name, source_parsed, loc, href)
            return ok, msg, None
        if fragment not in source_parsed.all_ids:
            return (
                False,
                f"{loc} 頁內錨點 #{fragment} 在 {source_name} 中不存在對應 id 屬性（href={href}）。",
                None,
            )
        return True, f"{loc} -> #{fragment}", None

    # 相對路徑解析
    path_and_query, has_hash, fragment = href.partition("#")
    path_part, has_query, _ = path_and_query.partition("?")
    norm_path = path_part.replace("\\", "/")
    if norm_path.startswith("./"):
        norm_path = norm_path[2:]

    parts = norm_path.split("/")
    lower_path = norm_path.lower()
    is_series_like = (
        lower_path.startswith("deck_")
        or "index.html" in lower_path
        or lower_path.endswith(".html")
        or lower_path.endswith(".htm")
        or ".." in parts
    )
    if not is_series_like:
        return True, None, None

    if has_query:
        return False, f"{loc} 跨簡報連結不得包含查詢字串（href={href}）。", None

    if len(parts) != 1 or parts[0] in ("", ".", ".."):
        return (
            False,
            f"{loc} 跨簡報連結須為同層相對路徑檔名（如 deck_00_framework.html 或 index.html），收到：{href}。",
            None,
        )

    target_name = parts[0]
    if target_name not in SERIES_HTML_FILES:
        return (
            False,
            f"{loc} 跨簡報連結指向未定義之系列目標檔案：{target_name}（href={href}）。",
            None,
        )

    target_parsed = parsed_map.get(target_name)
    if target_parsed is None:
        return (
            False,
            f"{loc} 跨簡報連結目標檔案不存在：{target_name}（href={href}）。",
            None,
        )

    if has_hash:
        if target_name == ENTRY_HTML:
            if fragment == "":
                return False, f"{loc} 連結包含空的錨點片段（href={href}）。", None
            if fragment.startswith("slide"):
                return (
                    False,
                    f"{loc} {ENTRY_HTML} 為導覽入口頁，不支援 #slide-N 投影片錨點（href={href}）。",
                    None,
                )
            if fragment not in target_parsed.all_ids:
                return (
                    False,
                    f"{loc} 連結錨點 #{fragment} 在 {ENTRY_HTML} 中不存在對應 id（href={href}）。",
                    None,
                )
            return True, f"{loc} -> {target_name}#{fragment}", target_name

        ok, msg = _validate_slide_fragment(fragment, target_name, target_parsed, loc, href)
        return ok, msg, (target_name if ok else None)

    return True, f"{loc} -> {target_name}", target_name


def _collect_structure_errors(parsed: ParsedHtml, label: str) -> list[str]:
    """檢查基本 HTML 結構完整性。"""
    errors: list[str] = []
    if not parsed.has_doctype:
        errors.append(f"[{label}] 缺少 <!DOCTYPE html> 宣告。")
    if not parsed.has_html_open:
        errors.append(f"[{label}] 缺少 <html> 起始標籤。")
    if not parsed.has_html_close:
        errors.append(f"[{label}] 缺少 </html> 結尾標籤。")
    if parsed.unclosed_slide_error:
        errors.append(f"[{label}] 偵測到未正確閉合的 <section class=\"slide\"> 標籤。")
    for dup_id in parsed.duplicate_slide_ids:
        errors.append(f"[{label}] 偵測到重複的投影片錨點 id=\"{dup_id}\"。")
    return errors


def _check_images_and_links(
    parsed: ParsedHtml,
    label: str,
    parsed_map: dict[str, ParsedHtml | None],
    repo_root: Path,
) -> tuple[list[tuple[bool, str]], list[tuple[bool, str]], set[str], list[str]]:
    """檢查單一檔案的所有 <img> 與跨簡報 <a> 連結，並回傳已連接的目標檔名集合與錯誤清單。"""
    errors: list[str] = []

    img_results: list[tuple[bool, str]] = []
    for img_info in parsed.images:
        ok, detail = validate_local_image(img_info, parsed.path, repo_root)
        img_results.append((ok, detail))
        if not ok:
            errors.append(f"[{label}] {detail}")

    link_results: list[tuple[bool, str]] = []
    linked_targets: set[str] = set()
    for link_info in parsed.links:
        ok, msg, target_name = validate_cross_link(link_info, label, parsed, parsed_map)
        if msg is not None:
            link_results.append((ok, msg))
        if not ok and msg is not None:
            errors.append(f"[{label}] {msg}")
        if ok and target_name is not None:
            linked_targets.add(target_name)

    return img_results, link_results, linked_targets, errors


def verify_entry_file(
    entry_path: Path,
    parsed_map: dict[str, ParsedHtml | None],
    repo_root: Path,
) -> tuple[bool, list[str]]:
    """驗收系列策展總入口 index.html（不要求含 <section class="slide">）。"""
    print(f"\n=== 總入口驗收：{ENTRY_HTML} ===")
    parsed = parsed_map.get(ENTRY_HTML)
    if parsed is None:
        msg = f"[{ENTRY_HTML}] 找不到系列策展總入口檔案：{entry_path}"
        print(f"  [FAIL] {msg}")
        return False, [msg]

    struct_errors = _collect_structure_errors(parsed, ENTRY_HTML)
    errors = list(struct_errors)
    img_results, link_results, linked_targets, asset_link_errors = _check_images_and_links(
        parsed, ENTRY_HTML, parsed_map, repo_root
    )
    errors.extend(asset_link_errors)

    missing_decks = [deck for deck in DECK_FILES if deck not in linked_targets]
    for deck in missing_decks:
        errors.append(f"[{ENTRY_HTML}] 缺少連向 {deck} 的有效相對路徑連結。")

    imgs_ok = all(ok for ok, _ in img_results)
    links_ok = all(ok for ok, _ in link_results) and not missing_decks
    struct_ok = not struct_errors

    print(
        f"  HTML 結構={'PASS' if struct_ok else 'FAIL'} | "
        f"<img> 本機 assets/={'PASS' if imgs_ok else 'FAIL'}（{len(img_results)} 張） | "
        f"6 份簡報入口連結={'PASS' if links_ok else 'FAIL'}（已涵蓋 {len(DECK_FILES) - len(missing_decks)}/{len(DECK_FILES)} 份）"
    )
    for idx, (ok, detail) in enumerate(img_results, 1):
        print(f"    Image {idx:02d} [{'PASS' if ok else 'FAIL'}] | {detail}")
    for idx, (ok, detail) in enumerate(link_results, 1):
        print(f"    Link  {idx:02d} [{'PASS' if ok else 'FAIL'}] | {detail}")
    if missing_decks:
        print(f"    [FAIL] 缺漏簡報連結：{', '.join(missing_decks)}")

    return len(errors) == 0, errors


def verify_deck_file(
    deck_path: Path,
    parsed_map: dict[str, ParsedHtml | None],
    repo_root: Path,
) -> tuple[bool, list[str]]:
    """驗收單一獨立簡報檔（5～8 頁、<=260 中文字、<footer> 出處、圖片與跨簡報連結）。"""
    label = deck_path.name
    print(f"\n=== 獨立簡報驗收：{label} ===")
    parsed = parsed_map.get(label)
    if parsed is None and deck_path.is_file():
        parsed = parse_html_file(deck_path)

    if parsed is None:
        msg = f"[{label}] 找不到簡報檔案：{deck_path}"
        print(f"  [FAIL] {msg}")
        return False, [msg]

    struct_errors = _collect_structure_errors(parsed, label)
    errors = list(struct_errors)
    img_results, link_results, _, asset_link_errors = _check_images_and_links(
        parsed, label, parsed_map, repo_root
    )
    errors.extend(asset_link_errors)

    slides = parsed.slides
    total_slides = len(slides)
    count_ok = MIN_SLIDES_PER_DECK <= total_slides <= MAX_SLIDES_PER_DECK
    if not count_ok:
        errors.append(
            f"[{label}] 投影片總頁數為 {total_slides} 頁，未落在允許範圍 {MIN_SLIDES_PER_DECK}～{MAX_SLIDES_PER_DECK} 頁之間。"
        )

    imgs_ok = all(ok for ok, _ in img_results)
    links_ok = all(ok for ok, _ in link_results)
    struct_ok = not struct_errors

    print(
        f"  HTML 結構={'PASS' if struct_ok else 'FAIL'} | "
        f"頁數={total_slides} 頁（標準 {MIN_SLIDES_PER_DECK}～{MAX_SLIDES_PER_DECK}）->{'PASS' if count_ok else 'FAIL'} | "
        f"<img>={'PASS' if imgs_ok else 'FAIL'}（{len(img_results)} 張） | "
        f"跨簡報連結={'PASS' if links_ok else 'FAIL'}（{len(link_results)} 條）"
    )

    for idx, (ok, detail) in enumerate(img_results, 1):
        print(f"    Image {idx:02d} [{'PASS' if ok else 'FAIL'}] | {detail}")
    for idx, (ok, detail) in enumerate(link_results, 1):
        print(f"    Link  {idx:02d} [{'PASS' if ok else 'FAIL'}] | {detail}")

    if total_slides == 0:
        print("    （無任何 <section class=\"slide\"> 投影片可檢查）")
    else:
        for idx, slide in enumerate(slides, 1):
            heading = str(slide["heading"] or "(無標題)")
            if len(heading) > 26:
                heading = heading[:25] + "…"
            cjk_count = int(slide["cjk_char_count"])  # type: ignore[arg-type]
            vis_count = int(slide["visible_char_count"])  # type: ignore[arg-type]
            has_footer = bool(slide["has_footer"])
            unclosed_footer = bool(slide["unclosed_footer"])
            footer_text = str(slide["footer_text"])

            chars_ok = cjk_count <= MAX_CJK_CHARS_PER_SLIDE
            source_matches = extract_source_matches(footer_text)
            source_ok = has_footer and (not unclosed_footer) and (len(source_matches) > 0)
            slide_ok = chars_ok and source_ok

            if not has_footer:
                errors.append(f"[{label}] 第 {idx} 頁（{heading}）缺少 <footer> 資料來源標註區塊。")
            elif unclosed_footer:
                errors.append(f"[{label}] 第 {idx} 頁（{heading}）偵測到未正確閉合的 <footer> 標籤。")
            elif not source_matches:
                errors.append(
                    f"[{label}] 第 {idx} 頁（{heading}）的 <footer> 區塊缺少明確資料來源標註（須含「來源：」或「[0...」來源檔名標記）。"
                )

            if not chars_ok:
                errors.append(
                    f"[{label}] 第 {idx} 頁（{heading}）正文區（排除 <footer> 與 HTML 標籤）含 {cjk_count} 個中文字，超過上限 {MAX_CJK_CHARS_PER_SLIDE} 個中文字。"
                )

            src_preview = "; ".join(source_matches[:2]) if source_matches else "無"
            if len(src_preview) > 45:
                src_preview = src_preview[:44] + "…"

            footer_tag = "OK" if source_ok else ("NO_FOOTER" if not has_footer else "MISSING_SRC")
            status_tag = "PASS" if slide_ok else "FAIL"
            print(
                f"    Slide {idx:02d} [{status_tag}] | 中文字: {cjk_count:3d}/{MAX_CJK_CHARS_PER_SLIDE} "
                f"({'OK' if chars_ok else 'OVER'}, 可視字元:{vis_count:3d}) | "
                f"<footer>來源: {footer_tag} ({src_preview}) | 標題: {heading}"
            )

    return len(errors) == 0, errors


def verify_series(base_dir: Path, repo_root: Path) -> bool:
    """驗收完整「1 總入口 ＋ 6 份獨立簡報」系列，回傳是否全數通過。"""
    print("============================================================")
    print("教學簡報系列自動化驗收報告（1 總入口 ＋ 6 份跨連結獨立簡報）")
    print(f"檢查目錄：{base_dir}")
    print("============================================================")

    parsed_map = load_series_map(base_dir)
    all_errors: list[str] = []

    _, entry_errors = verify_entry_file(base_dir / ENTRY_HTML, parsed_map, repo_root)
    all_errors.extend(entry_errors)

    for deck_name in DECK_FILES:
        _, deck_errors = verify_deck_file(base_dir / deck_name, parsed_map, repo_root)
        all_errors.extend(deck_errors)

    print("\n=== 系列驗收總結 ===")
    if all_errors:
        print(f"結果：FAIL（共 {len(all_errors)} 項未通過）")
        for i, err in enumerate(all_errors, 1):
            print(f"  {i}. {err}")
        return False

    print(
        f"結果：PASS（{ENTRY_HTML} 總入口與全部 {len(DECK_FILES)} 份獨立簡報皆通過所有驗收條件）"
    )
    return True


def resolve_base_dir() -> tuple[Path, Path]:
    """決定預設驗收目錄（優先取包含系列檔案的目前工作目錄，否則取專案根目錄）。"""
    repo_root = Path(__file__).resolve().parent.parent
    cwd = Path.cwd()
    if (cwd / ENTRY_HTML).exists() or any((cwd / d).exists() for d in DECK_FILES):
        return cwd, repo_root
    return repo_root, repo_root


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    arg_parser = argparse.ArgumentParser(
        description=(
            "驗證多冊教學簡報系列：index.html 總入口與 deck_00_framework.html～deck_05_yugoslavia.html"
            "（各 5～8 頁、<=260 中文字、<footer> 來源、本機 assets/ 圖片與跨簡報 #slide-N 錨點）。"
        )
    )
    arg_parser.add_argument(
        "target_path",
        nargs="?",
        default=None,
        help="待檢查之系列目錄或單一 HTML 檔案路徑（預設檢查專案根目錄全系列 1+6 份檔案）",
    )
    args = arg_parser.parse_args()

    default_base, repo_root = resolve_base_dir()

    if args.target_path is None:
        return 0 if verify_series(default_base, repo_root) else 1

    target = Path(args.target_path)
    if not target.exists():
        print(f"[ERROR] 找不到目標路徑：{target}")
        return 2

    if target.is_dir():
        return 0 if verify_series(target, repo_root) else 1

    base_dir = target.resolve().parent
    parsed_map = load_series_map(base_dir)
    if target.name == ENTRY_HTML:
        passed, errs = verify_entry_file(target, parsed_map, repo_root)
    else:
        if target.name not in parsed_map:
            parsed_map[target.name] = parse_html_file(target)
        passed, errs = verify_deck_file(target, parsed_map, repo_root)

    print("\n=== 單檔驗收總結 ===")
    if errs:
        print(f"結果：FAIL（共 {len(errs)} 項未通過）")
        for i, err in enumerate(errs, 1):
            print(f"  {i}. {err}")
        return 1

    print(f"結果：PASS（{target.name} 通過驗收）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
