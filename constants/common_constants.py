AUDIO_SEGMENT_CONVERTER_PATH = r"C:\Users\anush\Downloads\ffmpeg-2025-01-05-git-19c95ecbff-full_build\ffmpeg-2025-01-05-git-19c95ecbff-full_build\bin\ffmpeg.exe"
AUDIO_SEGMENT_FFPROBE_PATH = r"C:\Users\anush\Downloads\ffmpeg-2025-01-05-git-19c95ecbff-full_build\ffmpeg-2025-01-05-git-19c95ecbff-full_build\bin\ffprobe.exe"

# AUDIO_SEGMENT_CONVERTER_PATH = r"path_to_ffmpeg"
# AUDIO_SEGMENT_FFPROBE_PATH = r"path_to_ffprobe"

"""
steps for windows
step-1: Download ffmpef from : https://www.gyan.dev/ffmpeg/builds/
step-2: Extract downloaded files
step-3: Add bin path in system varablies
step-4: update respective paths in constants file

steps for Linux/ubuntu
step-1: Download using "sudo apt install ffmpeg" command
step-2: verify the download status by checking versions 
        ffmpeg -version
        ffprobe -version
step-3: search for paths using below commands
        which ffmpeg
        which ffprobe
step-4: update respective paths in constants file
"""


TEMP_FILE_PATH = "C:/Users/anush/Documents/saikiran/fast-api/AI-TOOL/util/temp/{}.wav"