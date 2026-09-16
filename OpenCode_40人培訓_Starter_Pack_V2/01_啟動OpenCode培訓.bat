@echo off
chcp 65001 >nul
cd /d "%~dp004_OpenCode-Math-Workshop"
if not exist "AGENTS.md" (
  echo [FAIL] 找不到 Workshop。請確認已完整解壓縮整個 Starter Pack V2。
  pause
  exit /b 1
)
opencode
if errorlevel 1 (
  echo.
  echo [FAIL] OpenCode 未能啟動。先執行 00_一鍵檢查環境.bat。
  pause
)
