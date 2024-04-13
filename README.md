

## 機能

気になるリポを登録しておくとリリース情報の更新があった場合に、discordへ自動投稿される

### リポの登録

[check_releases.py内のrepositories変数](https://github.com/herohoro/releaseAutoDiscoPost/blob/fbdb205fcb50dffb8c764f81b0bd8d69b2cc8d7d/check_releases.py#L33-L36)へ追記する


### 環境変数の設定

※ discordのWebhook機能は管理者からの権限(ウェブフックの管理)を付与されていないと設置できなくなっています。

1. Settingsタブをクリック:
    - リポジトリページの上部にあるナビゲーションバーで「Settings」（設定）をクリック
2. 左サイドバーからSecretsを選択:
    - Settingsページの左側にあるサイドバーで「Secrets and Variables」セクションを見つけ、「Actions」をクリック
4. **New repository secretをクリック**:
    - 「New repository secret」ボタンをクリックして新しいシークレットを作成します。
5. **シークレットの詳細を入力**:
    - **Name**: DISCORD_WEBHOOK_URL
    - **Value**: DiscordのWebhook URL
6. **Add secretをクリック**:
    - 入力が完了したら、「Add secret」ボタンをクリックして保存



> [!NOTE]
> GitHub Actionや環境変数の詳しい設定方法は、過去にherohoroブログにまとめているので、参照してください。
> https://herohoro.com/blog/notion-rss-reader

