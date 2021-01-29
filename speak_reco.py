import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
import pyttsx3
import os



r = sr.Recognizer() # initialise a recogniser

# listen for audio and convert it to text:
def reglin_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()




def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            reglin_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            reglin_speak('I did not get that')
        except sr.RequestError:
            reglin_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()


# get string and make a audio file to be played
def reglin_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en-ca') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print("Reglin" + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file