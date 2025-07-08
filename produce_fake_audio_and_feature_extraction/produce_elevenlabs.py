"""
ChatGPT chat histories that helped me
https://chatgpt.com/share/686a77e1-1ce0-8005-8e59-1ed5d25073d9
https://chatgpt.com/share/686a7800-9030-8005-aa52-17f7fc0a827a
"""


import requests

API_KEY = 'sk_dfa240010aa268c9a1b0f482e3862245db2c9bdb62b66a5b'
VOICE_ID = 'IuRRIAcbQK5AQk1XevPj'

url = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}'

headers = {
    'xi-api-key': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'audio/mpeg'
}

with open("texts_elevenlabs.txt", "r") as file:
    for idx, line in enumerate(file):
        

        data = {
            'text': line,
            'model_id': 'eleven_multilingual_v2', 
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            with open(f"audios_elevenlabs/doga_{idx}.mp3", 'wb') as f:
                f.write(response.content)
            print(f'Audio saved to audios_elevenlabs/doga_{idx}.mp3')
        else:
            print(f'Error: {response.status_code} - {response.text}')
