# 專案後台工程支撐腳本 (Project Support Scripts)

本資料夾歸檔本專案所有自動化處理、校驗、同步及生成腳本，嚴格遵守全域專案開發與工程規範。專案根目錄維持純發布成果，不散落輔助腳本。

## 腳本清單

1. **`verify_workshop_site.py`**
   - **作用**：自動檢驗工作坊 4 大頁面（`index.html`、`workshop-flow.html`、`prompts.html`、`troubleshooting.html`）的完整性。
   - **校驗項目**：
     - 短網址鏈接與短網址複製功能（`daydaystudy.top/cdsj5`、`daydaystudy.top/prompt`）。
     - 聖若瑟五校校訓金色精神信念標章（「AI 時代守本心，毅誠勤樸篤前行」與「AI 負責流程加速，教師專注教學判斷、算理本質與關懷學生」）。
     - 黑板全屏投影簡報（Deck Modal）結構與 12 頁簡報數據完整性。
     - 頁面間互通導航超連結有效性。
   - **執行方式**：
     ```bash
     python _scripts/verify_workshop_site.py
     ```
