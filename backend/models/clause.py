from pydantic import BaseModel, Field


class Clause(BaseModel):
    title: str = Field(..., description="Short name for the risky clause")
    category: str = Field(..., description="Clause category such as termination or arbitration")
    risk: str = Field(..., pattern="^(HIGH|MEDIUM|LOW)$")
    score: int = Field(..., ge=0, le=100)
    clauseText: str = Field(..., description="Quoted or paraphrased clause text")
    explanation: str = Field(..., description="Plain English explanation of the risk")
    recommendation: str = Field(..., description="Negotiation suggestion or action item")
