from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

from controller import speech_to_text_controller
from controller import text_to_voice_controller
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific domains for better security
    allow_credentials=True,
    allow_methods=["*"],  # Specify allowed methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # Specify allowed headers
)

app.include_router(speech_to_text_controller.router)
app.include_router(text_to_voice_controller.router)