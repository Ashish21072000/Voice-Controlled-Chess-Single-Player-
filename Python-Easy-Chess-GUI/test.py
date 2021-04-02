import speech_recognition as sr
r = sr.Recognizer()
x = 0
with sr.Microphone() as source:
    audio_data2 = r.listen(source)
    # recognize (convert from speech to text)
    
    with open('speech.wav', 'wb')as f:
        f.write(audio_data2.get_wav_data())
with sr.AudioFile('./speech.wav') as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    x = 1
    print(text)
print(x)
