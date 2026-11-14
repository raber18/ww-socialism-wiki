# Node 1 檢索與覆蓋率報告（`sources.md`）

## 一、主題界定與教學焦點

- **教學主題**：戰火下的路線分歧：1914–1945 歐亞社會主義流派與地方勢力的崛起比較
- **目標受眾**：沒有歷史背景的初學者（不預設了解黨派縮寫、馬克思主義術語或各國內戰史前情）
- **核心教學焦點**：
  1. **共同的時代背景**：1914–1945 年兩次世界大戰與戰間期衝突如何摧毀舊帝國與中央政府，在歐亞多地製造權力真空，同時催生「左翼／社會主義流派」與「地方／民間武裝勢力」。
  2. **社會主義陣營內部的四大路線分歧**：同樣追求社會主義或反壓迫變革，各派在「一黨專政（布爾什維克／史達林派）」、「議會改良妥協（德國 SPD／西班牙 PSOE 溫和派）」、「基層無政府自治（俄烏馬赫諾運動／西班牙 CNT-FAI）」與「抗戰人民陣線及農村游擊（中共／南斯拉夫共產黨）」之間出現劇烈分裂與甚至武裝清洗。
  3. **地方勢力的崛起、跨區流動與結局對比**：分析工兵委員會、農民秘密結社、軍閥派系、外籍志願軍與游擊隊如何徵兵、籌資與爭取外援；追蹤白俄流亡者、坦克軍火與西班牙老兵如何在歐亞大陸間跨區連動；比較地方勢力為何有的遭鎮壓吞併，有的卻能建國或奪取全國政權。
  4. **史觀衝突與史料邊界**：並陳各事件對立的史學詮釋（如俄國防衛論 vs. 專政論、德國 SPD 護憲論 vs. 背叛論、西班牙失序論 vs. 半組織化 *checas*、中國皖南事變互控、南斯拉夫戰後清洗禁忌與修正主義），並如實標註 `raw/` 原始資料未及之處。

---

## 二、覆蓋率檢核表（檢查關卡 1）

| 檢核維度 | 工作流門檻 | 本次實際覆蓋結果 | 通過狀態 |
| --- | --- | --- | --- |
| **地理區域數量** | 至少 **3** 個不同地理區域 | **5** 個區域：俄國（含前帝國邊疆與中亞）、德國、西班牙、中國、南斯拉夫 | **PASS**（5 >= 3） |
| **原始來源檔案數** | 至少 **4** 篇不同 `raw/` 原始來源 | **6** 篇全部來源：`01_russian_civil_war.md`、`02_german_revolution_1918_1919.md`、`03_spanish_civil_war.md`、`04_warlord_era_china.md`、`05_second_united_front.md`、`06_yugoslav_partisans.md` | **PASS**（6 >= 4） |

### 原始來源覆蓋明細

1. `01_russian_civil_war.md`（俄國／前俄帝國邊疆與中亞，1917–1923 年，含中亞抵抗延至 1934 年） `[01_russian_civil_war.md, 導言; Aftermath > Ensuing rebellion]`
2. `02_german_revolution_1918_1919.md`（德國，1914–1923 年戰後餘波與 1933 年背景） `[02_german_revolution_1918_1919.md, 導言; Background events; Aftermath; Impact on the Weimar Republic]`
3. `03_spanish_civil_war.md`（西班牙，1931–1939 年及戰後餘波） `[03_spanish_civil_war.md, 導言; Background; Course of the war > 1939]`
4. `04_warlord_era_china.md`（中國，1916–1928 年及 1928–1949 年餘波） `[04_warlord_era_china.md, 導言; Aftermath]`
5. `05_second_united_front.md`（中國，1935–1949 年） `[05_second_united_front.md, 導言; Background; Breakdown and aftermath > After 1945]`
6. `06_yugoslav_partisans.md`（南斯拉夫，1941–1948 年及戰後餘波） `[06_yugoslav_partisans.md, 導言; Post-war]`

> **檢查關卡 1 結論**：已同時滿足「>= 3 個地區（實得 5 個）」與「>= 4 篇原始來源（實得 6 篇）」，通過覆蓋率關卡，准予進入 Node 2 萃取證據卡。

---

## 三、入選 Wiki 頁面清單（共 52 頁，優先納編跨區綜合頁與核心流派、勢力、事件頁）

