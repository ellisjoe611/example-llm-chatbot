from pydantic import BaseModel, Field


class QuestionBody(BaseModel):
    question: str = Field(description="Question to chatbot", max_length=200)
