@echo off
chcp 65001 >nul
echo ==========================================
echo   推送修复代码到 GitHub
echo ==========================================
echo.

cd /d "d:\RJ\redianxinwen"

echo [问题说明]
echo 虽然你配置了 GitHub Secrets，但程序没有读取企业微信应用的配置。
echo 我已经修复了代码，添加了企业微信应用配置的读取逻辑。
echo.

echo [推送步骤]
echo 请按照以下步骤推送代码：
echo.

echo 1. 确认代理已启动（端口 7899）
echo 2. 按任意键开始推送...
pause >nul

echo.
echo [推送中...]
git push

if %errorlevel% equ 0 (
    echo.
    echo ==========================================
    echo   推送成功！
    echo ==========================================
    echo.
    echo 下一步：
    echo 1. 访问: https://github.com/wawojx-lab/TrendRadar/actions
    echo 2. 手动触发 "Get Hot News" 工作流
    echo 3. 查看运行日志，确认显示 "企业微信应用消息发送成功"
    echo 4. 检查企业微信是否收到消息
    echo.
) else (
    echo.
    echo ==========================================
    echo   推送失败
    echo ==========================================
    echo.
    echo 可能的原因：
    echo 1. 代理未启动或端口不对
    echo 2. 网络连接问题
    echo.
    echo 解决方法：
    echo 1. 确认代理已启动（端口 7899）
    echo 2. 检查网络连接
    echo 3. 手动推送: git push
    echo.
)

pause
