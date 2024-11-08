import openai
import os
from dotenv import load_dotenv
import speech_recognition as sr

def capitarAudio():
    rec = sr.Recognizer()
    textoCompleto = ''

    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Comece a falar!")
        while True:
            audio = rec.listen(mic, timeout=5, phrase_time_limit=5)

            try:
                texto = rec.recognize_google(audio, language = "pt-BR")
                print(f'Você acabou de falar {texto}')
                textoCompleto += " " + texto   
                 
                if 'fim' in texto.lower():
                    textoCompleto = textoCompleto.replace('encerrar', '')
                    print('Gravação encerrada')
                    break
                
            except sr.UnknownValueError:
                print("não entendi. repete fi")

    print(f"Tudo que voccê falou: {textoCompleto}")
    return textoCompleto

def ChatGPT():
    load_dotenv()

    api_key = os.getenv("CHATGPT_KEY")

    openai.api_key = api_key

    messages = [
        {"role": "system", "content": "Você é um importante assistente"}
    ]

    comando = capitarAudio()

    messages.append({"role": "user", "content": comando})

    while not "fim" in comando.lower():
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
            temperature = 1,
            max_tokens = 200
        )
        answer = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": answer})

        print(f"Resposta: {answer}")
        
        comando = capitarAudio()
        messages.append({"role": "user", "content": comando})

def main():
    capitarAudio()

if __name__ == "__main__":
    main()