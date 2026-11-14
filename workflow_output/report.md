# 教學簡報審查與自動化驗收報告（`report.md`）

## 一、執行摘要

- **教學主題**：戰火下的路線分歧：1914–1945 歐亞社會主義流派與地方勢力的崛起比較
- **目標受眾**：沒有歷史背景的初學者
- **最終總頁數**：**12 頁**（`<section class="slide">` 共 12 張，符合 10～14 頁規範）
- **覆蓋地理區域（5 區 >= 3）**：俄國（含前帝國邊疆與中亞）、德國、西班牙、中國、南斯拉夫
- **引用原始來源（6 篇 >= 4）**：
  1. `01_russian_civil_war.md`
  2. `02_german_revolution_1918_1919.md`
  3. `03_spanish_civil_war.md`
  4. `04_warlord_era_china.md`
  5. `05_second_united_front.md`
  6. `06_yugoslav_partisans.md`
- **交付成果檔案**：
  - 展示入口：[index.html](../index.html)
  - 工作流備份：[deck.html](deck.html)（經雜湊比對兩檔完全一致）
  - 上游產物：[sources.md](sources.md)、[cards.md](cards.md)、[outline.md](outline.md)、[drafts.md](drafts.md)
- **最終驗收狀態**：**PASS（Exit Code 0）**——第 2 輪 `python scripts/verify_slides.py` 四項硬性指標及全部 12 頁投影片皆通過；`raw/` 保持唯讀零異動。

---

## 二、Node 1～3 檢索與人工確認摘記

1. **Node 1（檢索與檢查關卡 1）**：於 [sources.md](sources.md) 精選 52 篇 `wiki/` 頁面（`syntheses/` 2 頁、`ideologies/` 14 頁、`factions/` 22 頁、`events/` 14 頁），涵蓋 5 個地理區域與全部 6 篇 `raw/` 原始來源，通過檢查關卡 1（`5 >= 3`、`6 >= 4`），並預先彙整 6 項資料邊界。
2. **Node 2（證據卡萃取）**：於 [cards.md](cards.md) 萃取 28 張原子化證據卡（`CARD-01`～`CARD-28`），全數雙重綁定 `[wiki/分類/檔名.md]` 與 `[來源檔名, 段落標題]`，並列所有史觀衝突與 `[資料不足／不確定：...]` 缺口。
3. **Node 3（初學者大綱與人工確認關卡）**：設計 12 頁教學大綱（[outline.md](outline.md)）後立即暫停。使用者於 **2026-11-14** 明確認可通過 12 頁大綱，並特別提示：**第 8 頁與第 11 頁涵蓋案例較多，須為初學者將專有名詞轉化為白話短句，並嚴控單頁純文字在 380 字以內**。

---

## 三、Node 4 逐頁 AI 忠實度審查結果表（檢查關卡 2）

逐頁核對 [drafts.md](drafts.md) 與 [cards.md](cards.md)：確認零外部腦補、年份／數據／專有名詞原文附註精確、史觀衝突雙邊並列、資料空白處採 `[資料不足／不確定：...]` 誠實標記，且每頁底部皆綁定明確來源標記。

