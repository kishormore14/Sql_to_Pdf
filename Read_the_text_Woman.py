import pyttsx3

def read_and_speak():
    # Read the text from the file
    try:
        with open("recognized_text.txt", "r") as file:
            text = file.read()
            print(f"Text read from file: {text}")

            # Convert the text to speech with a female voice
            speak_text(text, gender='female')

    except FileNotFoundError:
        print("File 'recognized_text.txt' not found.")

def speak_text(text, gender='male'):
    # Initialize the TTS engine with sapi5 driver
    engine = pyttsx3.init(driverName='sapi5')

    # Set properties (optional)
    engine.setProperty("rate", 150)  # Speed of speech

    # Select a voice with the specified gender
    if gender.lower() == 'female':
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Index 1 is typically a female voice

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    read_and_speak()
