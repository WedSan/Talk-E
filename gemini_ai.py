from generative_ai import GenerativeArtificialInteligence
import requests
import os
import google.generativeai as genai
class Gemini(GenerativeArtificialInteligence):

    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url
        self.chatHistory = [{"role": "model", "parts": ["Toda vez que for escrever uma frase ou palavra em inglês coloque ela dentro dessa tag XML <lang xml:lang='en-US'><break time='100ms'/>PALAVRA OU TEXTO INGLÊS AQUI DENTRO.</lang> quando for português use <lang xml:lang='pt-BR'>PALAVRA OU TEXTO EM PORTUGUÊS AQUI DENTRO.</lang> , todas as palavras que você escrever, escreva como se fosse você falando diretamente com uma outra pessoa, não como se fosse texto mas sim fala. Evite usar caracteres especiais como *, -, (),use apenas textos e numeros mas jamais algo que saia disso. Seja curto nas explicações. Quando for explicar algo fale algo como por exemplo, para dizer eu gosto de batata em ingles se diz: <lang xml:lang='en-US'>i like potatoes.</lang> Sempre no final de cada resposta (se o usuário fizer uma pergunta) pergunte para o usuário se ele tem mais algumda duvida. Nunca traduza alguma frase diretamente, sempre diga a tradução em ingles ou portugues de uma tal palavra é blablabla, okay?"]},]

    def generate_response(self, message: str) -> str:
        header = {
            "Content-type": "application/json"
        }
        
        payload = {
            "contents": [
                {
                    "role": "model",
                    "parts": [
                        {
                            "text": " Toda vez que for escrever uma frase ou palavra em inglês coloque ela dentro dessa tag XML <lang xml:lang='en-US'>PALAVRA OU TEXTO INGLÊS AQUI DENTRO</lang> quando for português use <lang xml:lang='pt-BR'>PALAVRA OU TEXTO EM PORTUGUÊS AQUI DENTRO</lang> , todas as palavras que você escrever, escreva como se fosse você falando diretamente com uma outra pessoa, não como se fosse texto mas sim fala. Não crie respostas muito grandes"
                        }
                    ]
                },
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": message
                        }
                    ]
                }
            ]
        }

        url_with_api_key = self.api_url + f"?key={self.api_key}"
        print(url_with_api_key)
        try:
            response = requests.post(url_with_api_key, headers=header, json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to make the request. Error: {e}")
        response_formated = response.json()['candidates'][0]['content']['parts'][0]['text'].replace("*", "")
        return response_formated

    