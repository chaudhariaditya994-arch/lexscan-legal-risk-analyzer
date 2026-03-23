import anthropic
import os
from fastapi import HTTPException

client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

async def analyze_pdf(base64_pdf: str) -> dict:
    system_prompt = "You are a senior legal risk analyst. Identify 6-15 clauses. Use web_search for unfamiliar legal terms. Always call analyze_legal_document with your complete analysis."

    tools = [
        {
            "name": "analyze_legal_document",
            "description": "Analyze a legal document for risky clauses",
            "input_schema": {
                "type": "object",
                "properties": {
                    "clauses": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "risk": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
                                "explanation": {"type": "string"},
                                "recommendation": {"type": "string"}
                            },
                            "required": ["title", "risk", "explanation", "recommendation"]
                        }
                    },
                    "overallRisk": {"type": "string"}
                },
                "required": ["clauses", "overallRisk"]
            }
        },
        {
            "name": "web_search_20250305",
            "description": "Search the web for information",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    ]

    response = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Analyze this PDF document: data:application/pdf;base64,{base64_pdf}"
            }
        ],
        tools=tools,
        tool_choice={"type": "tool", "name": "analyze_legal_document"}
    )

    for content in response.content:
        if content.type == "tool_use" and content.name == "analyze_legal_document":
            return content.input

    raise HTTPException(status_code=500, detail="No tool_use block found")