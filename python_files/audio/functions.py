
from sounddevice import InputStream
from scipy.io.wavfile import write
from pydub import AudioSegment
import speech_recognition as sr
from numpy import concatenate
from keyboard import is_pressed
    
def recording(file_name: str) -> None:
    
    def audio_callback(indata, frames, time, status):
        if status:
            print(f"Error: {status}")
        recording.append(indata.copy())
    
    fs = 16_000
    channels = 1
    recording = [] 
    print("Recording... Press 'q' to stop.")

    try:
        with InputStream(samplerate=fs, channels=channels, callback=audio_callback):
            while True:
                if is_pressed('q'):
                    print("\nRecording stopped.")
                    break

    except KeyboardInterrupt:
        print("\nRecording interrupted.")

    finally:
        recorded_audio = concatenate(recording, axis=0)
        write(file_name, fs, recorded_audio)
        print(f"Recording saved as {file_name}.")


def voice_to_string(file_name: str) -> str:

    audio = AudioSegment.from_file(file_name, format="wav")
    new_file_name = "_pcm.".join(file_name.split("."))
    audio.export(new_file_name, format="wav", parameters=["-acodec", "pcm_s16le"])
    print("File converted to PCM format.")

    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(new_file_name)

    with audio_file as source:
        audio = recognizer.record(source=source)
        text = recognizer.recognize_google(audio, language='es-PE')
        print(text)
    
    return text



if __name__ == "__main__":
    file_name = 'output.wav'
    recording(file_name=file_name)
    text = voice_to_string(file_name=file_name)

