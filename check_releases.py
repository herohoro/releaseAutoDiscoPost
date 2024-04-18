import requests
import os
from datetime import datetime, timedelta

def send_to_discord(content, webhook_url):
    if not webhook_url:
        print("Error: The Discord webhook URL is not set.")
        return
    data = {
        "content": content,
        "username": "GitHub Release Notifier"
    }
    response = requests.post(webhook_url, json=data)
    print(f"Discord response: {response.status_code}, {response.reason}")

def get_latest_release(user, repo, webhook_url):
    url = f"https://api.github.com/repos/{user}/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        release_data = response.json()
        release_name = release_data['name']
        release_url = release_data['html_url']
        published_at = datetime.strptime(release_data['published_at'], "%Y-%m-%dT%H:%M:%SZ")
        now = datetime.utcnow()
        
        if now - published_at < timedelta(days=1):
            message = f"Latest release for {repo}: {release_name}\nRelease details: {release_url}\nPublished at: {published_at}"
            send_to_discord(message, webhook_url)
        else:
            print(f"No new release within the last 24 hours for {repo}.")
    else:
        print(f"Failed to fetch release data for {user}/{repo}. Status code: {response.status_code}")

# 環境変数の取得
webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
print("Webhook URL at main level:", webhook_url)  # デバッグ出力

repositories = [("timlrx", "tailwind-nextjs-starter-blog"), ("usememos", "memos")]
for user, repo in repositories:
    get_latest_release(user, repo, webhook_url)
