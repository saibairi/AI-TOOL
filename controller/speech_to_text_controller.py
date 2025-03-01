from fastapi import APIRouter,HTTPException # type: ignore

from model.speech_to_text_model import SpeechRequest
from service.speech_to_text_service import speech_to_text_converter_service
from util.common_constants import logger

router = APIRouter()        

@router.post("/speech-to-text-converter")
async def speech_to_text_converter(payload: SpeechRequest):
    try:
        logger.info(f"speech_to_text_converter(), Request - {payload.speech}")
        text = await speech_to_text_converter_service(payload.speech)
        logger.info(f"speech_to_text_converter(), Response - {text}")
        return {"text": text}
    except Exception as e:
        logger.error(f"speech_to_text_converter(), Error - {e}")
        raise HTTPException(status_code=500, detail=str(e).replace("'", ""))
