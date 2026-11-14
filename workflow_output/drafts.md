# Node 4 逐頁教學講稿（`drafts.md`）

- **對應大綱**：[outline.md](outline.md)（15 頁順時序故事線，面向無歷史背景初學者）
- **證據來源**：[cards.md](cards.md)（`CARD-01`～`CARD-28`）與 [assets/credits.md](../assets/credits.md)
- **核心主軸（One Big Idea）**：兩次大戰打破舊帝國後，左翼與地方武裝陷入「基層自治」與「集權贏戰」的兩難；最終唯有同時掌握「農村土改、跨群體統戰與後方治安」的勢力，才能從地方游擊蛻變為全國政權。
- **編寫與驗收控管原則**：
  - 每頁標題為「一句完整白話論點」，內文採完整自然短句（拒絕電報式縮寫），每頁聚焦單一重點並附「承上啟下過渡句」。
  - 正文（含標題、敘事、圖說、過渡句，排除頁底 `來源：` 行）嚴控於 **230 個中文字以內**，並為內嵌 `<svg>` 標籤預留充足字元餘裕，確保後續渲染後遠低於 `scripts/verify_slides.py` 之 **280 字**上限。
  - 每頁末尾保留簡潔 H2 格式之 `<footer>` 出處標註。

---

## Slide 01：大戰打碎了舊帝國，誰能從亂世草莽蛻變為全國政權？

- **綁定卡片**：`CARD-01`, `CARD-02`, `CARD-03`, `CARD-27`
- **視覺與版面配置**：獨立深色全版面封面 ＋ 內嵌極簡歐亞五區時間軸 `<svg>`（正文不放來源清單與密集卡片；底緣保留簡潔 `<footer>` 來源標註）。
- **簡報內文**：
  - **標題**：大戰打碎了舊帝國，誰能從亂世草莽蛻變為全國政權？
  - **白話副標題（點出核心問題）**：1914 至 1945 年，追求改變的左翼與地方武裝陷入「基層自治」與「集權贏戰」的兩難；唯有兼顧農村土改、跨群體統戰與後方治安的勢力，才走到最後。
  - **承上啟下過渡句**：這段歐亞交織的三十年，就從五大戰場的起點看起。
  - **SVG 建議標籤（39 字元）**：`1917 俄國` / `1918 德國` / `1916–28 中國` / `1936 西班牙` / `1941–45 中南敵後`
- **來源**：`[01_russian_civil_war.md, 導言]; [02_german_revolution_1918_1919.md, 導言]; [03_spanish_civil_war.md, 導言]; [04_warlord_era_china.md, 導言]; [05_second_united_front.md, 導言]; [06_yugoslav_partisans.md, 導言]`
- **字數預估**：中文字 97 字｜正文可視字元 118 字（加 SVG 約 157 字，遠低於 280 字）

---

## Slide 02：兩次大戰壓垮舊中央，同時在歐亞五大戰場留下權力真空。

- **綁定卡片**：`CARD-01`, `CARD-02`
- **視覺與版面配置**：米白紙色 `#F7F4EB` 全局地圖導覽 ＋ 內嵌 `<svg>` 歐亞五大戰區戰略地圖。
- **簡報內文**：
  - **標題**：兩次大戰壓垮舊中央，同時在歐亞五大戰場留下權力真空。
  - **正文**：戰火先後摧毀沙俄、德意志帝國與袁世凱（Yuan Shikai）死後的中國中央秩序，並在 1936 年西班牙政變與 1941 年軸心國（Axis powers）瓜分南斯拉夫時重演。每當舊政府癱瘓，城鄉基層議會與地方武裝便就地崛起。
  - **承上啟下過渡句**：然而，同樣想趁亂重塑社會的左翼陣營，為何自己卻先分裂？
  - **SVG 建議標籤（33 字元）**：`1936 西班牙` / `1918 德國` / `1941 南斯拉夫` / `1917 俄國` / `1916 中國`