### 1. 跨區域與跨流派比較（`wiki/syntheses/`，2 頁）

| Wiki 相對路徑 | 涵蓋區域 | 關聯原始來源 | 一句話入選理由 |
| --- | --- | --- | --- |
| `wiki/syntheses/socialism_branches_comparison.md` | 俄國、德國、西班牙、中國、南斯拉夫 | `01`, `02`, `03`, `04`, `05`, `06` | 提供五大區域社會主義與左翼光譜、奪權路徑、左翼內戰及共通史觀爭議的總覽骨架。 |
| `wiki/syntheses/local_factions_and_war_dynamics.md` | 俄國、德國、西班牙、中國、南斯拉夫 | `01`, `02`, `03`, `04`, `05`, `06` | 整合比較歐亞地方軍閥、委員會、民兵與游擊隊的興起背景、財政兵源、跨國流動與結局路徑。 |

### 2. 社會主義與相關政治流派（`wiki/ideologies/`，14 頁）

| Wiki 相對路徑 | 涵蓋區域 | 關聯原始來源 | 一句話入選理由 |
| --- | --- | --- | --- |
| `wiki/ideologies/bolshevism.md` | 俄國（並輻射德、西、中、南） | `01`, `02`, `03`, `04`, `05`, `06` | 解析列寧布爾什維克一黨專政、戰時共產主義與民主集中制如何成為歐亞共黨原型及各國分歧起點。 |
| `wiki/ideologies/socialist_revolutionaries.md` | 俄國 | `01` | 呈現 1917 年曾贏得立憲會議多數的俄國社會革命黨如何分裂為右翼「民主反革命」與左翼起義派。 |
| `wiki/ideologies/menshevism.md` | 俄國（含高加索與中亞） | `01` | 說明孟什維克遭逐出蘇維埃後聯手右翼 SR 充當「第三勢力」並在邊疆求援英軍的路線。 |
| `wiki/ideologies/anarchism.md` | 俄國、西班牙、中國（山西） | `01`, `03`, `04` | 串聯俄烏馬赫諾運動、西班牙 CNT-FAI 革命與山西閻錫山折衷信條，呈現自由意志左翼的跨區實踐。 |
| `wiki/ideologies/german_social_democracy.md` | 德國 | `02` | 闡明德國多數派 SPD 為何拒斥布爾什維主義、聯手舊軍方與資方制憲，並引發三大史觀論戰。 |
| `wiki/ideologies/uspd.md` | 德國 | `02` | 補充介於 SPD 與 KPD 之間、主張延後制憲並於聖誕危機退出執政的德國獨立社民黨關鍵中樞角色。 |
| `wiki/ideologies/spartacists_and_kpd.md` | 德國 | `02` | 說明斯巴達克同盟與 KPD 追求委員會共和國的綱領、黨內選舉與起義路線衝突及遇害經過。 |
| `wiki/ideologies/spanish_anarcho_syndicalism_cnt_fai.md` | 西班牙 | `03` | 詳述 CNT-FAI 從反第二共和國到 1936 年推動農業集體化與工業社會化的無政府工團主義實踐。 |
| `wiki/ideologies/spanish_socialism_psoe_ugt.md` | 西班牙 | `03` | 解析 PSOE 內部在 1933 年敗選後分化為卡瓦耶羅革命馬克思派與議會溫和派的路線撕裂。 |
| `wiki/ideologies/spanish_communism_pce_and_poum.md` | 西班牙 | `03` | 對比依附蘇援主張保守防衛的史達林派 PCE 與推動革命卻遭 NKVD 謀殺清洗的反史達林派 POUM。 |
| `wiki/ideologies/chinese_nationalism_kmt_and_ccp.md` | 中國 | `04`, `05` | 說明孫中山藉蘇援依列寧式民主集中制改組國民黨、促成國共合作與 1927 年寧漢分裂的跨國制度移植。 |
| `wiki/ideologies/warlordism_and_regional_political_experiments.md` | 中國 | `04` | 剖析中國軍閥的靜態割據與均勢邏輯，以及閻錫山、馮玉祥、吳佩孚等特殊思想折衷與地方實驗。 |
| `wiki/ideologies/chinese_communism_and_united_front.md` | 中國（對照西班牙、南斯拉夫） | `04`, `05`, `03`, `06` | 梳理抗戰中毛澤東「獨立自主／以空間換時間」與王明「一切經過統一戰線」之爭及敵後土改路線。 |
| `wiki/ideologies/yugoslav_communism_and_titoism.md` | 南斯拉夫（對照西班牙） | `06`, `03` | 解讀南共（KPJ）如何藉淡化共產主義的「兄弟情誼與團結」人民陣線整合各族並走向蘇南分裂。 |

