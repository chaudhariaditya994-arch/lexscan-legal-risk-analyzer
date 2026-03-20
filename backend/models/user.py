from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    userId: str = Field(..., description="Client side or OAuth derived user id")
    email: EmailStr
    name: str
    plan: str = Field(default="free", pattern="^(free|pro)$")