- **來源**：`[01_russian_civil_war.md, Background]; [02_german_revolution_1918_1919.md, 導言]; [03_spanish_civil_war.md, Military coup]; [04_warlord_era_china.md, 導言]; [06_yugoslav_partisans.md, Background and origins]`
- **字數預估**：中文字 119 字｜正文可視字元 161 字（加 SVG 約 194 字）

---

## Slide 03：同喊社會主義，四條奪權路線的根本衝突讓左翼經常互打。

- **綁定卡片**：`CARD-03`
- **視覺與版面配置**：概念預備象限頁 ＋ 內嵌 `<svg>` 左翼四派光譜定位圖。
- **簡報內文**：
  - **標題**：同喊社會主義，四條奪權路線的根本衝突讓左翼經常互打。
  - **正文**：一黨集權派如布爾什維克（Bolsheviks）主張先鋒黨專政；議會改良派如德國社民黨（SPD）堅持選票與憲政。無政府與極左派追求廢除國家、當下自治；抗戰游擊派則選擇先聯合各階層抗敵、再紮根農村。
  - **承上啟下過渡句**：這場牽動五國的路線實驗，就從 1917 年俄國揭開序幕。
  - **SVG 建議標籤（22 字元）**：`一黨集權` / `議會改良` / `無政府自治` / `抗戰游擊` / `分散 ↔ 集權`
- **來源**：`[01_russian_civil_war.md, 導言]; [02_german_revolution_1918_1919.md, Background events]; [03_spanish_civil_war.md, Spanish Revolution; Combatants]; [05_second_united_front.md, Cooperation during the Second Sino-Japanese War]; [06_yugoslav_partisans.md, Objectives]`
- **字數預估**：中文字 118 字｜正文可視字元 149 字（加 SVG 約 171 字）

---

## Slide 04：俄國蘇維埃原是民選議會，卻在敗選解散國會後走向一黨制。

- **綁定卡片**：`CARD-01`, `CARD-04`
- **視覺與版面配置**：文圖左右雙欄歷史雜誌版面 ＋ 本機圖片 `assets/01_russia.jpg`。
- **簡報內文**：
  - **標題**：俄國蘇維埃原是民選議會，卻在敗選解散國會後走向一黨制。
  - **正文**：1917 年二月革命（February Revolution）推翻沙皇後，臨時政府與工農兵「蘇維埃」（soviets）形成雙重政權。列寧（Vladimir Lenin）領導布爾什維克奪權後，因在全俄立憲會議（Russian Constituent Assembly）敗給右翼社會革命黨（Right SRs），於 1918 年 1 月強行解散議會並陸續逐出反對派。
  - **圖說**：1917 年東線與前沙俄西部疆界變動圖。
  - **承上啟下過渡句**：此舉雖保住核心權力，卻也將俄國推入四方內戰火海。
- **來源**：`[01_russian_civil_war.md, Background; Warfare]`
- **字數預估**：中文字 134 字｜正文可視字元 241 字（無 SVG，安全低於 280 字）

---

## Slide 05：列寧靠強徵與 83% 舊軍官打贏內戰，代價是鎖死黨內民主。

- **綁定卡片**：`CARD-05`, `CARD-06`
- **視覺與版面配置**：戰場態勢示意頁 ＋ 內嵌 `<svg>` 紅、白、黑、綠四方角力圖。
- **簡報內文**：
  - **標題**：列寧靠強徵與 83% 舊軍官打贏內戰，代價是鎖死黨內民主。
  - **正文**：托洛茨基（Leon Trotsky）憑強制徵兵、督戰隊（barrier troops）與 83% 前沙俄高階軍官組紅軍（Red Army），擊敗白軍（White Army）、綠軍（Green Armies）與馬赫諾（Nestor Makhno）黑軍。工業跌至 1913 年 20% 後，列寧鎮壓喀琅施塔得（Kronstadt）起義並頒派系禁令、推新經濟政策（New Economic Policy, NEP）。
  - **承上啟下過渡句**：這場血腥代價，隨即動搖德國左翼的抉擇。
  - **SVG 建議標籤（22 字元）**：`紅軍 83% 舊軍官` / `保守白軍` / `黑軍先盟後剿` / `農民綠軍`
