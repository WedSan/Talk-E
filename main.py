from speech_to_text import recognize_from_microphone
from gpt_ai import GPT
from text_to_Speech import azure_speak
from generative_ai import GenerativeArtificialInteligence
from gemini_ai import Gemini
import os

text_recognized: str = recognize_from_microphone()

generative_ai: GenerativeArtificialInteligence = Gemini(os.environ["GENERATIVE_AI_GEMINI_KEY"], os.environ["GENERATIVE_AI_GEMINI_ENDPOINT"])
response_from_ai: str = generative_ai.generate_response(text_recognized)

azure_speak(response_from_ai)
