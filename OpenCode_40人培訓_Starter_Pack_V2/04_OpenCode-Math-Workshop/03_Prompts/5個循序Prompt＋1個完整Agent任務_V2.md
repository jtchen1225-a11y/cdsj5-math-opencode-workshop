# 5 個循序 Prompt + 1 個完整 Agent 任務（V2）

> 使用方法：由 Prompt 1 開始。講師以 A/B/C/D 四組錯峰送出。

## Prompt 1｜先認識工作區，不改任何檔案
請先閱讀 `AGENTS.md`，再列出本工作區中你能看到的教材、練習、Skills 與輸出資料夾。暫時不要建立或修改任何檔案。

## Prompt 2｜讀教材並分析
請使用 `textbook-analysis` skill，閱讀 `01_Input/textbook/P4_分數示範教材_6頁.pdf`。整理：學習目標、核心概念、先備知識、重要表徵、常見迷思、應用情境與推理要求。先在畫面回答，不要寫檔案。

## Prompt 3｜分析現有練習
閱讀 `01_Input/exercises/P4_分數練習_4頁.pdf`，把題目按「概念理解 / 程序技能 / 應用 / 推理」分類，並指出至少 5 個學生可能出現的典型錯因。如 PDF 無法可靠讀取，停止並說明，不可猜測。

## Prompt 4｜生成分層工作紙
請使用 `worksheet-generator` skill，依據剛才可靠讀到的教材內容，設計 9 題分層練習：A 基礎 3 題、B 應用 3 題、C 推理 3 題；附答案與簡短評分要點。先在畫面展示，不要寫檔案。

## Prompt 5｜把內容變成課堂
請使用 `lesson-designer` skill，設計一個「課前 8 分鐘 TIMSS 式分數活動」，採 2+2+3+1 節奏，明確寫出教師行動、學生行動、典型錯誤與最後一句總結。

---

# 完整 Agent 任務｜一次產出 4 份教師成品
請先閱讀 `AGENTS.md`，並按需要載入 `textbook-analysis`、`worksheet-generator`、`lesson-designer` 三個 skills。

可靠閱讀：
- `01_Input/textbook/P4_分數示範教材_6頁.pdf`
- `01_Input/exercises/P4_分數練習_4頁.pdf`

如果任何 PDF 無法可靠讀取，立即停止並報告問題，不得臆測。若能可靠讀取，請只在 `02_Output/` 建立以下 4 個檔案：

1. `01_教材與知識點分析.md`
2. `02_練習題認知層次與錯因.md`
3. `03_分層練習_9題.md`
4. `04_課前8分鐘TIMSS活動.md`

要求：
- 使用繁體中文。
- 每一份都要能直接給小學數學教師使用。
- 不修改 `01_Input/`。
- 完成後列出你建立的檔名，並用 5 行總結這次 Agent 做了甚麼。
