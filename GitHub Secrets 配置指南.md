# GitHub Secrets 配置指南

## 🔐 需要配置的 Secrets

根据你提供的讯飞星火 API 配置，需要在 GitHub 仓库中配置以下 Secrets：

---

### 1. AI API 配置

#### `AI_API_KEY`
```
67f3acdf69c12039e2ae68bd7685cdc0:YjMzZjJjOWM0YTcyZWFmMmVmYjY0YjYx
```

**说明**：讯飞星火 Coding Plan 的 API Key（格式：APIKey:APISecret）

#### `AI_MODEL`
```
openai/astron-code-latest
```

**说明**：模型名称，使用 `openai/` 前缀强制使用 OpenAI 协议

#### `AI_API_BASE`
```
https://maas-coding-api.cn-huabei-1.xf-yun.com/v2
```

**说明**：讯飞星火的 OpenAI 兼容接口地址

---

### 2. 企业微信推送配置（必填）

#### `WEWORK_WEBHOOK_URL`
```
你的企业微信机器人 Webhook 地址
```

**格式示例**：`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx`

**获取方式**：
1. 在企业微信中创建一个群聊（可以只有你自己）
2. 群设置 → 群机器人 → 添加机器人
3. 复制 Webhook 地址

---

## 📝 配置步骤

### 步骤 1：推送代码到 GitHub

```bash
# 进入项目目录
cd d:\RJ\redianxinwen

# 初始化 Git（如果还没有）
git init

# 添加远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/你的用户名/TrendRadar.git

# 添加所有文件
git add .

# 提交
git commit -m "配置 TrendRadar 使用讯飞星火 API"

# 推送到 GitHub
git push -u origin master
```

### 步骤 2：配置 GitHub Secrets

1. **进入仓库设置**
   - 打开你的 GitHub 仓库页面
   - 点击 "Settings" 标签

2. **进入 Secrets 页面**
   - 左侧菜单 → Secrets and variables → Actions

3. **添加 Secrets**
   - 点击 "New repository secret" 按钮
   - 依次添加以下 4 个 Secrets：

   | Name | Value |
   |------|-------|
   | `AI_API_KEY` | `67f3acdf69c12039e2ae68bd7685cdc0:YjMzZjJjOWM0YTcyZWFmMmVmYjY0YjYx` |
   | `AI_MODEL` | `openai/astron-code-latest` |
   | `AI_API_BASE` | `https://maas-coding-api.cn-huabei-1.xf-yun.com/v2` |
   | `WEWORK_WEBHOOK_URL` | 你的企业微信 Webhook 地址 |

   **注意**：每个 Secret 都要单独添加，不能一次性添加所有

### 步骤 3：启用 GitHub Actions

1. 进入仓库的 "Actions" 标签
2. 如果提示启用 Actions，点击 "I understand my workflows, go ahead and enable them"
3. 找到 "Get Hot News" 工作流
4. 点击 "Enable workflow"

### 步骤 4：测试运行

1. 在 Actions 页面
2. 选择 "Get Hot News" 工作流
3. 点击右侧的 "Run workflow" 按钮
4. 选择分支（默认 master）
5. 点击绿色的 "Run workflow" 按钮
6. 等待运行完成（约 2-5 分钟）
7. 查看运行日志
8. 检查企业微信群是否收到消息

---

## ✅ 验证配置是否成功

运行成功后，你应该在企业微信群看到类似这样的消息：

```
📊 TrendRadar 热点新闻推送

【AI 分析板块】
核心热点态势：
...

【热榜新闻】
AI 人工智能：
- xxx新闻标题
...

【RSS 订阅】
Hacker News：
- xxx文章标题
...
```

---

## 🔧 常见问题排查

### Q1: Actions 运行失败，提示 API Key 错误？

**检查**：
- `AI_API_KEY` 是否完整复制（包含冒号和后面的部分）
- `AI_API_BASE` 是否正确
- `AI_MODEL` 是否包含 `openai/` 前缀

### Q2: 没有收到企业微信推送？

**检查**：
- `WEWORK_WEBHOOK_URL` 是否正确配置
- Webhook 地址是否有效（可以在浏览器中访问测试）
- Actions 运行是否成功（查看日志）

### Q3: AI 分析部分为空？

**可能原因**：
- 讯飞星火 API 调用失败
- 查看 Actions 日志中的错误信息
- 检查 API Key 是否有余额

### Q4: 提示 "试用期已结束"？

**解决方法**：
- 进入 Actions 页面
- 找到 "Check In" 工作流
- 点击 "Run workflow" 签到续期
- 试用期会重置为 7 天

---

## 📊 讯飞星火 Coding Plan 说明

### 模型信息
- **模型名称**：astron-code-latest（默认 GLM5.0）
- **接口类型**：OpenAI 兼容接口
- **接口地址**：https://maas-coding-api.cn-huabei-1.xf-yun.com/v2
- **文档链接**：https://www.xfyun.cn/doc/spark/CodingPlan.html

### 成本估算
根据讯飞星火 Coding Plan 的计费方式：
- 每天两次推送 + AI 分析
- 预估成本：约 0.1-0.3 元/天（具体取决于新闻数量和 token 消耗）

### 特点
- ✅ 国内服务，访问速度快
- ✅ OpenAI 协议兼容，易于集成
- ✅ 性价比高
- ✅ 支持中文分析效果好

---

## 🎯 下一步

配置完成后，系统将：
- ✅ 每小时自动采集热点数据
- ✅ 早上 8:00-9:00 推送当前热点 + AI 分析
- ✅ 晚上 8:00-9:00 推送全天汇总 + AI 分析
- ✅ 自动筛选科技、AI、汽车、军事、国际形势相关新闻
- ✅ 使用讯飞星火 AI 进行深度分析

---

## 📚 相关文档

- **讯飞星火文档**：https://www.xfyun.cn/doc/spark/CodingPlan.html
- **TrendRadar 主文档**：README.md
- **配置说明**：配置说明.md
- **可视化编辑器**：https://sansan0.github.io/TrendRadar/

---

## 💡 提示

1. **首次运行建议**：手动触发一次测试，确保配置正确
2. **长期使用**：考虑部署 Docker 版本（无 7 天限制）
3. **监控成本**：定期检查讯飞星火账户余额
4. **调整配置**：根据实际效果调整 `ai_interests.txt` 和 `frequency_words.txt`

---

配置完成后，你就可以开始享受个性化的热点新闻推送服务了！🚀