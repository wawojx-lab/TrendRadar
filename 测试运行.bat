@echo off
chcp 65001 >nul
echo ==========================================
echo   TrendRadar 测试脚本
echo ==========================================
echo.

echo [1/3] 检查 GitHub Actions 状态...
gh workflow list --all

echo.
echo [2/3] 尝试触发工作流...
gh workflow run crawler.yml 2>nul
if %errorlevel% equ 0 (
    echo ✅ 工作流已触发！
) else (
    echo ⏳ 工作流还未识别，请稍等几分钟...
    echo.
    echo 请访问以下链接手动触发：
    echo https://github.com/wawojx-lab/TrendRadar/actions
)

echo.
echo [3/3] 查看最近的运行记录...
gh run list --limit 3

echo.
echo ==========================================
echo   测试步骤
echo ==========================================
echo.
echo 1. 访问: https://github.com/wawojx-lab/TrendRadar/actions
echo 2. 找到 "Get Hot News" 工作流
echo 3. 点击 "Run workflow"
echo 4. 查看运行状态
echo 5. 检查企业微信是否收到消息
echo.
pause
