import openai
import os
from dotenv import load_dotenv
import speech_recognition as sr

load_dotenv()

api_key = os.getenv("CHATGPT_KEY")

# openai.api_key = api_key

# print(sr.Microphone().list_microphone_names())

rec = sr.Recognizer()

texto = ''

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Comece a falar!")
    audio = rec.listen(mic)

try:
    texto = rec.recognize_google(audio, language = "pt-BR")
    print(f"Obrigado por falar: {texto}")
    
except sr.UnknownValueError:
    print("não entendi")