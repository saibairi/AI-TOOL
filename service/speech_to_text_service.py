import base64
from io import BytesIO
import speech_recognition as sr # type: ignore
from pydub import AudioSegment # type: ignore

from constants.common_constants import *

async def speech_to_text_converter_service(speech_base64: str) -> str:
    try:
        # Decode base64 audio
        audio_data = base64.b64decode(speech_base64)
        audio_file = BytesIO(audio_data)

        # Manually set paths to ffmpeg and ffprobe
        AudioSegment.converter = AUDIO_SEGMENT_CONVERTER_PATH
        AudioSegment.ffprobe = AUDIO_SEGMENT_FFPROBE_PATH

        # Convert audio to WAV (if needed, using pydub)
        audio = AudioSegment.from_file(audio_file)
        wav_file = BytesIO()
        audio.export(wav_file, format='wav')
        wav_file.seek(0)

        # Transcribe audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
            audio_content = recognizer.record(source)
            text = recognizer.recognize_google(audio_content)

        return text
    except Exception as e:
        raise Exception(f"Error processing speech: {str(e)}")
