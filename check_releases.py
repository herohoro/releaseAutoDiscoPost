import requests
import os
from datetime import datetime, timedelta, timezone

def send_to_discord(content, webhook_url):
    print(f"{datetime.now(timezone.utc)}: Webhook URL in send_to_discord:", webhook_url)
    if not webhook_url:
        print("Error: The Discord webhook URL is not set.")
        return
    data = {
        "content": content,
        "username": "GitHub Release Notifier"
    }
    try:
        response = requests.post(webhook_url, json=data)
        print(f"Discord response: {response.status_code}, {response.reason}")
    except Exception as e:
        print(f"Error sending message to Discord: {e}")

def get_latest_release(user, repo, webhook_url):
    print(f"{datetime.now(timezone.utc)}: Webhook URL in get_latest_release:", webhook_url)
    url = f"https://api.github.com/repos/{user}/{repo}/releases/latest"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            release_data = response.json()
            release_name = release_data['name']
            release_url = release_data['html_url']
            published_at = datetime.strptime(release_data['published_at'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)
            
            if now - published_at < timedelta(days=1):
                message = f"Latest release for {repo}: {release_name}\nRelease details: {release_url}\nPublished at: {published_at}"
                send_to_discord(message, webhook_url)
            else:
                print(f"No new release within the last 24 hours for {repo}.")
        else:
            print(f"Failed to fetch release data for {user}/{repo}. Status code: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error fetching release data: {e}")

# Repositories and their corresponding Discord webhooks
repositories = [
    ("yaseenmustapha", "nextjs13-app", os.getenv('DISCORD_WEBHOOK_JOUHOUYASAMPLE')),
    ("timlrx", "tailwind-nextjs-starter-blog", os.getenv('DISCORD_WEBHOOK_YUBINKYOKU')),
    ("usememos", "memos", os.getenv('DISCORD_WEBHOOK_YUBINKYOKU'))
]

for user, repo, webhook_url in repositories:
    get_latest_release(user, repo, webhook_url)
