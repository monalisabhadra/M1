import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')


    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in english")
        audio = recognizer.listen(source)


        try:
            print("???? Recognizing Speech....")
            text = recognizer.recognize_google(audio, language="en-US")
            print(f"You said{text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("API ERROR:{e}")
        return""
    

def translate_text(text, target_language="hi"):
    translation = GoogleTranslator(source="auto", target=target_language).translate(text)
    print(f"Translated Text: {translation}")
    return translation

def display_language_options():
    print("???? Available translation language:")
    print("1. Hindi(hi)")
    print("2. Tamil(ta)")
    print("3. Telegu(te)")
    print("4. Bengali(bn)")
    print("5. Marathi(mr)")
    print("6. Gujarati(gu)")
    print("7. Malayalam(ml)")
    print("8. Punjabi(pa)")

    choice = input("please select the target language number(1-8):")
    language_dict = {
        "1":"hi",
        "2":"ta",
        "3":"te",
        "4":"bn",
        "5":"mr",
        "6":"gu",
        "7":"ml",
        "8":"pa"
        }
    return language_dict.get(choice, "es")  


def main():
    
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
       translated_text =transalate_text(original_text, target_language=target_language)
       speak(transalate_text, language="en")
       print("Translation Spoken out")

if __name__ == "__main__":
    main()