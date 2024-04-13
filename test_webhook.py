import os

# 環境変数 'DISCORD_WEBHOOK_URL' の値を取得
webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

# 取得したWebhook URLを表示
print("The Discord webhook URL is:", webhook_url)

# 簡単なメッセージを送信してWebhookが動作するかテスト
if webhook_url:
    import requests
    data = {
        "content": "Hello, Discord! This is a test message from GitHub Actions.",
        "username": "GitHub Actions Bot"
    }
    response = requests.post(webhook_url, json=data)
    print("Sent test message to Discord. Response status:", response.status_code)
else:
    print("No webhook URL found. Please check the environment variable setting.")
