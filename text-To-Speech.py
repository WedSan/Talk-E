
import os
import io
from pydub import AudioSegment
from pydub.utils import which
from pydub.playback import play
import azure.cognitiveservices.speech as speechsdk

## Função para tocar com o áudio
def play_audio_from_bytes(audio_data, format='wav'):
        audio_data_io = io.BytesIO(audio_data)
        audio_segment = AudioSegment.from_file(audio_data_io, format=format)
        play(audio_segment)

### Configurando o caminho do ffmpeg para o pydub
ffmpeg_path = os.path.join('bin', 'ffmpeg.exe')
ffplay_path = os.path.join('bin', 'ffplay.exe')
AudioSegment.converter = ffmpeg_path
AudioSegment.ffplay = ffplay_path

###### Configuração da Azure
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'), region=os.environ.get('AZURE_SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#### Escolha da voz - para mais ler o README
speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

### Criando o sintetizador de fala
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)

## Texto a ser sintetizado
text = """Seja bem vindo ao Talk-e, sua IA para prática de Inglês. Welcome to talk-e""".strip()

# Síntese de fala 
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()


# Verificar o resultado da síntese
if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Síntese de fala concluída com sucesso.")
    audio_data = speech_synthesis_result.audio_data
    play_audio_from_bytes(audio_data)
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print(f"Síntese de fala cancelada: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print(f"Detalhes do erro: {cancellation_details.error_details}")