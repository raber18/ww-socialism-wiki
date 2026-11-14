# 教學簡報審查與自動化驗收報告（`report.md`）

## 一、重構演進與最終執行摘要

- **教學主題**：戰火下的路線分歧：1914–1945 歐亞社會主義流派與地方勢力的崛起比較
- **目標受眾**：沒有歷史背景的初學者
- **架構重構決策**：由最初「單一 12 頁純文字條列簡報（`v1`）」及過度階段的 15 頁單檔大綱，**退回重構為「`1` 份策展總入口（[index.html](../index.html)）＋ `6` 份按總論與國家獨立拆分之圖文策展簡報（[deck_00_framework.html](../deck_00_framework.html) 至 [deck_05_yugoslavia.html](../deck_05_yugoslavia.html)）」**，徹底解決跨國時間軸跳躍問題，讓每個戰區擁有完整、順時序的獨立故事線並以超連結跨檔互通。
- **總規模統計**：
  - 策展總入口：`1` 頁（[index.html](../index.html)，內嵌歐亞五大戰區連動 SVG 圖與 6 張策展導覽卡）
  - 獨立簡報：`6` 份（每份 6～7 頁，共 **37 頁** `<section class="slide">`，均符合每份 5～8 頁規範）
  - 本機歷史影像：`5` 張 Wikimedia Commons 核驗圖檔置於 `assets/`（授權與來源見 [assets/credits.md](../assets/credits.md)），總入口全部展示 5 張、國別簡報第 2 頁各展示對應戰區 1 張
  - 覆蓋地區與來源：`5` 大地理區域（俄國、德國、中國、西班牙、南斯拉夫），`6` 篇 `raw/` 原始來源與 `28` 張證據卡（[cards.md](cards.md)）
- **最終驗收狀態**：**PASS（Exit Code 0）**——完成全系列「去 AI 模板化」與 768p 視覺精修後，執行 `python scripts/verify_slides.py` 對「1 總入口 ＋ 6 份獨立簡報（共 37 頁）」進行結構、字數（`<= 260` 中文字）、`<footer>` 來源、`assets/` 本機圖片與全網跨簡報 `#slide-N` 錨點檢查，全數項目 100% 通過；`raw/` 與 `wiki/` 全程維持唯讀零異動。

---

## 二、視覺與互動規格檢核（去 AI 模板化與歷史雜誌策展風）

1. **色彩、字體與排版紀律**：全系列採米白紙色（`#F7F4EB`）、深炭墨文字（`#1C1917`）、暗紅（`#991B1B`）與深藍（`#1E3A5F`）；主標題與引文採襯線體（`"Noto Serif TC", "Source Han Serif TC", Georgia, serif`），內文採無襯線體；各國第 1 頁皆採全版面深色典藏封面（`<section class="slide slide--cover">`）。
2. **去 AI 模板化與雜誌版型重構**：
   - 全 6 冊（[deck_00_framework.html](../deck_00_framework.html)～[deck_05_yugoslavia.html](../deck_05_yugoslavia.html)）全面刪除全大寫英文 Kicker（如 `01 · ...`），統一改為精簡繁體中文篇章眉標（如 `俄國篇・體制轉折`、`西班牙篇・五月事件與蘇援`）。
   - 消除 `<h2>` 下方滿版 `border-bottom` 與容器上下雙重橫線，投影片高度下修為 `min-height: 500px`（`padding: 26px 40px 18px`）以完整適配 768p 筆電視口。
   - 打破單調三列等寬表格（移除 `.chronology-rows` 制式框格），改採「左側大字引文／關鍵數據 ＋ 右側兩段短文」（`.magazine-split`）與「無外框垂直細線雙欄／三欄」（`.editorial-split`、大號襯線數字錨點 `01/02/03`）交錯編排，並於關鍵人名與核心概念加上深墨色 `<strong>` 強調以利 3 秒掃視。
   - 修正 [index.html](../index.html) Hero 右側為讀者視角觀展導讀、擴大上方 SVG 標籤寬度並調高弧線避開壓字、將下方時間軸巴斯馬奇文字移至虛線右側加底色襯墊，並將全系列頂部導覽列統一去檔名為「`策展總覽`」。
