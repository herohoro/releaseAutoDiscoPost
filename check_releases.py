import requests
import json
import os  # 環境変数にアクセスするために必要
from datetime import datetime, timedelta

def send_to_discord(content, webhook_url):
    if not webhook_url:
        print("Error: The Discord webhook URL is not set.")
        return  # URLがNoneの場合、早期に関数から抜ける
    data = {
        "content": content,
        "username": "GitHub Release Notifier"
    }
    response = requests.post(webhook_url, json=data)
    print(f"Discord response: {response.status_code}, {response.reason}")

def get_latest_release(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        release_data = response.json()
        release_name = release_data['name']
        release_url = release_data['html_url']
        published_at = datetime.strptime(release_data['published_at'], "%Y-%m-%dT%H:%M:%SZ")
        now = datetime.utcnow()
        
        if now - published_at < timedelta(days=1):  # 24時間以内に公開された場合
            message = f"Latest release for {repo}: {release_name}\nRelease details: {release_url}\nPublished at: {published_at}"
            send_to_discord(message, os.getenv('DISCORD_WEBHOOK_URL'))
        else:
            print(f"No new release within the last 24 hours for {repo}.")
    else:
        print(f"Failed to fetch release data for {user}/{repo}. Status code: {response.status_code}")

# リポジトリのリストを定義
repositories = [
    ("timlrx", "tailwind-nextjs-starter-blog"),
    ("usememos", "memos"),
    # 他のリポジトリを追加する場合は、このリストにタプルとして追加します
]

# 各リポジトリの最新リリース情報を取得してDiscordに投稿
for user, repo in repositories:
    get_latest_release(user, repo)