- **來源**：`[01_russian_civil_war.md, 導言; Background; Warfare; Aftermath]`
- **字數預估**：中文字 103 字｜正文可視字元 236 字（加 SVG 約 258 字）

---

## Slide 06：德國社民黨懼怕俄式內戰，寧願聯手舊軍方鎮壓極左保住議會。

- **綁定卡片**：`CARD-01`, `CARD-08`, `CARD-09`, `CARD-10`, `CARD-11`
- **視覺與版面配置**：左圖右文檔案紀事版面 ＋ 本機圖片 `assets/02_germany.jpg`。
- **簡報內文**：
  - **標題**：德國社民黨懼怕俄式內戰，寧願聯手舊軍方鎮壓極左保住議會。
  - **正文**：1918 年基爾（Kiel）起義推翻帝制後，工兵委員會以 344 票對 98 票交權給國民議會。艾伯特（Friedrich Ebert）密約保留舊軍官並安撫資方；面對斯巴達克起義（Spartacist uprising），政府動用自由軍團（Freikorps）殺害李卜克內西（Karl Liebknecht）與盧森堡（Rosa Luxemburg），埋下威瑪隱患。
  - **圖說**：1918–1919 柏林十一月革命街頭路障。
  - **承上啟下過渡句**：同時期的東亞，中國正陷入無主的軍閥混戰。
- **來源**：`[02_german_revolution_1918_1919.md, 導言; Background events; Revolution, first stage: fall of the Empire; Revolution, second stage: defeat of the radical Left]`
- **字數預估**：中文字 129 字｜正文可視字元 242 字（無 SVG，安全低於 280 字）

---

## Slide 07：失去強中央的中國陷入軍閥混戰，農民只得靠秘密會社武裝自保。

- **綁定卡片**：`CARD-02`, `CARD-12`, `CARD-13`
- **視覺與版面配置**：形勢圖文雙欄版面 ＋ 本機圖片 `assets/03_china_warlords.png`。
- **簡報內文**：
  - **標題**：失去強中央的中國陷入軍閥混戰，農民只得靠秘密會社武裝自保。
  - **正文**：1916 年北洋軍（Beiyang Army）分裂爭奪北京與海關財源，列強更無視 1919 年禁運走私軍火。閻錫山（Yan Xishan）融合十派主義、馮玉祥（Feng Yuxiang）左傾卻收鴉片稅；多數兵災則逼出農村紅槍會（Red Spear Society）與全女性鐵門會（Iron Gate Society）自衛。
  - **圖說**：1925 年中國主要軍閥派系割據形勢圖。
  - **承上啟下過渡句**：看清軍閥不可靠後，孫中山決定引進俄國組織技術。
- **來源**：`[04_warlord_era_china.md, 導言; Warlord relations; Warlord profiles; Armaments; Other forces]`
- **字數預估**：中文字 129 字｜正文可視字元 222 字（無 SVG，安全低於 280 字）

---

## Slide 08：孫中山引進列寧式組織改組國民黨，北伐卻因收編軍閥埋下病根。

