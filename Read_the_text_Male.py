import pyttsx3

def read_and_speak():
    # Read the text from the file
    try:
        with open("recognized_text.txt", "r") as file:
            text = file.read()
            print(f"Text read from file: {text}")

            # Convert the text to speech
            speak_text(text)

    except FileNotFoundError:
        print("File 'recognized_text.txt' not found.")

def speak_text(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty("rate", 150)  # Speed of speech

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    read_and_speak()