| 頁碼 | 投影片標題 | 綁定卡片 | 審查輪次與局部調整歷程 | 忠實度與字數狀態 |
| :--- | :--- | :--- | :--- | :--- |
| **Slide 01** | 戰火下的路線分歧（1914–1945） | `CARD-01`～`03` | 第 1 輪一次通過（五年份、五舞台、雙主軸與 6 篇導言吻合）。 | **PASS**（未觸發退回） |
| **Slide 02** | 舊秩序垮台：誰填補權力真空？ | `CARD-01`, `02` | 第 1 輪將 1916 中國補充 `(Yuan Shikai)` 首次原文附註後通過。 | **PASS**（1 輪微調即定稿） |
| **Slide 03** | 左翼光譜：為何分成四派？ | `CARD-03` | 第 1 輪一次通過（四大派別對比精簡清晰）。 | **PASS**（未觸發退回） |
| **Slide 04** | 俄國：蘇維埃如何變成一黨專政？ | `CARD-04`～`06` | Node 4 第 2 輪補全 `(Vladimir Lenin)` 與 `(New Economic Policy, NEP)`；Node 5 第 1 輪因頁底細目過長超字，退回 Node 4 收斂為 `[01_russian_civil_war.md, 導言; Background; Warfare]`。 | **PASS**（精準收斂來源層級） |
| **Slide 05** | 德國：工兵委員會為何主動交權？ | `CARD-01`, `08`～`10` | Node 4 第 2 輪補全 `(Karl Liebknecht)`、`(Rosa Luxemburg)`、`(Ruhr Red Army)`，維持 `8 小時`、`344 對 98 票`、`1918–1920` 史實無誤。 | **PASS**（剛好 380/380 通過） |
| **Slide 06** | 中國：軍閥割據、民間會社與黨軍移植 | `CARD-12`～`14` | Node 4 第 2 輪補齊 `(Yan Xishan)`、`(Feng Yuxiang)`、`(Red Spear Society)` 原文附註。 | **PASS**（未觸發 Node 5 退回） |
| **Slide 07** | 西班牙內戰：社會革命與左翼內鬨（1936–1939） | `CARD-17`～`19` | 第 1 輪一次通過（革命派／贏戰派／27 國禁運／三位數通膨／德義援佛朗哥均吻合）。 | **PASS**（未觸發退回） |
| **Slide 08** | 二戰敵後：中共與南國游擊隊崛起 | `CARD-15`, `16`, `21`～`23` | 第 1 輪即依使用者提醒拆成「中共統戰／中共土改／南國起義／南國擴軍」4 張白話短卡（370 字，安全過關）。 | **PASS**（一次通過） |
| **Slide 09** | 歐亞跨區流動網 | `CARD-14`～`16`, `24`～`26` | Node 4 第 2 輪修正白俄赴西為 `150–170 名`、蘇南分裂為 `1947–1948 年`；Node 5 第 1 輪超字後退回精簡引導句並以 `[04_warlord_era_china.md, Armaments]`、`[01_russian_civil_war.md, Background; Aftermath]` 統整對應節次。 | **PASS**（退回精簡 69 字） |
| **Slide 10** | 結局分岔與後方治理 | `CARD-19`, `22`, `24`, `27` | Node 4 第 2 輪將塞德曼對俄白軍／國府評語還原為「未壓制叛亂、縱容貪腐」；Node 5 第 1 輪達 456 字超字後，退回簡化結語與 `[05_second_united_front.md, After 1945]` 等精簡章節名，降為 370 字。 | **PASS**（退回精簡 86 字） |
| **Slide 11** | 史觀交鋒與研究邊界 | `CARD-07`, `11`, `16`, `20`, `24`, `28` | Node 4 第 2 輪將 `5–200 萬` 明確寫為 `5 萬至 200 萬`、改「八路軍編制」為符合 `CARD-28` 的「八路軍人數」；Node 5 第 1 輪僅多 6 字（386/380），退回刪減 14 字冗詞後降為 372 字。 | **PASS**（退回精簡 14 字） |
| **Slide 12** | 總結：帶走三個提問 | `CARD-03`, `25`～`28` | 第 1 輪一次通過（涵蓋三大思辨提問與全 6 篇核心來源）。 | **PASS**（未觸發退回） |

---

## 四、Node 5 每一輪自動化腳本驗收數據與修正紀錄（檢查關卡 3）

### 第 1 輪執行：`python scripts/verify_slides.py`（未通過，Exit Code 1）

- **檢查發現**：HTML 結構（`<!DOCTYPE html>`、`<html>`、`</html>`、無 `<img>`）與總頁數（12 頁）皆 **PASS**，每頁均含明確資料來源標註；唯 **Slide 04、09、10、11** 因包含多國來源路徑或卡片副標使純文字超過 380 字上限。
- **第 1 輪逐頁實測明細**：
  - Slide 01：`359/380` (PASS)｜Slide 02：`370/380` (PASS)｜Slide 03：`351/380` (PASS)
  - Slide 04：**`420/380` (OVER，+40 字)**
  - Slide 05：`380/380` (PASS)｜Slide 06：`357/380` (PASS)｜Slide 07：`349/380` (PASS)｜Slide 08：`370/380` (PASS)
  - Slide 09：**`441/380` (OVER，+61 字)**
  - Slide 10：**`456/380` (OVER，+76 字)**
  - Slide 11：**`386/380` (OVER，+6 字)**
  - Slide 12：`364/380` (PASS)