- **綁定卡片**：`CARD-14`
- **視覺與版面配置**：水平組織演變流程長廊頁 ＋ 內嵌 `<svg>` 組織演變流程圖。
- **簡報內文**：
  - **標題**：孫中山引進列寧式組織改組國民黨，北伐卻因收編軍閥埋下病根。
  - **正文**：受制軍閥的孫中山（Sun Yat-sen），1923 年藉蘇援依民主集中制（democratic centralism）改組國民黨（KMT），建黃埔軍校（Whampoa Military Academy）與國民革命軍（NRA）並聯手中共（CCP）。蔣介石（Chiang Kai-shek）雖藉北伐（Northern Expedition）掌權，卻整批收編舊軍閥埋下腐敗隱患。
  - **承上啟下過渡句**：八年後，歐洲西南角的西班牙也捲入左翼內鬨。
  - **SVG 建議標籤（35 字元）**：`1917 護法受制` → `1923 改組建軍` → `1926 北伐清黨` → `1928 收編軍閥`
- **來源**：`[04_warlord_era_china.md, 導言; South; Reunification; Aftermath]`
- **字數預估**：中文字 108 字｜正文可視字元 230 字（加 SVG 約 265 字）

---

## Slide 09：西班牙左翼困在「先革命或先贏戰」，街頭內鬨把共和國推向敗亡。

- **綁定卡片**：`CARD-17`, `CARD-18`, `CARD-19`
- **視覺與版面配置**：紀實影像跨欄雜誌版面 ＋ 本機圖片 `assets/04_spain.jpg`。
- **簡報內文**：
  - **標題**：西班牙左翼困在「先革命或先贏戰」，街頭內鬨把共和國推向敗亡。
  - **正文**：1936 年政變後，無政府工團聯盟（CNT-FAI）與馬克思主義統一工人黨（POUM）推動集體化，西班牙共產黨（PCE）則憑蘇聯「X 行動」（Operation X）主張護產贏戰。兩派於 1937 年五月事件（May Days）街頭互打，加上 27 國禁運引爆通膨，終敗給德義相助的佛朗哥（Francisco Franco）。
  - **圖說**：1936 年西班牙共和派女民兵訓練實景。
  - **承上啟下過渡句**：這場城市內耗的敗局，正反襯出敵後游擊隊的出路。
- **來源**：`[03_spanish_civil_war.md, 導言; Spanish Revolution; Combatants; Foreign involvement; Course of the war; Financing]`
- **字數預估**：中文字 138 字｜正文可視字元 226 字（無 SVG，安全低於 280 字）

---

## Slide 10：二次合作破裂後，中共轉向貧農土改減稅，把敵後變成擴張基地。

- **綁定卡片**：`CARD-15`, `CARD-16`
- **視覺與版面配置**：雙軌結構演變對比頁 ＋ 內嵌 `<svg>` 敵後根據地擴張對比圖（依資料邊界不虛構未載年度兵力數字）。
- **簡報內文**：
  - **標題**：二次合作破裂後，中共轉向貧農土改減稅，把敵後變成擴張基地。
  - **正文**：1936 年西安事變（Xi'an Incident）促成國共停火並編組八路軍（Eighth Route Army）與新四軍（New Fourth Army），毛澤東（Mao Zedong）則堅持獨立自主與「以空間換時間」。1941 年皖南事變（New Fourth Army Incident）後，中共在敵後推動貧農土改減稅，對比國府貪腐，終藉東北日械於 1949 年建國。
  - **承上啟下過渡句**：同期的巴爾幹，另一支游擊隊正面臨殘酷存亡戰。
  - **SVG 建議標籤（30 字元）**：`1936 西安事變合作` / `1941 皖南破裂` / `貧農土改減稅` / `1949 建國`
- **來源**：`[05_second_united_front.md, 導言; Background; Cooperation during the Second Sino-Japanese War; Breakdown and aftermath]`
- **字數預估**：中文字 119 字｜正文可視字元 225 字（加 SVG 約 255 字）

---

## Slide 11：南斯拉夫游擊隊淡化共產口號並團結各族，自主打下八十萬大軍。