3. **固定頂部系列導覽列與離線互動**：7 份 HTML 頂部皆配置一致的相對路徑導覽列（`策展總覽`、`00 總論`～`05 南斯拉夫`）；6 份簡報依序設定 `id="slide-1"`～`id="slide-N"`，以 Vanilla JS 支援 `ArrowLeft`/`ArrowRight`/`Space`/`PageUp`/`PageDown`/`Home`/`End` 切換、頁碼點、進度條，並支援解析 `location.hash` 與監聽 `hashchange` 直達指定投影片。
4. **100% 溯源與硬性紅線**：正文（排除 `<footer>` 與標籤）實測控在 `116～253` 個中文字（低於 `260` 字硬性上限），保留完整歷史數據與對立史觀，每頁底部 `<footer>` 實標 `[來源檔名, 段落標題]`，資料缺漏皆依 [cards.md](cards.md) 誠實揭示。

---

## 三、全系列逐冊逐頁自動化驗收數據明細

依據 `python scripts/verify_slides.py`（[scripts/verify_slides.py](../scripts/verify_slides.py)）於根目錄 `c:\Users\raber\Desktop\ww-socialism-wiki` 實測結果彙整：

### 1. 總入口頁面（[index.html](../index.html)）

| 檢查項目 | 實測結果 | 明細說明 |
| :--- | :--- | :--- |
| HTML 結構與路徑規範 | **PASS** | 全數使用相對路徑，無 `/` 絕對路徑 |
| 本機 `assets/` 圖片（5 張） | **PASS** | `assets/01_russia.jpg`、`assets/02_germany.jpg`、`assets/03_china_warlords.png`、`assets/04_spain.jpg`、`assets/05_yugoslavia.jpg` |
| 6 份簡報入口與跨連結（15 條） | **PASS** | 頂部導覽、主按鈕、`#series-map` 與 6 張策展卡已完整涵蓋 `deck_00`～`deck_05` |

### 2. 逐冊簡報逐頁中文字數與元件統計（共 6 份，37 頁）

| 簡報檔名 | 頁數 | 本機 `<img>` | 跨簡報連結數 | 逐頁正文 CJK 中文字數（上限 `<= 260`，括號為可視字元） | `<footer>` 來源 | 驗收狀態 |
| :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| [deck_00_framework.html](../deck_00_framework.html) | 6 | 0 | 13（PASS） | `#1`: `117`(209)、`#2`: `210`(356)、`#3`: `177`(303)、`#4`: `221`(379)、`#5`: `217`(286)、`#6`: `183`(206) | 6/6 OK | **PASS** |
| [deck_01_russia.html](../deck_01_russia.html) | 6 | 1 (`assets/01_russia.jpg`) | 10（PASS） | `#1`: `128`(207)、`#2`: `133`(306)、`#3`: `185`(360)、`#4`: `153`(306)、`#5`: `176`(297)、`#6`: `190`(299) | 6/6 OK | **PASS** |
| [deck_02_germany.html](../deck_02_germany.html) | 6 | 1 (`assets/02_germany.jpg`) | 10（PASS） | `#1`: `124`(211)、`#2`: `127`(262)、`#3`: `165`(274)、`#4`: `172`(268)、`#5`: `194`(342)、`#6`: `173`(290) | 6/6 OK | **PASS** |
| [deck_03_china.html](../deck_03_china.html) | 7 | 1 (`assets/03_china_warlords.png`) | 10（PASS） | `#1`: `116`(199)、`#2`: `165`(298)、`#3`: `223`(349)、`#4`: `224`(328)、`#5`: `211`(332)、`#6`: `213`(293)、`#7`: `177`(219) | 7/7 OK | **PASS** |
| [deck_04_spain.html](../deck_04_spain.html) | 6 | 1 (`assets/04_spain.jpg`) | 13（PASS） | `#1`: `127`(211)、`#2`: `174`(270)、`#3`: `202`(287)、`#4`: `232`(368)、`#5`: `218`(313)、`#6`: `237`(364) | 6/6 OK | **PASS** |
| [deck_05_yugoslavia.html](../deck_05_yugoslavia.html) | 6 | 1 (`assets/05_yugoslavia.jpg`) | 13（PASS） | `#1`: `141`(230)、`#2`: `190`(261)、`#3`: `237`(342)、`#4`: `253`(376)、`#5`: `239`(353)、`#6`: `242`(271) | 6/6 OK | **PASS** |
| **系列合計** | **37** | **5** | **69＋15** | 全系列範圍 **`116`～`253` / `260`** | **37/37 OK** | **PASS** |

