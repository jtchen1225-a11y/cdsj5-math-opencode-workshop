# 專案後台工程支撐腳本 (Project Support Scripts)

本資料夾歸檔本專案所有自動化處理、校驗、同步及生成腳本，嚴格遵守全域專案開發與工程規範。專案根目錄維持純發布成果，不散落輔助腳本。

## 腳本清單

1. **`verify_workshop_site.py`**
   - **作用**：自動檢驗工作坊 4 大頁面（`index.html`、`workshop-flow.html`、`prompts.html`、`troubleshooting.html`）的架構與完整性。
   - **校驗項目**：
     - 短網址鏈接與短網址複製功能（`daydaystudy.top/cdsj5`、`daydaystudy.top/prompt`）。
     - 聖若瑟五校校訓金色精神信念標章（「AI 時代守本心，毅誠勤樸篤前行」與「AI 負責流程加速，教師專注教學判斷、算理本質與關懷學生」）。
     - 12 頁投影地圖（Deck Modal）零捲軸架構（`overflow: hidden !important`、`#deck-slide-content` 彈性分佈、`@media (max-height: 780px)` 適配）。
     - `prompts.html` 獨立學員實操工作台隔離性驗證（零跨頁外部連結、移除簡報干擾）。
   - **執行方式**：
     ```bash
     python _scripts/verify_workshop_site.py
     ```

2. **`audit_prompts_links.py`**
   - **作用**：掃描並審計 `prompts.html` 內所有的 `<a>` 標籤與超連結，確保 100% 僅指向本頁錨點（`#prompt-*`），零外部或跨頁外跳連結。
   - **執行方式**：
     ```bash
     python _scripts/audit_prompts_links.py
     ```

3. **`test_deck_layout_math.py`**
   - **作用**：以數值精確模擬並驗證 768p、800p、900p、1080p、1440p 投影設備下的黑板卡片可用高度、字級與行距，確保在字體最大化、閱讀最舒適的前提下，垂直保留安全裕度（Margin > 0），零溢出、零滾動條。
   - **執行方式**：
     ```bash
     python _scripts/test_deck_layout_math.py
     ```