- **綁定卡片**：`CARD-21`, `CARD-22`, `CARD-23`, `CARD-24`
- **視覺與版面配置**：右圖左文紀念焦點頁 ＋ 本機圖片 `assets/05_yugoslavia.jpg`。
- **簡報內文**：
  - **標題**：南斯拉夫游擊隊淡化共產口號並團結各族，自主打下八十萬大軍。
  - **正文**：1941 年軸心國瓜分南斯拉夫後，德軍殺百名平民報復，烏斯塔沙（Ustaše）亦展開清洗；切特尼克（Chetniks）畏戰通敵並屠殺非塞族，1943 年遭盟軍放棄。南共（KPJ）狄托（Josip Broz Tito）淡化共產口號，以「兄弟情誼與團結」（brotherhood and unity）凝聚各族與十萬女戰士，建成 80 萬大軍自主建國。
  - **圖說**：南斯拉夫反法西斯游擊隊紀念雕塑。
  - **承上啟下過渡句**：其實，五國戰場還連著一條跨洲流動網。
- **來源**：`[06_yugoslav_partisans.md, 導言; Objectives; Background and origins; Operations; Services; Composition; Women; Post-war]`
- **字數預估**：中文字 144 字｜正文可視字元 228 字（無 SVG，安全低於 280 字）

---

## Slide 12：從海參崴坦克到西班牙老兵，一條歐亞流動網改寫了五國戰局。

- **綁定卡片**：`CARD-25`, `CARD-26`
- **視覺與版面配置**：跨洲路徑圖解頁 ＋ 內嵌 `<svg>` 歐亞跨國流動路徑圖。
- **簡報內文**：
  - **標題**：從海參崴坦克到西班牙老兵，一條歐亞流動網改寫了五國戰局。
  - **正文**：100 至 200 萬白俄流亡者（White émigrés）跨洲流動：海參崴法製 FT-17（Renault FT-17）坦克與白軍軍火歸張作霖（Zhang Zuolin），白俄兵團在上海阻擊北伐，更有 150 至 170 名赴西助戰。左翼亦然：俄國契卡（Cheka）之名外溢西班牙，國際縱隊（International Brigades）逾千南國老兵返國成為游擊骨幹。
  - **承上啟下過渡句**：結合跨國流動與各國結局，成敗規律隨之浮現。
  - **SVG 建議標籤（35 字元）**：`海參崴 FT-17` / `東北・上海白俄` / `西班牙 150–170 白俄` / `千名南國老兵返國`
- **來源**：`[01_russian_civil_war.md, 導言; Aftermath]; [03_spanish_civil_war.md, Foreign involvement; Atrocities]; [04_warlord_era_china.md, Armaments; Other forces]; [06_yugoslav_partisans.md, Operations; Composition]`
- **字數預估**：中文字 124 字｜正文可視字元 223 字（加 SVG 約 258 字）

---

## Slide 13：地方勢力能否走完奪權最後一哩，取決於土改、統戰與後方治安。

- **綁定卡片**：`CARD-27`
- **視覺與版面配置**：四象限矩陣分析頁 ＋ 內嵌 `<svg>` 成敗分岔矩陣。
- **簡報內文**：
  - **標題**：地方勢力能否走完奪權最後一哩，取決於土改、統戰與後方治安。
  - **正文**：缺乏穩固基層與後勤的武裝多半瓦解：俄國黑軍綠軍遭剿、德國委員會交權、西班牙共和派敗亡，中國舊軍閥則成被收編的包袱。塞德曼（Michael Seidman）指出，西班牙國民軍靠控糧鎮壓杜絕游擊，俄白軍與國府縱容匪患貪腐盡失民心；唯有掌握土改減稅、跨族統戰與自主軍力的中共與南國游擊隊，成功蛻變為全國政權。
  - **承上啟下過渡句**：然而對同一段歷史，史家評價卻截然相反。
  - **SVG 建議標籤（31 字元）**：`基層土改統戰` / `後方治安管控` / `覆滅・整編` / `獨立・掌權（芬／波／中／南）`
