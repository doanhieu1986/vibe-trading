"""Web search tool: search the web via DuckDuckGo (free, no API key)."""

from __future__ import annotations

import json
import os
from typing import Any

from src.agent.tools import BaseTool
from src.security.scanner import with_security_warnings

_DEFAULT_REGION = "vn-vi" if os.getenv("AGENT_LANGUAGE", "").strip().lower() == "vi" else "wt-wt"

_VN_SOURCES = "cafef.vn OR vietstock.vn OR ndh.vn OR vneconomy.vn OR tinnhanhchungkhoan.vn OR fireant.vn OR hsx.vn OR hnx.vn"


class WebSearchTool(BaseTool):
    """Search the web via DuckDuckGo and return top results."""

    name = "web_search"

    @classmethod
    def check_available(cls) -> bool:
        """Available only if ddgs or duckduckgo_search is installed."""
        try:
            try:
                import ddgs  # noqa: F401
            except ImportError:
                import duckduckgo_search  # noqa: F401
            return True
        except ImportError:
            return False
    description = (
        "Search the web via DuckDuckGo. Returns top results with title, URL, and snippet. "
        + (
            "QUAN TRỌNG: Luôn ưu tiên tìm kiếm trên các trang tin tức Việt Nam. "
            f"Thêm 'site:{_VN_SOURCES}' vào query khi tìm tin tức thị trường VN. "
            "Ví dụ: query='VN-Index tuần này site:cafef.vn OR site:vietstock.vn'. "
            "Region mặc định đã là 'vn-vi' (kết quả tiếng Việt). "
            if _DEFAULT_REGION == "vn-vi" else
            "Use this to find information, news, or URLs before reading them with read_url. "
        )
    )
    parameters = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "Search query. Khi tìm tin tức VN: thêm 'site:cafef.vn OR site:vietstock.vn OR site:ndh.vn' để ưu tiên nguồn Việt Nam."
                    if _DEFAULT_REGION == "vn-vi" else
                    "Search query"
                ),
            },
            "max_results": {
                "type": "integer",
                "description": "Maximum number of results to return (default 5, max 10)",
                "default": 5,
            },
            "region": {
                "type": "string",
                "description": f"DuckDuckGo region code (default '{_DEFAULT_REGION}'). Use 'vn-vi' for Vietnam, 'us-en' for US.",
                "default": _DEFAULT_REGION,
            },
        },
        "required": ["query"],
    }
    repeatable = True

    def execute(self, **kwargs: Any) -> str:
        """Run a DuckDuckGo search.

        Args:
            **kwargs: Must include query; optionally max_results.

        Returns:
            JSON with search results or error.
        """
        query = kwargs["query"]
        max_results = min(int(kwargs.get("max_results", 5)), 10)
        region = kwargs.get("region", _DEFAULT_REGION)

        try:
            try:
                from ddgs import DDGS
            except ImportError:
                from duckduckgo_search import DDGS

            with DDGS() as ddgs:
                raw = list(ddgs.text(query, region=region, max_results=max_results))

            results = [
                {
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "snippet": r.get("body", ""),
                }
                for r in raw
            ]
            payload = {"status": "ok", "query": query, "results": results}
            payload = with_security_warnings(
                payload,
                fields=("results.*.title", "results.*.snippet"),
            )
            return json.dumps(payload, ensure_ascii=False)
        except ImportError:
            return json.dumps(
                {
                    "status": "error",
                    "error": "DuckDuckGo search package not installed. Run: pip install ddgs",
                },
                ensure_ascii=False,
            )
        except Exception as exc:
            return json.dumps(
                {"status": "error", "error": str(exc)},
                ensure_ascii=False,
            )
