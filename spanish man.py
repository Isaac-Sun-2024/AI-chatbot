# using gpt-3.5-turbo because davinci is too expensive
import subprocess as sp
import openai
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from threading import Thread, Event



# messgaes
messages = []

#personality
# system_msg = "You are an mexican ex-convict who has escaped maximum security prison and is on the run. you have recently escaped to spain and you do not speak fluent english. You enjoy helping children with their homework. You start your responses with Ex-convict:"
system_msg = "You are a redneck farmer from alabama who speaks in a strong redneck accent. Your name is a 'Jeb Higgins' you have an AI called agribrain that helps you at your farm. You must start your responses with Jeb Higgins:"
messages.append({"role": "system", "content": system_msg})

# translator
translator = Translator()

# api key for openAI
openai.api_key = ""

# make tts engine
engine = pyttsx3.init()

engine.setProperty('voice', "com.apple.speech.synthesis.voice.jorge")


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('Skipping unknown error')


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    return response["choices"][0]["message"]["content"]


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


print("""
 _____                            _____                    ___  _____ 
|_   _|                          /  ___|                  / _ \|_   _|
  | | ___  __ _  __ _  ___ ______\ `--. _   _ _ __ ______/ /_\ \ | |  
  | |/ __|/ _` |/ _` |/ __|______|`--. \ | | | '_ \______|  _  | | |  
 _| |\__ \ (_| | (_| | (__       /\__/ / |_| | | | |     | | | |_| |_ 
 \___/___/\__,_|\__,_|\___|      \____/ \__,_|_| |_|     \_| |_/\___/ 

                               gpt-3.5-turbo
""")

print("This AI was made by Isaac Sun.")


def main():
    while True:
        start = input('\n manual or recording? (m/r): ')
        if start == "r":
            # record audio
            filename = "input.wav"
            print("\n Listening...")
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                source.pause_threshold = 1
                audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                with open(filename, "wb") as f:
                    f.write(audio.get_wav_data())

            # audio to text
            text1 = transcribe_audio_to_text(filename)
            print(f"\n You (english): {text1}")

            # store in memory
            messages.append({"role": "user", "content": text1})

            # translate to spanish
            text = translator.translate(text1, src='en', dest='es')

            if text:
                print(f"\n You (in spanish): {text.text}")

                # generate response using ai
                response = generate_response(text1)
                hmmm = translator.translate(response, src='es', dest='en')
                print(hmmm.text)
                messages.append({"role": "assistant", "content": response})

                #translate
                yabadabadoo = translator.translate(response, src='en', dest='es')
                print('\n spanish man (spanish): ' + yabadabadoo.text)

                # read response with tts
                speak_text(yabadabadoo.text)

        elif start == 'm':
            # audio to text
            text1 = input('Message: ')
            print(f"\n You (english): {text1}")

            # store in memory
            messages.append({"role": "user", "content": text1})

            # translate to spanish
            text = translator.translate(text1, src='en', dest='es')

            if text:
                print(f"\n You (in spanish): {text.text}")

                # generate response using ai
                response = generate_response(text1)
                hmmm = translator.translate(response, src='es', dest='en')
                print(hmmm.text)
                messages.append({"role": "assistant", "content": response})

                yabadabadoo = translator.translate(response, src='en', dest='es')
                print('\n spanish man (spanish): ' + yabadabadoo.text)

                # read response with tts
                speak_text(yabadabadoo.text)

        else:
            print('Exiting Program...')
            # the best thing is, I don't have to clear memory!
            quit()
    # except Exception as e:
    # print("an error occured: {}".format(e))

if __name__ == "__main__":
    def lol1(event: Event) -> None:
        global extProc1
        extProc1 = sp.Popen(['python', 'facedetect.py'])

    event = Event()
    thread0 = Thread(target=lol1, args=(event,))
    thread0.start()
    main()