### 3. 地方勢力與武裝組織（`wiki/factions/`，22 頁）

| Wiki 相對路徑 | 涵蓋區域 | 關聯原始來源 | 一句話入選理由 |
| --- | --- | --- | --- |
| `wiki/factions/russian_soviets.md` | 俄國 | `01` | 追蹤基層民選工農兵議會「蘇維埃」如何從雙重政權核心逐步官僚化為一黨國家機構。 |
| `wiki/factions/red_army.md` | 俄國 | `01` | 揭示紅軍如何從志願赤衛隊轉向農村強制徵兵、任用 83% 沙俄軍官及部署督戰隊贏得內戰。 |
| `wiki/factions/white_movement.md` | 俄國（流亡至中國、西班牙） | `01`, `04`, `03` | 呈現白軍綱領、白色恐怖及戰敗後 100–200 萬流亡者與武器轉入中國奉系及西班牙國民軍之跨區軌跡。 |
| `wiki/factions/black_army_makhnovshchina.md` | 俄國／烏克蘭 | `01` | 記錄烏克蘭馬赫諾無政府主義起義軍兩度助紅軍破白軍卻在 1920 年底遭紅軍背棄圍剿的地方武裝悲劇。 |
| `wiki/factions/green_armies.md` | 俄國 | `01` | 說明反對紅白雙方與徵糧的「非意識形態綠軍」及坦波夫農民起義（24 萬人口損失）如何迫出新經濟政策。 |
| `wiki/factions/borderland_and_central_asian_factions.md` | 俄國邊疆與中亞 | `01` | 對照芬蘭及波羅的海三國趁亂獨立建國，與高加索及中亞浩罕／巴斯馬奇運動遭紅軍擊敗的不同結局。 |
| `wiki/factions/czechoslovak_legion_and_foreign_interventions.md` | 俄國（遺留軍火至中國） | `01`, `04` | 涵蓋捷克軍團與 13 國干涉內戰經過，並連結海參崴遺留法製 FT-17 坦克流入東北張作霖軍中的跨區線索。 |
| `wiki/factions/german_workers_and_soldiers_councils.md` | 德國 | `02` | 呈現全德溫和工兵委員會、柏林革命代表、人民海軍師與短命地方蘇維埃共和國／魯爾紅軍的基層動態。 |
| `wiki/factions/freikorps_and_german_military.md` | 德國 | `02` | 說明保留舊指揮架構的帝國軍方與諾斯克擴編之右翼自由軍團如何武裝平定極左起義並埋下威瑪隱患。 |
| `wiki/factions/spanish_popular_front_and_republicans.md` | 西班牙 | `03` | 解析人民陣線「半多元框架」下民兵整合為人民共和軍（EPR）的困難及中央與加泰隆尼亞／巴斯克摩擦。 |
| `wiki/factions/cnt_fai_and_left_militias.md` | 西班牙 | `03` | 記述 1936 年 7 月工人開倉發槍阻止政變、建立革命民兵（含杜魯蒂縱隊）與抗拒正規化的衝突。 |
| `wiki/factions/spanish_nationalists_and_falange.md` | 西班牙（對比俄、中） | `03` | 說明非洲軍團、軍官「非洲派」與佛朗哥收編 FET y de las JONS 的集權機制及後方治安比較。 |
| `wiki/factions/international_brigades.md` | 西班牙、南斯拉夫 | `03`, `06` | 記錄 53 國反法西斯志願者規模與馬蒂清洗爭議，並揭示逾千名南斯拉夫老兵返國組成游擊隊骨幹之跨國橋樑。 |
| `wiki/factions/spanish_civil_war_foreign_interventions.md` | 西班牙（多國干涉） | `03` | 對比 27 國不干涉武器禁運如何重創共和國，及德（禿鷹軍團）義（CTV）葡援國民軍與蘇「X 行動」角力。 |
| `wiki/factions/beiyang_warlord_cliques.md` | 中國 | `04`, `05` | 追蹤北洋皖直奉三系興衰、張作霖吸納白俄武器軍團，以及張學良東北軍在 1936 年西安事變的關鍵轉向。 |
| `wiki/factions/guominjun_shanxi_and_northwest_warlords.md` | 中國 | `04`, `05` | 涵蓋馮玉祥國民軍、閻錫山異軌鐵路與太原兵工廠半獨立體系、馬家軍／回族騎兵及楊虎城西北軍。 |
| `wiki/factions/chinese_peasant_militias_and_foreign_powers.md` | 中國 | `04` | 揭示農村自衛秘密會社（紅槍會、孝衣會、全女性鐵門會／花籃會）、白俄雇傭兵與海關總稅務司／禁運漏洞。 |
| `wiki/factions/kmt_nra_and_ccp.md` | 中國（對比西班牙） | `04`, `05`, `03` | 呈現黃埔建軍、北伐整批收編軍閥的結構弱點，以及戰時軍閥腐敗倒戈促成 1949 年中共勝出的因果鏈。 |
| `wiki/factions/ccp_eighth_route_and_new_fourth_armies.md` | 中國 | `05`, `04` | 追蹤八路軍與新四軍、陝甘寧及晉察冀邊區如何在名義服從下透過敵後收編與土改發展為全國政權力量。 |
| `wiki/factions/yugoslav_partisans.md` | 南斯拉夫 | `06` | 詳載游擊隊由 8.1 萬擴至逾 80 萬大軍、首創歐洲抵抗運動空軍與海軍及 200 萬 AFŽ／10 萬女戰士動員實績。 |
| `wiki/factions/chetniks.md` | 南斯拉夫 | `06` | 剖析保皇派切特尼克因大塞族種族清洗、畏懼人質報復避戰通敵而失去盟軍承認（含救美飛行員矛盾）的過程。 |
| `wiki/factions/ustase_ndh_and_axis_occupiers_yugoslavia.md` | 南斯拉夫 | `06` | 說明 1941 年軸心國肢解體制、德軍百人質屠殺與烏斯塔沙滅絕暴行如何反而將各族平民推向游擊隊。 |

