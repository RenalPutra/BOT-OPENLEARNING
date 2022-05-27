from pathlib import Path
from playsound import playsound
audio = Path().cwd() / "music/undertale.mp3"
for i in range(5):
    playsound(audio)