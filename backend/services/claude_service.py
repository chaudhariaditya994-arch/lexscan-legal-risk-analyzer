import anthropic
from models.analysis import AnalysisResult

client = anthropic.Anthropic()

async def analyze_document(content: bytes) -> AnalysisResult:
    # call Claude with tool_use
    # placeholder
    return AnalysisResult(clauses=[], overallRisk="LOW")