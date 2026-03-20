from __future__ import annotations

import os
from typing import Any

from anthropic import AsyncAnthropic
from fastapi import HTTPException

from models.analysis import AnalysisResult


SYSTEM_PROMPT = "You are a senior legal risk analyst. Identify 6-15 clauses. Use web_search for unfamiliar legal terms. Always call analyze_legal_document with your complete analysis."
MODEL_NAME = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")

ANALYZE_LEGAL_DOCUMENT_TOOL: dict[str, Any] = {
    "name": "analyze_legal_document",
    "description": "Return complete structured legal risk analysis for the uploaded contract.",
    "input_schema": AnalysisResult.model_json_schema(),
}

WEB_SEARCH_TOOL: dict[str, Any] = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 3,
}


async def analyze_pdf(base64_pdf: str) -> dict[str, Any]:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="ANTHROPIC_API_KEY is not configured.")

    client = AsyncAnthropic(api_key=api_key)
    response = await client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        tools=[ANALYZE_LEGAL_DOCUMENT_TOOL, WEB_SEARCH_TOOL],
        tool_choice={"type": "tool", "name": "analyze_legal_document"},
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": base64_pdf,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Analyze the attached legal document and return your full findings through the analyze_legal_document tool.",
                    },
                ],
            }
        ],
    )

    for block in response.content:
        if getattr(block, "type", None) == "tool_use" and getattr(block, "name", None) == "analyze_legal_document":
            return dict(block.input)

    raise HTTPException(status_code=500, detail="Claude did not return an analyze_legal_document tool_use block.")
