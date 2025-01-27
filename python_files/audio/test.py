#%%
import speech_recognition as sr

file_name = 'output_pcm.wav'

r = sr.Recognizer()
audio_file = sr.AudioFile(file_name)

langs = ['es-PE','en-US']

with audio_file as source:
    audio = r.record(source)
    prob = {lang: r.recognize_google(audio, language=lang, show_all=True) for lang in langs}


# %%
with sr.Microphone() as source:
    while True:
        try: 
            new_audio = r.listen(source)
            new_text = r.recognize_google(new_audio, language='es-PE')
            print('\ncut\n')
            print(new_text)
        except KeyboardInterrupt:
            print('Keyboard has interrupted the recording.')
            break
        except:
            print('Unknown error, but we will continue') 


#%%

import os; dir(os)