- **來源**：`[01_russian_civil_war.md, 導言; Aftermath]; [02_german_revolution_1918_1919.md, Revolution, second stage: defeat of the radical Left]; [03_spanish_civil_war.md, Atrocities]; [04_warlord_era_china.md, Aftermath]; [05_second_united_front.md, Breakdown and aftermath]; [06_yugoslav_partisans.md, Post-war]`
- **字數預估**：中文字 166 字｜正文可視字元 198 字（加 SVG 約 229 字）

---

## Slide 14：鎮壓是防衛還是背叛？史家觀點對立，史料也留有明確空白。

- **綁定卡片**：`CARD-07`, `CARD-11`, `CARD-16`, `CARD-20`, `CARD-24`, `CARD-28`
- **視覺與版面配置**：報紙雙欄細線對照版面（左欄「觀點 A：防衛與失序論」vs. 右欄「觀點 B：專政與清洗論」，底部附細線研究邊界警示欄；無圖片、無重複色條卡片）。
- **簡報內文**：
  - **標題**：鎮壓是防衛還是背叛？史家觀點對立，史料也留有明確空白。
  - **左欄（觀點 A：防衛與失序）**：利布曼（Marcel Liebman）視俄禁黨為戰時防衛；護憲派認德社民黨阻內戰；失序論指西國處決源於崩潰；南國老兵捍衛抗敵記憶。
  - **右欄（觀點 B：專政與清洗）**：張伯倫（William Henry Chamberlin）批俄專政（紅恐估 5 至 200 萬）；修正派批德妥協過頭；佩恩（Stanley Payne）指西國屬組織清洗；皖南互控先開火，南國 8 至 10 萬清洗引發修正主義。
  - **研究邊界**：`[資料不足／不確定：未載中共蘇區、1923 後德左翼、八路軍兵力與非蘇聯跨國交流。]`
  - **承上啟下過渡句**：帶著對證據邊界的清醒，我們收束全場。
- **來源**：`[01_russian_civil_war.md, Background; Aftermath]; [02_german_revolution_1918_1919.md, Contemporary statements]; [03_spanish_civil_war.md, Atrocities]; [05_second_united_front.md, Breakdown and aftermath]; [06_yugoslav_partisans.md, Post-war; Partisan legacy]`
- **字數預估**：中文字 179 字｜正文可視字元 272 字（含雙欄小標、無 SVG，低於 280 字）

---

## Slide 15：面對戰火與秩序重組，帶走三個檢視勢力興衰的思考工具。

- **綁定卡片**：`CARD-03`, `CARD-25`, `CARD-26`, `CARD-27`, `CARD-28`
- **視覺與版面配置**：編輯索引三欄收束頁（襯線大序號 `01 / 02 / 03` 與水平細線排版，呼應開篇核心主軸）。
- **簡報內文**：
  - **標題**：面對戰火與秩序重組，帶走三個檢視勢力興衰的思考工具。
  - **正文**：
    - 第一，看「組織兩難」：追求集權贏戰時，左翼能否避免在內部清洗中自我吞噬？
    - 第二，看「後方紮根」：武裝靠強徵與貪腐維繫，還是靠土改減稅與跨群體統戰贏得支持？
    - 第三，看「跨區連動」：別忘了追蹤流亡軍人、外國軍火與禁運如何跨洲重塑本地戰局。
  - **承上啟下過渡句（全場收束）**：回到核心之問：唯有兼顧基層認同與後方秩序者，才能走到最後。
- **來源**：`[01_russian_civil_war.md, 導言]; [02_german_revolution_1918_1919.md, 導言]; [03_spanish_civil_war.md, Spanish Revolution]; [04_warlord_era_china.md, Aftermath]; [05_second_united_front.md, Breakdown and aftermath]; [06_yugoslav_partisans.md, Post-war]`
- **字數預估**：中文字 147 字｜正文可視字元 170 字（無 SVG，安全低於 280 字）
