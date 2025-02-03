from openai import OpenAI
from functions import recording
import sys
from datetime import datetime as dt

if len(sys.argv) > 1 and sys.argv[1] == 'w':
    uprofile = 'c:\\Users\\sgast\\wolfram\\log\\'
else:
    uprofile = 'c:\\Users\\sgast\\log\\'

print("logging work/day on ", uprofile)

file = "output.wav"
recording(file_name=file)

client = OpenAI()

with open(file, "rb") as f:
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=f,
        prompt="Este audio es sobre mí registrando mi día a día en casa y en la compañía. Siempre ten en cuenta que vivo en Perú."
        )

log_file_path = uprofile + dt.now().strftime('%a %d %b %Y -- %I.%M%p')+'.txt'

with open(log_file_path, 'w') as f:
    print("texto transcrito:")
    print(transcription.text)
    f.write(transcription.text)


