# 聖若瑟教區中學第五校｜小學數學 × OpenCode — AI Agent 實作工作坊

> **校訓理念：**「AI 時代守本心，毅誠勤樸篤前行」  
> 本網站專為**澳門聖若瑟教區中學第五校 小學中英文部數學教師**設計，作為「小學數學 × OpenCode — AI Agent 實作工作坊」的學員手冊、講師教案與現場操作指南。

遵循 `SKILL.md` 之所有規範，採用**純 HTML5 + 自包含 CSS** 打造，完全無外部框架或 Node 建置依賴，可直接本機雙擊開啟，或一鍵發布至 **GitHub Pages**。

---

## 🏛️ 工作坊四大核心架構

1. **⏱️ 2 小時（120 分鐘精準實操）**：
   - 0–60 分鐘完成首份備課；60–120 分鐘深耕分層、修訂、重用與課堂難題記錄。
2. **📄 1 個真實教材（守住數學事實）**：
   - 以校本真實數學 PDF 為唯一材料來源，恪守知識點邊界，嚴禁虛構算理。
3. **🔄 4 次 Agent 工作循環**：
   - 第一次備課（規格先於產出）
   - 分層設計（認知階梯與學習支架）
   - 同步修訂（跨檔案連鎖修改與差異追蹤）
   - 再次重用（新課題直接複用專案規則）
4. **📦 1 個可重用專案（長期校本資產）**：
   - 建立具備 `AGENTS.md` 長期規範的專案結構，成為個人與科組永久數位教學庫。

---

## 🎯 培訓核心定位與非談判成果

- **時長**：120 分鐘（精確劃分，10+10+10+12+8+10+15+20+15+7+3 = 120 min）。
- **對象**：小學中英文部數學教師（零編程基礎）。
- **非談判成果**：
  1. `output/01-first-version/`：第一次備課成果（第 60 分鐘合格線）。
  2. `output/02-differentiated/`：A 支援 / B 基準 / C 挑戰分層材料。
  3. `output/03-revised/`：同步修訂成果與 `change-summary.md` 差異報告。
  4. `output/04-reused/`：新課題專案重用成果。
  5. `notes/next-workshop-problem.md`：記錄一個真實課堂問題離場（下一場培訓起點）。

---

## 📂 網站與專案目錄結構

```text
14_培訓網頁/
├── index.html                            # 培訓首頁（四大架構、概覽、4大成果、專案地圖、GitHub部署）
├── workshop-flow.html                    # 120 分鐘實操流程與逐分鐘時間軸
├── prompts.html                          # 8 階段精準 Prompt 庫 + 一鍵複製 + V2 完整任務
├── troubleshooting.html                  # 10 大常見問題排查 + 40 人現場突發 SOP
├── images/                               # 輕量響應式 SVG 圖解
│   ├── 00-workshop-map.svg               # 2 小時學習迴圈流程圖
│   └── 01-project-structure.svg          # 專案目錄與權限邊界圖
├── resources/                            # 規範與範本
│   ├── task-spec-template.md             # 需求規格書 task-spec.md 範本
│   ├── next-workshop-problem-template.md # 課堂問題 notes/ 範本
│   └── sample-agents.md                  # 專案持續規則 AGENTS.md 範本
├── skills/
│   └── math-agent-workshop-2h-site/
│       └── SKILL.md                      # Agent 建置規範鏡像檔
├── Math-Agent-Workshop/                  # [保持原貌] 教師實操工作區結構示範
├── OpenCode_40人培訓_Starter_Pack_V2/    # [保持原貌] 40 人現場安裝包、Docx 指南與 BAT
├── SKILL.md                              # 規範說明
└── README.md                             # 專案說明文件
```

---

## 💻 本地預覽方法 (Local Preview)

本網站純靜態，無需編譯：

### 方法 1：直接雙擊開啟
直接在檔案總管中雙擊 `index.html`，即可使用任何現代瀏覽器（Chrome、Edge、Safari、Firefox）瀏覽。

### 方法 2：使用本機輕量 HTTP 伺服器
若習慣透過本機伺服器瀏覽：
```bash
cd "G:\我的雲端硬碟\14_培訓網頁"
python -m http.server 8000
```
開啟瀏覽器訪問：`http://localhost:8000`

---

## 🚀 最後部署到 GITHUB（GitHub Pages 發布指南）

本網站所有資源皆使用相對路徑，完全符合 GitHub Pages 部署標準：

1. **推送代碼至 GitHub 儲存庫**：
   ```bash
   git init
   git add index.html workshop-flow.html prompts.html troubleshooting.html images/ resources/ skills/ README.md
   git commit -m "feat: deploy CDSJ5 math workshop site"
   git branch -M main
   git remote add origin https://github.com/<你的帳號>/<儲存庫名稱>.git
   git push -u origin main
   ```

2. **啟用 GitHub Pages**：
   - 進入該 GitHub 儲存庫的 **Settings**。
   - 點擊左側選單 **Pages**。
   - 在 **Build and deployment** 下方的 **Source** 選擇 `Deploy from a branch`。
   - **Branch** 選擇 `main` 分支，資料夾選擇 `/ (root)`，點擊 **Save**。
   - 約 1–2 分鐘後，即可透過 `https://<你的帳號>.github.io/<儲存庫名稱>/` 訪問完整網站！

---

## 🔒 資料安全與個資保護守則

1. **嚴禁上傳學生個資**：不得將包含學生姓名、座號、成績、家長聯絡等機密文件送入 OpenCode。
2. **保護原始教材**：`materials/` 僅限讀取，嚴禁覆蓋原始 PDF。
3. **API Key 獨立使用**：每位教師在學校 Workspace 建立個人 Key，嚴禁在公開群組或投影畫面洩漏。
