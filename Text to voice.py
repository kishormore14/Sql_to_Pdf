# pip install pyttsx3
import speech_recognition as sr
import pyttsx3

def type_by_voice():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

    try:
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

        # Save the recognized text to a text file
        with open("recognized_text.txt", "w") as file:
            file.write(text)
            print("Recognized text saved to 'recognized_text.txt'")

        # Convert the text to speech
        speak_text(text)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

def speak_text(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty("rate", 150)  # Speed of speech

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    type_by_voice()
