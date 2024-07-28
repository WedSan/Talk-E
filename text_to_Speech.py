
import os
import io
from pydub import AudioSegment
from pydub.playback import play
import azure.cognitiveservices.speech as speechsdk

## Função para tocar com o áudio
def play_audio_from_bytes(audio_data, format='wav'):
        audio_data_io = io.BytesIO(audio_data)
        audio_segment = AudioSegment.from_file(audio_data_io, format=format)
        play(audio_segment)


def azure_speak(message: str) -> None:
    ###### Configuração da Azure
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'), region=os.environ.get('AZURE_SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    #### Escolha da voz - para mais ler o README
    speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

    ### Criando o sintetizador de fala
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)

    ## Texto a ser sintetizado
    xml_text = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>     <voice name='en-US-AvaMultilingualNeural'>         $     </voice> </speak>"
    text = xml_text.replace("$", message)

    # Síntese de fala 
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(text).get()

    # Verificar o resultado da síntese
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Síntese de fala concluída com sucesso.")
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print(f"Síntese de fala cancelada: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Detalhes do erro: {cancellation_details.error_details}")

#example usage
# azure_speak("Seja bem vindo ao Talk-e, sua IA para prática de Inglês. Welcome to talk-e")