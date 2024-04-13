import requests

def get_latest_release(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        release_data = response.json()
        release_name = release_data['name']
        release_url = release_data['html_url']

        print(f"Latest release for {repo}: {release_name}")
        print(f"Release details: {release_url}")
    else:
        print(f"Failed to fetch release data for {user}/{repo}. Status code: {response.status_code}")


# リポジトリのリストを定義
repositories = [
    ("timlrx", "tailwind-nextjs-starter-blog"),
    ("usememos", "memos"),
    # 他のリポジトリを追加する場合は、このリストにタプルとして追加します
]

# 各リポジトリの最新リリース情報を取得して表示
for user, repo in repositories:
    get_latest_release(user, repo)
