import json
import os

import httpx
from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from fastmcp.server.openapi import MCPType, RouteMap

# Get required environment variables
BASE_URL = os.getenv("BASE_URL")
GITBUCKET_API_KEY = os.getenv("GITBUCKET_API_KEY")

# Check if required environment variables are set
if not BASE_URL:
    raise ToolError("BASE_URL environment variable is not set")

if not GITBUCKET_API_KEY:
    raise ToolError("GITBUCKET_API_KEY environment variable is not set")


client = httpx.AsyncClient(
    base_url=BASE_URL,
    headers={"Authorization": f"token {GITBUCKET_API_KEY}"},
)

with open("openapi.json", "r") as f:
    openapi_spec = json.load(f)

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="GitBucket MCP Server",
    route_maps=[
        # RouteMap(
        #     methods=["*"],
        #     pattern=r".*",
        #     mcp_type=MCPType.TOOL,
        # ),  # 全てをToolとして定義
        RouteMap(
            methods=["GET"], pattern="^/api/v3/repositories$", mcp_type=MCPType.TOOL
        ),  # /api/v3/repositories
        RouteMap(
            methods=["GET"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}
        RouteMap(
            methods=["GET", "POST"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/issues$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/issues
        RouteMap(
            methods=["GET"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/issues\/[^\/]+$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/issues/{issue_id}
        RouteMap(
            methods=["GET", "POST"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/issues\/[^\/]+\/comments$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/issues/{issue_id}/comments
        RouteMap(
            methods=["GET", "POST"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/pulls$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/pulls
        RouteMap(
            methods=["GET", "PATCH"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/pulls\/[^\/]+$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/pulls/{pull_number}
        RouteMap(
            methods=["GET"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/pulls\/[^\/]+\/commits$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/pulls/{pull_number}/commits
        RouteMap(
            methods=["GET", "PUT"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/pulls\/[^\/]+\/merge$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/pulls/{pull_number}/merge
        RouteMap(
            methods=["GET"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/branches$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/branches
        RouteMap(
            methods=["GET"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/branches\/[^\/]+$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/branches/{branch}
        RouteMap(
            methods=["GET"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/commits$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/commits
        RouteMap(
            methods=["GET"],
            pattern=r"^\/api\/v3\/repos\/[^\/]+\/[^\/]+\/commits\/[^\/]+$",
            mcp_type=MCPType.TOOL,
        ),  # /api/v3/repos/{owner}/{repository}/commits/{sha}
        RouteMap(
            methods=["DELETE", "POST", "PUT", "PATCH"],
            pattern=r".*",
            mcp_type=MCPType.EXCLUDE,
        ),  # その他を除外
    ],
)

if __name__ == "__main__":
    mcp.run()
