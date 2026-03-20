from typing import List

from pydantic import BaseModel, Field

from models.clause import Clause


class AnalysisResult(BaseModel):
    documentTitle: str
    documentType: str
    overallRisk: str = Field(..., pattern="^(HIGH|MEDIUM|LOW)$")
    overallRiskScore: int = Field(..., ge=0, le=100)
    executiveSummary: str
    negotiationSummary: str
    searchedLegalTerms: List[str] = Field(default_factory=list)
    clauses: List[Clause] = Field(default_factory=list, min_length=6, max_length=15)


class StoredAnalysis(AnalysisResult):
    id: str
    userId: str
    pdfHash: str
    cached: bool = False
    processingTimeMs: int = 0
