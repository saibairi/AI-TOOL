from fastapi import APIRouter,HTTPException # type: ignore

from service.text_to_voice_service import text_to_voice_converter_service
from model.text_to_voice_model import TextRequest
from util.common_constants import logger

router = APIRouter()        

@router.post("/text-to-voice-converter")
async def text_to_voice_converter(payload: TextRequest):
    try:
        logger.info(f"text_to_voice_converter(), Request - {payload.text}")
        text = await text_to_voice_converter_service (payload.text)
        logger.info(f"text_to_voice_converter(), Response - {text}")
        return {"voice": text}
    except Exception as e:
        logger.error(f"text_to_voice_converter(), Error - {e}")
        raise HTTPException(status_code=500, detail=str(e).replace("'", ""))
