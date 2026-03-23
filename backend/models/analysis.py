from pydantic import BaseModel
from typing import List

class Clause(BaseModel):
    title: str
    risk: str
    explanation: str
    recommendation: str

class AnalysisResult(BaseModel):
    clauses: List[Clause]
    overallRisk: str