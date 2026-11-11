# This script use for Text to audio
import os
import requests
import numpy as np
import sounddevice as sd

myinput = "Hello rashmi billore kya kha rahi ho. tumhari shugar kesi he or BP kesa he, apani tabiyat ka khyal rakho."
response = requests.post(
  url="https://openrouter.ai/api/v1/audio/speech",
  headers={
    "Authorization": "Bearer <Your API Key>",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  json={
  "model": "fish-audio/s2.1-pro-free:free",
  "input": myinput,
  "voice": "b347db033a6549378b48d00acb0d06cd",
  "response_format": "mp3"
}
# # #   json={
# # #   "model": "heygen/heygen-voice-1-turbo:free",
# # #   "input": myinput,
# # #   "voice": "nadine",
# # #   "response_format": "pcm"
# # # }
)

with open("output.mp3", "wb") as f:
  f.write(response.content)
print(f"Audio saved. Generation ID: {response.headers.get('X-Generation-Id')}")
#-----------------------------------------------------------------------
# # # pcm_file = r"output.pcm"

# # # with open(pcm_file, "rb") as f:
# # #     pcm_data = f.read()

# # # # Assuming 16-bit signed PCM
# # # audio = np.frombuffer(pcm_data, dtype=np.int16)

# # # sd.play(audio, samplerate=40000)
# # # sd.wait()
#-----------------------------------------------------------------------
mp3_file = r"output.mp3"
os.startfile(mp3_file)