### 4. 關鍵事件與轉折點（`wiki/events/`，14 頁）

| Wiki 相對路徑 | 涵蓋區域 | 關聯原始來源 | 一句話入選理由 |
| --- | --- | --- | --- |
| `wiki/events/february_and_october_revolutions_1917.md` | 俄國（影響德國） | `01`, `02` | 建立一戰壓垮沙俄、雙重政權與十月革命震盪歐洲的時代原點。 |
| `wiki/events/dissolution_of_constituent_assembly_1918.md` | 俄國 | `01` | 鎖定 1918 年 1 月布爾什維克敗選後解散立憲會議作為一黨專政與社會革命黨反抗的結構轉折。 |
| `wiki/events/red_terror_and_left_sr_uprising_1918.md` | 俄國（外溢至西班牙） | `01`, `03` | 呈現左翼 SR 七月起義、全面紅色恐怖、死亡數據巨大分歧及「契卡（*checas*）」向西班牙外溢之軌跡。 |
| `wiki/events/kronstadt_and_tambov_rebellions_1921.md` | 俄國 | `01` | 說明 1921 年水兵與農民起義遭鎮壓後，俄共十大派系禁令與新經濟政策（NEP）定型蘇聯體制的關鍵轉折。 |
| `wiki/events/kiel_mutiny_and_november_9_1918.md` | 德國 | `02` | 還原 1918 年水兵抗命、全德無流血推翻王朝及 11 月 9 日謝德曼與李卜克內西宣告兩個共和國的時刻。 |
| `wiki/events/ebert_groener_pact_and_council_congress_1918.md` | 德國 | `02` | 記錄艾伯特－格勒納密約、施廷內斯－萊吉恩協定、代表大會讓權（344:98 票）與聖誕危機破裂經過。 |
| `wiki/events/spartacist_uprising_and_1919_revolts.md` | 德國 | `02` | 記述一月暴動實情（KPD 未主導）、李卜克內西與盧森堡遭自由軍團殺害及柏林三月戰鬥／地方蘇維埃覆滅。 |
| `wiki/events/weimar_constitution_and_post_1919_aftermath.md` | 德國（關聯蘇俄） | `02`, `01` | 整合威瑪制憲、第 48 條隱患、魯爾紅軍／三月行動、拉帕洛條約外交轉向與現代史學研究共識。 |
| `wiki/events/spanish_revolution_and_may_days_1937.md` | 西班牙 | `03` | 聚焦 1936 年集體化社會革命與 1937 年巴塞隆納五月事件中史達林派對 CNT-FAI 及 POUM 的武裝壓制。 |
| `wiki/events/spanish_civil_war_terror_and_aftermath.md` | 西班牙（跨區對比） | `03` | 提供紅白恐怖傷亡統計、38.9 億美元戰時融資對比及「國家失序論 vs. 半組織化 *checas*」與「一戰危機論」爭辯。 |
| `wiki/events/post_1928_warlord_conflicts_and_nanjing_decade.md` | 中國（對比西班牙） | `04`, `05`, `03` | 追蹤 1928 年名義統一後的中原大戰、新疆戰事與南京十年妥協結構如何延續至 1949 年政權易手。 |
| `wiki/events/xian_incident_and_second_united_front_1936_1945.md` | 中國 | `05`, `04` | 詳述蘇聯促和、西北軍閥與中共秘密停火、1936 西安事變及第二次國共合作建立初期架構。 |
| `wiki/events/wannan_incident_and_kmt_ccp_breakdown_1938_1949.md` | 中國（對比西班牙） | `05`, `04`, `03` | 呈現 1941 年皖南事變（並列國共先開火互控）、敵後三角交鋒與戰後東北日械暨軍閥倒戈結局。 |
| `wiki/events/yugoslav_postwar_purges_and_tito_stalin_split.md` | 南斯拉夫 | `06` | 揭露 1944–1945 年布萊堡等大清洗（8–10 萬死）、1947–1948 年蘇南分裂及 1990 年代後史觀修正主義爭議。 |

