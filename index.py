import speech_recognition as sr

microfone = sr.Recognizer()

with sr.Microphone() as source:
    microfone.adjust_for_ambient_noise(source)

    print("dizer alguma coisa")

    audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google_cloud(audio, language='pt-br')
        print("frase: "+frase)
    except sr.UnknownValueError:
        print("Erro")