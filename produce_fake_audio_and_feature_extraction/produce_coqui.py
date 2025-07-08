
"""
ChatGPT chat histories that helped me
https://chatgpt.com/share/686a77e1-1ce0-8005-8e59-1ed5d25073d9
https://chatgpt.com/share/686a7800-9030-8005-aa52-17f7fc0a827a
"""


import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

with open("texts.txt", "r") as file:
  for idx, line in enumerate(file):
    
    # TTS to a file, use a preset speaker
    tts.tts_to_file(
      text=line,
      speaker="Asya Anara",
      language="tr",
      file_path=f"asya_{idx}.wav"
    )
