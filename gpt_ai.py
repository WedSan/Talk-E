from generative_ai import GenerativeArtificialInteligence
import requests
import os

class GPT(GenerativeArtificialInteligence):
    
    def __init__(self, api_key: str, endpoint_url: str) -> None:
        self._api_key = api_key
        self._endpoint_url = endpoint_url

    def generate_response(self, message: str) -> str:

        headers = {
            "Content-Type": "application/json",
            "api-key": self._api_key,
        }

        # Payload for the request
        payload = {
        "messages": [
            {
            "role": "user",
            "content": message
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
        }

        # Send request
        try:
            response = requests.post(self._endpoint_url, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        except requests.RequestException as e:
            raise SystemExit(f"Failed to make the request. Error: {e}")
        
        #return response content
        message_response = response.json()['choices'][0]['message']['content']
        return message_response

### Usage Example
generative_ai = GPT(os.environ["GENERATIVE_AI_KEY"], os.environ["GENERATIVE_AI_ENDPOINT"])
print(generative_ai.generate_response("Como posso dizer que gosto de comer bolo em inglês?"))