```text
=== 教學簡報自動化驗收報告 ===
檢查目標：index.html
[條件 4] HTML 結構檢查：<!DOCTYPE html>=PASS, <html>=PASS, </html>=PASS, 無 <img>=PASS
[條件 1] 投影片總頁數（<section class="slide">）：12 頁（標準：10～14 頁）-> PASS

--- 逐頁檢查明細（條件 2：資料來源標註｜條件 3：純文字字數 <= 380）---
  Slide 01 [PASS] | 字數: 359/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言]; [02_german_revolution_1…) | 標題: 戰火下的路線分歧（1914–1945）
  Slide 02 [PASS] | 字數: 370/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, Background]; [02_german_revo…) | 標題: 舊秩序垮台：誰填補權力真空？
  Slide 03 [PASS] | 字數: 351/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言; Background]; [02_german_…) | 標題: 左翼光譜：為何分成四派？
  Slide 04 [FAIL] | 字數: 420/380 (OVER) | 來源標註: OK ([01_russian_civil_war.md, 導言; Formation of the Red Arm…) | 標題: 俄國：蘇維埃如何變成一黨專政？
  Slide 05 [PASS] | 字數: 380/380 (OK) | 來源標註: OK ([02_german_revolution_1918_1919.md, Impact of the Russ…) | 標題: 德國：工兵委員會為何主動交權？
  Slide 06 [PASS] | 字數: 357/380 (OK) | 來源標註: OK ([04_warlord_era_china.md, 導言; Warlord relations; Warlo…) | 標題: 中國：軍閥割據、民間會社與黨軍移植
  Slide 07 [PASS] | 字數: 349/380 (OK) | 來源標註: OK ([03_spanish_civil_war.md, 導言; Spanish Revolution; Comb…) | 標題: 西班牙內戰：社會革命與左翼內鬨（1936–1939）
  Slide 08 [PASS] | 字數: 370/380 (OK) | 來源標註: OK ([05_second_united_front.md, Background; Cooperation du…) | 標題: 二戰敵後：中共與南國游擊隊崛起
  Slide 09 [FAIL] | 字數: 441/380 (OVER) | 來源標註: OK ([01_russian_civil_war.md, Evacuations; Repression]; [0…) | 標題: 歐亞跨區流動網
  Slide 10 [FAIL] | 字數: 456/380 (OVER) | 來源標註: OK ([01_russian_civil_war.md, 導言; Aftermath]; [02_german_r…) | 標題: 結局分岔與後方治理對比
  Slide 11 [FAIL] | 字數: 386/380 (OVER) | 來源標註: OK ([01_russian_civil_war.md, Background; Aftermath]; [02_…) | 標題: 史觀交鋒與研究邊界
  Slide 12 [PASS] | 字數: 364/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言]; [02_german_revolution_1…) | 標題: 總結：帶走三個提問

=== 總結 ===
結果：FAIL（共 4 項未通過）
  1. 第 4 頁（俄國：蘇維埃如何變成一黨專政？）扣除 HTML 標籤後純文字為 420 字，超過上限 380 字。
  2. 第 9 頁（歐亞跨區流動網）扣除 HTML 標籤後純文字為 441 字，超過上限 380 字。
  3. 第 10 頁（結局分岔與後方治理對比）扣除 HTML 標籤後純文字為 456 字，超過上限 380 字。
  4. 第 11 頁（史觀交鋒與研究邊界）扣除 HTML 標籤後純文字為 386 字，超過上限 380 字。
```

### 第 1 輪 → 第 2 輪局部退回與修正動作

僅針對未通過之第 4、9、10、11 頁進行局部精簡（保持其餘 8 頁不變），同步更新 [drafts.md](drafts.md)、[index.html](../index.html) 與 [deck.html](deck.html)：
1. **Slide 04**：不更動教學短句與原文附註，將頁底冗長子節清單收斂為所屬實際 H2 大節 `[01_russian_civil_war.md, 導言; Background; Warfare]`（由 420 字降至 **310 字**）。
2. **Slide 09**：精簡導言與流動卡措辭、移除重複之 `(戰上海)`／`(Franco)` 附註及項目數字前綴，並以 `[01_russian_civil_war.md, Background; Aftermath]` 與 `[04_warlord_era_china.md, Armaments]` 精確涵蓋白俄、FT-17 坦克與契卡來源（由 441 字降至 **372 字**）。
3. **Slide 10**：濃縮頁面標題、核心結論與三項條列短句，並調整為 `[01_russian_civil_war.md, 導言]`、`[02_german_revolution_1918_1919.md, 導言]` 與 `[05_second_united_front.md, After 1945]`（由 456 字降至 **370 字**）。
4. **Slide 11**：精簡導言及各國短句贅字（保留全部四組史觀對立與 `[資料不足／不確定：未載德無政府派、中共蘇區與八路軍人數]` 原樣提示），由 386 字降至 **372 字**。

