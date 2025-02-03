from openai import OpenAI
from functions import recording
import sys
from datetime import datetime as dt

if len(sys.argv) > 1 and sys.argv[1] == 'w':
    uprofile    = 'c:\\Users\\sgast\\wolfram\\log\\'
    prompt      = 'Hi, I am logging work here, please keep the message on English, even if I use some words on Spanish. Correct any mistake made, thank you.' 
else:
    uprofile    = 'c:\\Users\\sgast\\log\\'
    prompt      = 'Hola, estoy registrando mi día tranquilamente, no tienes que arreglar mucho, intenta captar la escencia de las muletillas y algunas frases para darle humanidad a la grabación.' 

print("logging work/day on ", uprofile)

file = "output.wav"
recording(file_name=file)

client = OpenAI()

with open(file, "rb") as f:
    transcription = client.audio.transcriptions.create(model="whisper-1", file=f, prompt=prompt)

log_file_path = uprofile + dt.now().strftime('%a %d %b %Y -- %I.%M%p')+'.txt'

with open(log_file_path, 'w') as f:
    print("Transcripted text")
    print(transcription.text)
    f.write(transcription.text)


