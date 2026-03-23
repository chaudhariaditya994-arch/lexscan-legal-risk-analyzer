from pydantic import BaseModel

class ClauseModel(BaseModel):
    title: str
    risk: str
    category: str