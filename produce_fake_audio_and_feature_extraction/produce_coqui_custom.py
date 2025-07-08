"""
ChatGPT chat histories that helped me
https://chatgpt.com/share/686a77e1-1ce0-8005-8e59-1ed5d25073d9
https://chatgpt.com/share/686a7800-9030-8005-aa52-17f7fc0a827a
"""


import torch
from TTS.api import TTS
import os

REAL_AUDIOS_PATH = "celebrity_real_audios"

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

custom_voices = [f for f in os.listdir(REAL_AUDIOS_PATH) if os.path.isfile(os.path.join(REAL_AUDIOS_PATH, f))]

with open("texts.txt", "r") as f:
        lines = f.readlines()
        
        for cv_idx, cv in enumerate(custom_voices):
            
            for counter in range(2000):
                 
                tts.tts_to_file(
                text=lines[cv_idx * 2000 + counter],
                speaker_wav=f"{REAL_AUDIOS_PATH}/{cv}",
                language="tr",
                file_path=f"{os.path.splitext(cv)[0]}_{counter}.wav"
                )
        


    
    