---

## 四、跨簡報錨點連動網檢查結果

除每份 HTML 固定頂部 7 條系列導覽列連結（共 `7 × 7 = 49` 條）及 `index.html` 內頁導覽連結（含 `#series-map` 與 6 張策展卡）外，簡報正文頁共設置 **20 條具語意連動與章節導引功能之跨檔連結**，全部指向真實目標檔案與對應 `#slide-N` 頁面：

| 來源頁面 | 目標錨點（實際驗證頁數） | 跨國連動／策展脈絡 | 檢查狀態 |
| :--- | :--- | :--- | :---: |
| `deck_00_framework.html#slide-4` | `deck_01_russia.html#slide-6`（6/6） | 白俄大流亡與契卡機制源頭 | **PASS** |
| `deck_00_framework.html#slide-4` | `deck_03_china.html#slide-4`（4/7） | 1923 蘇援改組、FT-17 坦克與白俄傭兵入華 | **PASS** |
| `deck_00_framework.html#slide-4` | `deck_04_spain.html#slide-4`（4/6） | 蘇聯 X 行動、*checas* 外溢與國際縱隊 | **PASS** |
| `deck_00_framework.html#slide-4` | `deck_05_yugoslavia.html#slide-3`（3/6） | 西班牙國際縱隊老兵返南國任骨幹 | **PASS** |
| `deck_00_framework.html#slide-6` | `index.html`、`deck_01_russia.html` | 返回策展總覽、進入第一章俄國篇 | **PASS** |
| `deck_01_russia.html#slide-6` | `deck_02_germany.html#slide-3`（3/6） | 德國 SPD 恐懼俄式內戰促成雙重妥協 | **PASS** |
| `deck_01_russia.html#slide-6` | `deck_03_china.html#slide-4`（4/7） | 白俄軍火與列寧式黨軍改組東傳中國 | **PASS** |
| `deck_01_russia.html#slide-6` | `deck_04_spain.html#slide-4`（4/6） | 契卡名號與白俄流亡者遠赴西班牙 | **PASS** |
| `deck_02_germany.html#slide-3` | `deck_01_russia.html#slide-4`（4/6） | 對照布勞恩引為警戒的俄國四方內戰 | **PASS** |
| `deck_02_germany.html#slide-6` | `deck_04_spain.html#slide-5`（5/6） | 威瑪崩潰後德軍（禿鷹軍團）介入西班牙 | **PASS** |
| `deck_02_germany.html#slide-6` | `deck_03_china.html#slide-1`（1/7） | 章節導引：進入第三章中國篇 | **PASS** |
| `deck_03_china.html#slide-4` | `deck_01_russia.html#slide-6`（6/6） | 追溯白俄流亡與海參崴軍火起點 | **PASS** |
| `deck_03_china.html#slide-7` | `deck_00_framework.html#slide-5`（5/6）、`deck_04_spain.html#slide-1`（1/6） | 回顧地方成敗公式、進入第四章西班牙篇 | **PASS** |
| `deck_04_spain.html#slide-4` | `deck_01_russia.html#slide-3`（3/6）、`deck_05_yugoslavia.html#slide-3`（3/6） | 追溯契卡清洗源頭、銜接南斯拉夫老兵骨幹 | **PASS** |
| `deck_04_spain.html#slide-5` | `deck_02_germany.html#slide-6`（6/6）、`deck_00_framework.html#slide-5`（5/6） | 對照德國後續干預與塞德曼後方治安公式 | **PASS** |
| `deck_04_spain.html#slide-6` | `deck_00_framework.html#slide-3`（3/6）、`deck_05_yugoslavia.html#slide-1`（1/6） | 對照左翼四派路線、進入第五章南斯拉夫篇 | **PASS** |
| `deck_05_yugoslavia.html#slide-3` | `deck_04_spain.html#slide-4`（4/6）、`deck_00_framework.html#slide-4`（4/6） | 回望西班牙國際縱隊與歐亞六大連動鏈 | **PASS** |
| `deck_05_yugoslavia.html#slide-5` | `deck_01_russia.html#slide-6`（6/6）、`deck_00_framework.html#slide-5`（5/6） | 對比蘇聯模板分歧與五國結局路徑 | **PASS** |
| `deck_05_yugoslavia.html#slide-6` | `deck_00_framework.html#slide-5`（5/6）、`index.html` | 系列收官回望公式並返回策展總覽 | **PASS** |

