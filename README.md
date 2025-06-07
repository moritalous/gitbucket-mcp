# GitBucket MCP Server (非公式)

このプロジェクトは、GitBucketのMCP(Model Context Protocol)サーバーの非公式実装です。FastMCPとOpenAPI仕様を使用して、GitBucketのAPIにアクセスし、リポジトリ、イシュー、プルリクエストなどの情報を取得・操作するためのツールを提供します。

## 概要

MCP(Model Context Protocol)は、アプリケーションがLLM（大規模言語モデル）にコンテキストを提供するための標準化されたプロトコルです。このサーバーは、GitBucketのOpenAPI仕様を基にFastMCPを使用して自動生成されており、LLMがGitBucketのリソースにアクセスできるようになります。

主な機能：
- リポジトリの一覧取得と詳細情報の取得
- イシューの作成、取得、コメント機能
- プルリクエストの作成、取得、更新機能

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
uv sync
```

## 設定方法

このサーバーを使用するには、以下の環境変数を設定する必要があります：

- `BASE_URL`: GitBucketサーバーのベースURL（例：`http://localhost:8080`）
- `GITBUCKET_API_KEY`: GitBucketのAPIキー

MCPクライアント（Claude Desktop等）の設定例：

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

## 利用可能なツール

現在、以下のAPIが利用可能です：

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

注意：OpenAPI仕様には他にも多くのAPIが定義されていますが、現在は上記のAPIのみが有効化されています。


## 制限事項

このMCPサーバーは非公式の実装であり、GitBucketの公式サポートを受けていません。

### 現在の制限

- OpenAPI仕様には多くのAPIが定義されていますが、以下の理由により多くのAPIがコメントアウトされています：
  - 一部のAPIで必要なエンドポイントが不足している
  - リクエストボディのネストが深すぎてツール読み込みでエラーが発生する
  - 動作しないAPIが存在する

- 現在有効化されているのは、基本的なリポジトリ、イシュー、プルリクエストの操作のみです

- GitBucketのAPIに変更があった場合、このサーバーも更新が必要になる可能性があります

## ライセンス

このプロジェクトは[Apache License 2.0](LICENSE)の下で公開されています。

## 貢献方法

バグ報告や機能リクエストは、GitHubのIssueを通じてお願いします。プルリクエストも歓迎します。

## 謝辞

このプロジェクトの開発にあたり、以下のプロジェクトに大変感謝しております：

- [GitBucket](https://github.com/gitbucket/gitbucket) - オープンソースのGitプラットフォーム
- [FastMCP](https://github.com/jlowin/fastmcp) - MCPサーバーの高速実装フレームワーク
- [Model Context Protocol](https://modelcontextprotocol.github.io/) - LLMとアプリケーション間の標準プロトコル

