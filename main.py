from index import recognize_from_microphone
from gpt_ai import GPT
from text_to_Speech import azure_speak
from generative_ai import GenerativeArtificialInteligence
import os

text_recognized: str = recognize_from_microphone()

generative_ai: GenerativeArtificialInteligence = GPT(os.environ["GENERATIVE_AI_KEY"], os.environ["GENERATIVE_AI_ENDPOINT"])
response_from_ai: str = generative_ai.generate_response(text_recognized)

azure_speak(response_from_ai)