---

## 四、初步識別之 `raw/` 資料缺口提醒

依據 `AGENTS.md` 誠實不知原則，預先彙整現有 6 篇原始來源並未載明、後續撰寫證據卡與教學簡報時嚴禁腦補的關鍵空白：

1. `[資料不足／不確定：02_german_revolution_1918_1919.md 未詳述德國獨立無政府主義派別活動、1923 年後至 1933 年間 SPD 與 KPD 路線演變，亦未提供工兵委員會與自由軍團各自總兵力、詳細財政收支及巴伐利亞／不來梅／符茲堡蘇維埃共和國的領導名單與施政綱領]`
2. `[資料不足／不確定：04_warlord_era_china.md 與 05_second_united_front.md 未記載中國共產黨 1921 年建黨經過與 1927–1935 年蘇區／長征詳情、王明與毛澤東分歧背後的共產國際訓令細節、八路軍與新四軍具體年度人數成長曲線、1941 年皖南事變先開火責任歸屬，以及 1931–1937 年新疆戰事交戰各方與蘇聯角色]`
3. `[資料不足／不確定：03_spanish_civil_war.md 未詳列 CNT 與 FAI 各自創設時間與規模、1936 年人民陣線全部成員黨名單、1937 年五月事件具體導火線與傷亡數，亦未說明國際縱隊「約 32,000 人」與「粗估 40,000 人」兩組數字之調和方法]`
4. `[資料不足／不確定：01_russian_civil_war.md 未記載綠軍組織結構、活動範圍、指揮官姓名與兵力規模，未詳述坦波夫起義是否全數或部分歸屬綠軍體系，亦未列出干涉俄國的「13 個外國國家」完整名單]`
5. `[資料不足／不確定：06_yugoslav_partisans.md 未記載南斯拉夫共產黨 1920–1940 年地下時期選舉與綱領細節、1948 年蘇南分裂後工人自治經濟理論內涵、切特尼克與內迪奇政權總兵力、1942 年 12 月游擊隊兵力「236,000 人」與統計表「135,000 人」落差原因，亦未明載「二戰歐洲僅有的兩個主要依靠自身力量解放的國家」中之另一國名稱]`
6. `[資料不足／不確定：除俄國白軍流亡中／西、共產國際／蘇聯援助與南斯拉夫西班牙內戰老兵返國抗戰外，6 篇原始來源對歐亞各非蘇聯左翼流派之間的直接跨國思想交流細節缺乏系統性記載]`