### 第 2 輪複驗：`python scripts/verify_slides.py`（全數通過，Exit Code 0）

對根目錄 `index.html` 與備份 `workflow_output/deck.html` 分別執行驗收，均回傳 **Exit Code 0（PASS）**，且經檔案雜湊比對兩份 HTML 完全一致（`True`）：

```text
=== 教學簡報自動化驗收報告 ===
檢查目標：index.html
[條件 4] HTML 結構檢查：<!DOCTYPE html>=PASS, <html>=PASS, </html>=PASS, 無 <img>=PASS
[條件 1] 投影片總頁數（<section class="slide">）：12 頁（標準：10～14 頁）-> PASS

--- 逐頁檢查明細（條件 2：資料來源標註｜條件 3：純文字字數 <= 380）---
  Slide 01 [PASS] | 字數: 359/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言]; [02_german_revolution_1…) | 標題: 戰火下的路線分歧（1914–1945）
  Slide 02 [PASS] | 字數: 370/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, Background]; [02_german_revo…) | 標題: 舊秩序垮台：誰填補權力真空？
  Slide 03 [PASS] | 字數: 351/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言; Background]; [02_german_…) | 標題: 左翼光譜：為何分成四派？
  Slide 04 [PASS] | 字數: 310/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言; Background; Warfare]) | 標題: 俄國：蘇維埃如何變成一黨專政？
  Slide 05 [PASS] | 字數: 380/380 (OK) | 來源標註: OK ([02_german_revolution_1918_1919.md, Impact of the Russ…) | 標題: 德國：工兵委員會為何主動交權？
  Slide 06 [PASS] | 字數: 357/380 (OK) | 來源標註: OK ([04_warlord_era_china.md, 導言; Warlord relations; Warlo…) | 標題: 中國：軍閥割據、民間會社與黨軍移植
  Slide 07 [PASS] | 字數: 349/380 (OK) | 來源標註: OK ([03_spanish_civil_war.md, 導言; Spanish Revolution; Comb…) | 標題: 西班牙內戰：社會革命與左翼內鬨（1936–1939）
  Slide 08 [PASS] | 字數: 370/380 (OK) | 來源標註: OK ([05_second_united_front.md, Background; Cooperation du…) | 標題: 二戰敵後：中共與南國游擊隊崛起
  Slide 09 [PASS] | 字數: 372/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, Background; Aftermath]; [03_…) | 標題: 歐亞跨區流動網
  Slide 10 [PASS] | 字數: 370/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言]; [02_german_revolution_1…) | 標題: 結局分岔與後方治理
  Slide 11 [PASS] | 字數: 372/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, Background; Aftermath]; [02_…) | 標題: 史觀交鋒與研究邊界
  Slide 12 [PASS] | 字數: 364/380 (OK) | 來源標註: OK ([01_russian_civil_war.md, 導言]; [02_german_revolution_1…) | 標題: 總結：帶走三個提問

=== 總結 ===
結果：PASS（全部 4 項驗收條件及 12 頁投影片皆通過）
```

> 附註：`python scripts/verify_slides.py workflow_output/deck.html` 亦回傳相同逐頁字數（310～380 字）與 `結果：PASS`（Exit Code 0）。

---

## 五、最終交付查核結論

- **離線互動與視覺規格**：全檔內嵌 CSS 與 Vanilla JS，零外部相依且無 `<img>` 標籤；支援 `←`／`→`／`PageUp`／`PageDown`／`Space`／`Home`／`End` 鍵盤切換、畫面按鈕、跳頁頁碼方塊與頂部進度條。
- **硬性規則稽核**：100% 溯源標註、零外部知識、誠實不知標註保留、史觀衝突雙邊並列，且 `raw/` 檔案全程未改動。