---

## 五、全系列自動化總驗收完整輸出（Exit Code 0）

以下為執行 `python scripts/verify_slides.py`（無參數，對整個系列執行完整驗證）之未截斷實測輸出：

```text
============================================================
教學簡報系列自動化驗收報告（1 總入口 ＋ 6 份跨連結獨立簡報）
檢查目錄：C:\Users\raber\Desktop\ww-socialism-wiki
============================================================

=== 總入口驗收：index.html ===
  HTML 結構=PASS | <img> 本機 assets/=PASS（5 張） | 6 份簡報入口連結=PASS（已涵蓋 6/6 份）
    Image 01 [PASS] | 投影片外全域區 -> assets/01_russia.jpg
    Image 02 [PASS] | 投影片外全域區 -> assets/02_germany.jpg
    Image 03 [PASS] | 投影片外全域區 -> assets/03_china_warlords.png
    Image 04 [PASS] | 投影片外全域區 -> assets/04_spain.jpg
    Image 05 [PASS] | 投影片外全域區 -> assets/05_yugoslavia.jpg
    Link  01 [PASS] | 投影片外區域 -> index.html
    Link  02 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  03 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  04 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  05 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  06 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  07 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html
    Link  08 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  09 [PASS] | 投影片外區域 -> #series-map
    Link  10 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  11 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  12 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  13 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  14 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  15 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html

=== 獨立簡報驗收：deck_00_framework.html ===
  HTML 結構=PASS | 頁數=6 頁（標準 5～8）->PASS | <img>=PASS（0 張） | 跨簡報連結=PASS（13 條）
    Link  01 [PASS] | 投影片外區域 -> index.html
    Link  02 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  03 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  04 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  05 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  06 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  07 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html
    Link  08 [PASS] | 第 4 頁 -> deck_01_russia.html#slide-6（第 6/6 頁）
    Link  09 [PASS] | 第 4 頁 -> deck_03_china.html#slide-4（第 4/7 頁）
    Link  10 [PASS] | 第 4 頁 -> deck_04_spain.html#slide-4（第 4/6 頁）
    Link  11 [PASS] | 第 4 頁 -> deck_05_yugoslavia.html#slide-3（第 3/6 頁）
    Link  12 [PASS] | 第 6 頁 -> index.html
    Link  13 [PASS] | 第 6 頁 -> deck_01_russia.html
    Slide 01 [PASS] | 中文字: 117/260 (OK, 可視字元:209) | <footer>來源: OK ([01_russian_civil_war.md, 導言]; [02_german_re…) | 標題: 大戰打碎舊帝國後，誰能從亂世蛻變為全國政權？
    Slide 02 [PASS] | 中文字: 210/260 (OK, 可視字元:356) | <footer>來源: OK ([01_russian_civil_war.md, Background]; [02_g…) | 標題: 兩次大戰打碎舊中央，在歐亞五大戰場留下權力真空
    Slide 03 [PASS] | 中文字: 177/260 (OK, 可視字元:303) | <footer>來源: OK ([01_russian_civil_war.md, 導言]; [02_german_re…) | 標題: 同喊社會主義，四條奪權路線的衝突讓左翼經常互打
    Slide 04 [PASS] | 中文字: 221/260 (OK, 可視字元:379) | <footer>來源: OK ([01_russian_civil_war.md, Aftermath]; [03_sp…) | 標題: 從海參崴坦克到西班牙老兵，六條跨國鏈改寫五國戰局
    Slide 05 [PASS] | 中文字: 217/260 (OK, 可視字元:286) | <footer>來源: OK ([01_russian_civil_war.md, 導言; Aftermath]; [0…) | 標題: 地方勢力能否掌權，取決於土改、統戰與後方治安
    Slide 06 [PASS] | 中文字: 183/260 (OK, 可視字元:206) | <footer>來源: OK ([01_russian_civil_war.md, 導言]; [02_german_re…) | 標題: 帶著三個分析工具，走進歐亞五國的現場時間軸

=== 獨立簡報驗收：deck_01_russia.html ===
  HTML 結構=PASS | 頁數=6 頁（標準 5～8）->PASS | <img>=PASS（1 張） | 跨簡報連結=PASS（10 條）
    Image 01 [PASS] | 第 2 頁 -> assets/01_russia.jpg
    Link  01 [PASS] | 投影片外區域 -> index.html
    Link  02 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  03 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  04 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  05 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  06 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  07 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html
    Link  08 [PASS] | 第 6 頁 -> deck_02_germany.html#slide-3（第 3/6 頁）
    Link  09 [PASS] | 第 6 頁 -> deck_03_china.html#slide-4（第 4/7 頁）
    Link  10 [PASS] | 第 6 頁 -> deck_04_spain.html#slide-4（第 4/6 頁）
    Slide 01 [PASS] | 中文字: 128/260 (OK, 可視字元:207) | <footer>來源: OK ([01_russian_civil_war.md, 導言; Geography and …) | 標題: 從民選蘇維埃到一黨專政：1917–1921 俄國的…
    Slide 02 [PASS] | 中文字: 133/260 (OK, 可視字元:306) | <footer>來源: OK ([01_russian_civil_war.md, Background; Warfar…) | 標題: 1917 年沙皇退位後，俄國陷入雙重政權並爆發十月…
    Slide 03 [PASS] | 中文字: 185/260 (OK, 可視字元:360) | <footer>來源: OK ([01_russian_civil_war.md, Background; Warfar…) | 標題: 1918 年敗選後解散立憲會議，接連排除左翼盟友走…
    Slide 04 [PASS] | 中文字: 153/260 (OK, 可視字元:306) | <footer>來源: OK ([01_russian_civil_war.md, 導言; Background; Wa…) | 標題: 1918–1921 四方內戰：靠強制徵兵與 83%…
    Slide 05 [PASS] | 中文字: 176/260 (OK, 可視字元:297) | <footer>來源: OK ([01_russian_civil_war.md, Background; Warfar…) | 標題: 1921 年喀琅施塔得起義遭鎮壓，派系禁令與新經濟…
    Slide 06 [PASS] | 中文字: 190/260 (OK, 可視字元:299) | <footer>來源: OK ([01_russian_civil_war.md, 導言; Background; Wa…) | 標題: 史觀交鋒：戰時防衛或一黨專政？以及俄國內戰的跨國餘波

=== 獨立簡報驗收：deck_02_germany.html ===
  HTML 結構=PASS | 頁數=6 頁（標準 5～8）->PASS | <img>=PASS（1 張） | 跨簡報連結=PASS（10 條）
    Image 01 [PASS] | 第 2 頁 -> assets/02_germany.jpg
    Link  01 [PASS] | 投影片外區域 -> index.html
    Link  02 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  03 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  04 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  05 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  06 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  07 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html
    Link  08 [PASS] | 第 3 頁 -> deck_01_russia.html#slide-4（第 4/6 頁）
    Link  09 [PASS] | 第 6 頁 -> deck_04_spain.html#slide-5（第 5/6 頁）
    Link  10 [PASS] | 第 6 頁 -> deck_03_china.html#slide-1（第 1/7 頁）
    Slide 01 [PASS] | 中文字: 124/260 (OK, 可視字元:211) | <footer>來源: OK ([02_german_revolution_1918_1919.md, 導言; Revo…) | 標題: 工兵委員會為何主動讓權：1918–1919 德國革…
    Slide 02 [PASS] | 中文字: 127/260 (OK, 可視字元:262) | <footer>來源: OK ([02_german_revolution_1918_1919.md, Revoluti…) | 標題: 1918 年 11 月基爾水兵起義，柏林同日宣告兩…
    Slide 03 [PASS] | 中文字: 165/260 (OK, 可視字元:274) | <footer>來源: OK ([02_german_revolution_1918_1919.md, Backgrou…) | 標題: 懼怕俄式內戰，SPD 與舊軍方及資方簽下雙重妥協
    Slide 04 [PASS] | 中文字: 172/260 (OK, 可視字元:268) | <footer>來源: OK ([02_german_revolution_1918_1919.md, Revoluti…) | 標題: 344 對 98 票：全德工兵委員會主動交權給國民…
    Slide 05 [PASS] | 中文字: 194/260 (OK, 可視字元:342) | <footer>來源: OK ([02_german_revolution_1918_1919.md, 導言; Revo…) | 標題: 自由軍團血腥鎮壓斯巴達克與地方蘇維埃，左翼永久撕裂
    Slide 06 [PASS] | 中文字: 173/260 (OK, 可視字元:290) | <footer>來源: OK ([02_german_revolution_1918_1919.md, 導言; Impa…) | 標題: 史觀交鋒：保住議會民主，抑或過度妥協錯失改革？

=== 獨立簡報驗收：deck_03_china.html ===
  HTML 結構=PASS | 頁數=7 頁（標準 5～8）->PASS | <img>=PASS（1 張） | 跨簡報連結=PASS（10 條）
    Image 01 [PASS] | 第 2 頁 -> assets/03_china_warlords.png
    Link  01 [PASS] | 投影片外區域 -> index.html
    Link  02 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  03 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  04 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  05 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  06 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  07 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html
    Link  08 [PASS] | 第 4 頁 -> deck_01_russia.html#slide-6（第 6/6 頁）
    Link  09 [PASS] | 第 7 頁 -> deck_00_framework.html#slide-5（第 5/6 頁）
    Link  10 [PASS] | 第 7 頁 -> deck_04_spain.html#slide-1（第 1/6 頁）
    Slide 01 [PASS] | 中文字: 116/260 (OK, 可視字元:199) | <footer>來源: OK ([04_warlord_era_china.md, 導言; Aftermath]; [0…) | 標題: 從軍閥割據到敵後土改：1916–1949 中國的裂…
    Slide 02 [PASS] | 中文字: 165/260 (OK, 可視字元:298) | <footer>來源: OK ([04_warlord_era_china.md, 導言; Warlord relati…) | 標題: 1916 年袁世凱死後，北洋三大派系展開殘酷均勢混戰
    Slide 03 [PASS] | 中文字: 223/260 (OK, 可視字元:349) | <footer>來源: OK ([04_warlord_era_china.md, Warlord armies; Ar…) | 標題: 兵災與武器禁運下，無槍農民以會社武裝守衛鄉土
    Slide 04 [PASS] | 中文字: 224/260 (OK, 可視字元:328) | <footer>來源: OK ([04_warlord_era_china.md, Infrastructure; Ar…) | 標題: 1923 年跨國轉折：列寧式改組國民黨與白俄軍火坦…
    Slide 05 [PASS] | 中文字: 211/260 (OK, 可視字元:332) | <footer>來源: OK ([04_warlord_era_china.md, 導言; South; Reunifi…) | 標題: 北伐、寧漢分裂與「整批收編」舊軍閥埋下的統治隱患
    Slide 06 [PASS] | 中文字: 213/260 (OK, 可視字元:293) | <footer>來源: OK ([05_second_united_front.md, Background; Coop…) | 標題: 1936 西安事變促成合作，1941 皖南事變爆發…
    Slide 07 [PASS] | 中文字: 177/260 (OK, 可視字元:219) | <footer>來源: OK ([05_second_united_front.md, Breakdown and af…) | 標題: 敵後貧農土改減稅與 1945 東北日械接收的奪權公式

=== 獨立簡報驗收：deck_04_spain.html ===
  HTML 結構=PASS | 頁數=6 頁（標準 5～8）->PASS | <img>=PASS（1 張） | 跨簡報連結=PASS（13 條）
    Image 01 [PASS] | 第 2 頁 -> assets/04_spain.jpg
    Link  01 [PASS] | 投影片外區域 -> index.html
    Link  02 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  03 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  04 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  05 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  06 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  07 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html
    Link  08 [PASS] | 第 4 頁 -> deck_01_russia.html#slide-3（第 3/6 頁）
    Link  09 [PASS] | 第 4 頁 -> deck_05_yugoslavia.html#slide-3（第 3/6 頁）
    Link  10 [PASS] | 第 5 頁 -> deck_02_germany.html#slide-6（第 6/6 頁）
    Link  11 [PASS] | 第 5 頁 -> deck_00_framework.html#slide-5（第 5/6 頁）
    Link  12 [PASS] | 第 6 頁 -> deck_00_framework.html#slide-3（第 3/6 頁）
    Link  13 [PASS] | 第 6 頁 -> deck_05_yugoslavia.html#slide-1（第 1/6 頁）
    Slide 01 [PASS] | 中文字: 127/260 (OK, 可視字元:211) | <footer>來源: OK ([03_spanish_civil_war.md, 導言; Military coup;…) | 標題: 社會革命與左翼內鬨：1936–1939 西班牙共和…
    Slide 02 [PASS] | 中文字: 174/260 (OK, 可視字元:270) | <footer>來源: OK ([03_spanish_civil_war.md, Military coup; Spa…) | 標題: 1936 年七月軍人政變，工人開倉發槍掀開社會革命
    Slide 03 [PASS] | 中文字: 202/260 (OK, 可視字元:287) | <footer>來源: OK ([03_spanish_civil_war.md, Spanish Revolution…) | 標題: 共和派內部死結：先自治集體化，還是先集中權力贏得戰…
    Slide 04 [PASS] | 中文字: 232/260 (OK, 可視字元:368) | <footer>來源: OK ([03_spanish_civil_war.md, Course of the war;…) | 標題: 1937 五月事件、蘇聯黃金買軍火與 NKVD／契…
    Slide 05 [PASS] | 中文字: 218/260 (OK, 可視字元:313) | <footer>來源: OK ([03_spanish_civil_war.md, Combatants; Foreig…) | 標題: 27 國禁運重傷共和國，德義武力與高壓「清理」助佛…
    Slide 06 [PASS] | 中文字: 237/260 (OK, 可視字元:364) | <footer>來源: OK ([03_spanish_civil_war.md, Death toll; Atroci…) | 標題: 史觀交鋒：共和區暴力是無政府失序，或左翼半組織化執…

=== 獨立簡報驗收：deck_05_yugoslavia.html ===
  HTML 結構=PASS | 頁數=6 頁（標準 5～8）->PASS | <img>=PASS（1 張） | 跨簡報連結=PASS（13 條）
    Image 01 [PASS] | 第 2 頁 -> assets/05_yugoslavia.jpg
    Link  01 [PASS] | 投影片外區域 -> index.html
    Link  02 [PASS] | 投影片外區域 -> deck_00_framework.html
    Link  03 [PASS] | 投影片外區域 -> deck_01_russia.html
    Link  04 [PASS] | 投影片外區域 -> deck_02_germany.html
    Link  05 [PASS] | 投影片外區域 -> deck_03_china.html
    Link  06 [PASS] | 投影片外區域 -> deck_04_spain.html
    Link  07 [PASS] | 投影片外區域 -> deck_05_yugoslavia.html
    Link  08 [PASS] | 第 3 頁 -> deck_04_spain.html#slide-4（第 4/6 頁）
    Link  09 [PASS] | 第 3 頁 -> deck_00_framework.html#slide-4（第 4/6 頁）
    Link  10 [PASS] | 第 5 頁 -> deck_01_russia.html#slide-6（第 6/6 頁）
    Link  11 [PASS] | 第 5 頁 -> deck_00_framework.html#slide-5（第 5/6 頁）
    Link  12 [PASS] | 第 6 頁 -> deck_00_framework.html#slide-5（第 5/6 頁）
    Link  13 [PASS] | 第 6 頁 -> index.html
    Slide 01 [PASS] | 中文字: 141/260 (OK, 可視字元:230) | <footer>來源: OK ([06_yugoslav_partisans.md, 導言; Background an…) | 標題: 跨民族游擊隊的自主崛起：1941–1948 南斯拉…
    Slide 02 [PASS] | 中文字: 190/260 (OK, 可視字元:261) | <footer>來源: OK ([06_yugoslav_partisans.md, Background and or…) | 標題: 1941 年軸心國肢解南斯拉夫，百人質報復與清洗逼…
    Slide 03 [PASS] | 中文字: 237/260 (OK, 可視字元:342) | <footer>來源: OK ([06_yugoslav_partisans.md, Objectives; Backg…) | 標題: 狄托淡化共產口號高喊「兄弟情誼」，西班牙老兵返鄉扛…
    Slide 04 [PASS] | 中文字: 253/260 (OK, 可視字元:376) | <footer>來源: OK ([06_yugoslav_partisans.md, 導言; Operations; S…) | 標題: 全民動員擴軍逾 80 萬並建海空軍 vs. 保皇切…
    Slide 05 [PASS] | 中文字: 239/260 (OK, 可視字元:353) | <footer>來源: OK ([06_yugoslav_partisans.md, 導言; Composition; …) | 標題: 1945 自主光復、戰後大清洗爭議與 1947–1…
    Slide 06 [PASS] | 中文字: 242/260 (OK, 可視字元:271) | <footer>來源: OK ([01_russian_civil_war.md, 導言]; [02_german_re…) | 標題: 全系列收官：五國比較歷史的三個核心洞見

=== 系列驗收總結 ===
結果：PASS（index.html 總入口與全部 6 份獨立簡報皆通過所有驗收條件）
```

---

## 六、演進紀錄與合規稽核

- **舊版 `v1`（單一 12 頁簡報，見 [deck.html](deck.html) 歷史存檔）**：曾以 12 頁、每頁 310～380 字全文字卡片形式通過早期單檔驗收；後因跨國時間軸跳躍不利初學者消化，依策展重構決定退回並重建為現今「1 總入口 ＋ 6 份獨立國家簡報（37 頁）」之圖文策展架構。
- **硬性規範稽核**：全程未改動 `raw/` 任何原始資料；繁體中文搭配專有名詞首次原文附註；每頁皆附 `[來源檔名, 段落標題]`；對照史家爭議且明確揭示缺漏。
