import pyttsx3 # type: ignore
import base64
import time
import os

import constants.common_constants as constant

async def text_to_voice_converter_service(text: str):
    # file_name = constant.TEMP_FILE_PATH.format(str(time.time()))
    root_path = r"C:\Users\anush\Documents\saikiran\fast-api\AI-TOOL\util\temp"
    file_name = root_path + "/"+ (str(time.time())) +".wav"
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Set speech rate
        engine.setProperty('volume', 0.9)  # Set volume (0.0 to 1.0)

        # Save the audio output to the temporary file
        engine.save_to_file(text, file_name)
        engine.runAndWait()

        try:
            with open(file_name, "rb") as audio_file:
                audio_data = audio_file.read()

            # Encode the binary audio data to Base64
            base64_audio = base64.b64encode(audio_data).decode("utf-8")

        finally:
            # Clean up: Remove the temporary file
            if os.path.exists(file_name):
                os.remove(file_name)

        return base64_audio
    except Exception as e:
        raise Exception(f"Error processing speech: {str(e)}")
