# coding=utf-8
"""
企业微信应用推送模块

实现企业微信应用消息推送，直接推送到个人微信。
"""

import time
import requests
from typing import Optional


class WeWorkAppSender:
    """企业微信应用消息发送器"""

    def __init__(
        self,
        corp_id: str,
        agent_id: str,
        agent_secret: str,
        proxy_url: Optional[str] = None
    ):
        """
        初始化企业微信应用发送器

        Args:
            corp_id: 企业ID
            agent_id: 应用AgentId
            agent_secret: 应用Secret
            proxy_url: 代理URL（可选）
        """
        self.corp_id = corp_id
        self.agent_id = agent_id
        self.agent_secret = agent_secret
        self.proxy_url = proxy_url
        self.access_token = None
        self.token_expires_at = 0

    def get_access_token(self) -> Optional[str]:
        """
        获取企业微信 access_token

        Returns:
            access_token 或 None（失败时）
        """
        # 检查缓存的 token 是否有效
        if self.access_token and time.time() < self.token_expires_at:
            return self.access_token

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": self.corp_id,
            "corpsecret": self.agent_secret
        }

        proxies = None
        if self.proxy_url:
            proxies = {"http": self.proxy_url, "https": self.proxy_url}

        try:
            response = requests.get(url, params=params, proxies=proxies, timeout=30)
            if response.status_code == 200:
                result = response.json()
                if result.get("errcode") == 0:
                    self.access_token = result.get("access_token")
                    # token 有效期 7200 秒，提前 5 分钟刷新
                    self.token_expires_at = time.time() + result.get("expires_in", 7200) - 300
                    print(f"✅ 获取企业微信 access_token 成功")
                    return self.access_token
                else:
                    print(f"❌ 获取 access_token 失败：{result.get('errmsg')}")
                    return None
            else:
                print(f"❌ 获取 access_token 失败，状态码：{response.status_code}")
                return None
        except Exception as e:
            print(f"❌ 获取 access_token 出错：{e}")
            return None

    def send_text_message(
        self,
        user_id: str,
        content: str,
        enable_id_trans: bool = False
    ) -> bool:
        """
        发送文本消息到个人微信

        Args:
            user_id: 用户ID（企业微信账号）
            content: 消息内容
            enable_id_trans: 是否开启ID转译（可选）

        Returns:
            bool: 发送是否成功
        """
        access_token = self.get_access_token()
        if not access_token:
            print("❌ 无法获取 access_token，消息发送失败")
            return False

        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send"
        params = {"access_token": access_token}

        payload = {
            "touser": user_id,
            "msgtype": "text",
            "agentid": int(self.agent_id),
            "text": {
                "content": content
            },
            "enable_id_trans": 1 if enable_id_trans else 0
        }

        proxies = None
        if self.proxy_url:
            proxies = {"http": self.proxy_url, "https": self.proxy_url}

        try:
            response = requests.post(
                url,
                params=params,
                json=payload,
                proxies=proxies,
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                if result.get("errcode") == 0:
                    print(f"✅ 企业微信应用消息发送成功")
                    return True
                else:
                    print(f"❌ 企业微信应用消息发送失败：{result.get('errmsg')}")
                    # 如果是 token 过期，清除缓存
                    if result.get("errcode") in [40014, 42001]:
                        self.access_token = None
                        self.token_expires_at = 0
                    return False
            else:
                print(f"❌ 企业微信应用消息发送失败，状态码：{response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 企业微信应用消息发送出错：{e}")
            return False

    def send_markdown_message(
        self,
        user_id: str,
        content: str,
        enable_id_trans: bool = False
    ) -> bool:
        """
        发送 Markdown 消息到个人微信

        Args:
            user_id: 用户ID（企业微信账号）
            content: Markdown 内容
            enable_id_trans: 是否开启ID转译（可选）

        Returns:
            bool: 发送是否成功
        """
        access_token = self.get_access_token()
        if not access_token:
            print("❌ 无法获取 access_token，消息发送失败")
            return False

        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send"
        params = {"access_token": access_token}

        payload = {
            "touser": user_id,
            "msgtype": "markdown",
            "agentid": int(self.agent_id),
            "markdown": {
                "content": content
            },
            "enable_id_trans": 1 if enable_id_trans else 0
        }

        proxies = None
        if self.proxy_url:
            proxies = {"http": self.proxy_url, "https": self.proxy_url}

        try:
            response = requests.post(
                url,
                params=params,
                json=payload,
                proxies=proxies,
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                if result.get("errcode") == 0:
                    print(f"✅ 企业微信应用消息发送成功")
                    return True
                else:
                    print(f"❌ 企业微信应用消息发送失败：{result.get('errmsg')}")
                    # 如果是 token 过期，清除缓存
                    if result.get("errcode") in [40014, 42001]:
                        self.access_token = None
                        self.token_expires_at = 0
                    return False
            else:
                print(f"❌ 企业微信应用消息发送失败，状态码：{response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 企业微信应用消息发送出错：{e}")
            return False
