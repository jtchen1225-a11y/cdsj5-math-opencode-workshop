@echo off
chcp 65001 >nul
title OpenCode 培訓 - 環境檢查
echo ========================================
echo OpenCode 40 人培訓 - 環境檢查 V2
echo ========================================
echo.
echo [1/3] Node.js
node -v
if errorlevel 1 echo [FAIL] 找不到 Node.js，請先安裝 Node.js LTS。
echo.
echo [2/3] npm
npm -v
if errorlevel 1 echo [FAIL] 找不到 npm，請重新安裝 Node.js LTS。
echo.
echo [3/3] OpenCode
opencode --version
if errorlevel 1 echo [FAIL] 找不到 OpenCode，請在 cmd 執行：npm install -g opencode-ai
echo.
echo 如果上面三項都有版本號，環境基本合格。
echo 若有 FAIL，請把此畫面給技術助手查看。
echo.
pause
