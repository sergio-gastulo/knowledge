from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl
from functions import recording, voice_to_string

session = WolframLanguageSession(kernel='C:\\Program Files\\Wolfram Research\\Wolfram\\14.1\\WolframKernel.exe')

file = "output.wav"
recording(file_name=file)
text = voice_to_string(file_name=file)

prompt = f"""
Toma el siguiente texto transcrito de voz en español, corrígelo para que tenga puntuación adecuada (puntos, comas, signos de exclamación o interrogación, etc.), infiere cortes de párrafo donde sea necesario y arregla palabras que no tienen sentido usando el contexto de las 10 a 11 palabras más cercanas. También, agrega palabras pequeñas que puedan estar ausentes, como preposiciones, para que las frases tengan fluidez natural. Si encuentras términos en inglés que parecen incorrectos según el contexto, reemplázalos por la palabra más adecuada en inglés o español según corresponda. Mantén el estilo casual, como si fuera una narración relajada del día.

Aquí está el texto original:
{text}.

Devuélveme el texto corregido con los cambios aplicados
"""

transformed_text = session.evaluate(wl.Quiet(wl.LLMSynthesize(prompt)))
print(f'The transformed text is {transformed_text}')
session.terminate()





