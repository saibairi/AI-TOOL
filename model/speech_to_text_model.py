from pydantic import BaseModel

class SpeechRequest(BaseModel):
    speech: str