import speech_recognition as sr

def record_audio():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1) as source:
        print("Processing...")
        audio = r.listen(source)

    query = r.recognize_google(audio, language = 'en-EN')
    print(f'Message: {query.lower()}')

record_audio()    