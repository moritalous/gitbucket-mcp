# GitBucket MCP Server (非公式)

このプロジェクトは、GitBucketのMCP(Model Context Protocol)サーバーの非公式実装です。MCPを通じてGitBucketのAPIにアクセスし、リポジトリ、イシュー、プルリクエスト、コミット、ブランチなどの情報を取得・操作するためのツールを提供します。

## 概要

MCP(Model Context Protocol)は、アプリケーションがLLM（大規模言語モデル）にコンテキストを提供するための標準化されたプロトコルです。このサーバーを使用することで、LLMはGitBucketのリソースにアクセスし、GitHubフローに似た操作を行うことができます。

- GitBucketツールで、リポジトリの一覧を取得してください。
- GitBucketツールで、イシューを作成してください。
- GitBucketツールで、プルリクエストを作成してください。

## インストール方法

### 前提条件

- Python 3.10以上
- GitBucketサーバー（アクセス可能なもの）
- GitBucketのAPIキー

### インストール手順

1. リポジトリをクローンします：

```bash
git clone https://github.com/moritalous/gitbucket-mcp.git
cd gitbucket-mcp
```

2. 依存パッケージをインストールします：

```bash
uv sync -U
```

## 設定方法


```json
{
    "mcpServers": {
        "gitbucket": {
            "command": "uv",
            "args": [
                "run",
                "--directory",
                "Cloneしたgitbucket-mcpディレクトリのフルパス",
                "main.py"
            ],
            "env": {
                "BASE_URL": "http://localhost:8080/",
                "GITBUCKET_API_KEY": "YOUR_API_KEY"
            }
        }
    }
}
```

このサーバーを使用するには、以下の環境変数を設定する必要があります：

- `BASE_URL`: GitBucketサーバーのベースURL（例：`http://localhost:8080`）
- `GITBUCKET_API_KEY`: GitBucketのAPIキー

## ツール一覧

以下のツールを定義していますが、OpenAPI仕様に定義されているAPIから任意のAPIを有効化して使用することができます。

| メソッド | API | 内容 |
| --- | --- | --- |
| GET | /api/v3/repositories | リポジトリの一覧を取得 |
| GET | /api/v3/repos/{owner}/{repository} | 特定のリポジトリの情報を取得 |
| GET | /api/v3/repos/{owner}/{repository}/issues | リポジトリのイシュー一覧を取得 |
| POST | /api/v3/repos/{owner}/{repository}/issues | 新しいイシューを作成 |
| GET | /api/v3/repos/{owner}/{repository}/issues/{issue_id} | 特定のイシューの情報を取得 |
| GET | /api/v3/repos/{owner}/{repository}/issues/{issue_id}/comments | イシューのコメント一覧を取得 |
| POST | /api/v3/repos/{owner}/{repository}/issues/{issue_id}/comments | イシューにコメントを追加 |
| GET | /api/v3/repos/{owner}/{repository}/pulls | プルリクエスト一覧を取得 |
| POST | /api/v3/repos/{owner}/{repository}/pulls | 新しいプルリクエストを作成 |
| GET | /api/v3/repos/{owner}/{repository}/pulls/{pull_number} | 特定のプルリクエストの情報を取得 |
| PATCH | /api/v3/repos/{owner}/{repository}/pulls/{pull_number} | プルリクエストを更新 |
| GET | /api/v3/repos/{owner}/{repository}/pulls/{pull_number}/commits | プルリクエストのコミット一覧を取得 |
| GET | /api/v3/repos/{owner}/{repository}/pulls/{pull_number}/merge | プルリクエストのマージ状態を確認 |
| PUT | /api/v3/repos/{owner}/{repository}/pulls/{pull_number}/merge | プルリクエストをマージ |
| GET | /api/v3/repos/{owner}/{repository}/branches | ブランチ一覧を取得 |
| GET | /api/v3/repos/{owner}/{repository}/branches/{branch} | 特定のブランチの情報を取得 |
| GET | /api/v3/repos/{owner}/{repository}/commits | コミット一覧を取得 |
| GET | /api/v3/repos/{owner}/{repository}/commits/{sha} | 特定のコミットの情報を取得 |


## 制限事項

このMCPサーバーは非公式の実装であり、GitBucketの公式サポートを受けていません。GitBucketのAPIに変更があった場合、このサーバーも更新が必要になる可能性があります。

## ライセンス

このプロジェクトは[Apache License 2.0](LICENSE)の下で公開されています。

## 貢献方法

バグ報告や機能リクエストは、GitHubのIssueを通じてお願いします。プルリクエストも歓迎します。

## 謝辞

大変感謝しております。

- [GitBucket](https://github.com/gitbucket/gitbucket)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [Model Context Protocol](https://modelcontextprotocol.github.io/)

