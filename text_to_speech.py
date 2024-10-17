import pyttsx3
engine = pyttsx3.init()    # Initialize the TTS engine

engine.setProperty('rate', 150)   # Set speech rate

engine.setProperty('volume', 1.0)   # Set volume (1.0 is max)

# Set gender: 0 for male, 1 for female (adjust index based on your system)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # Set to female voice (use voices[0] for male)

# Make sure text input is taken before the engine runs
text = input('Enter the text: ')   # Take input from the user

engine.say(text)   # Convert text to speech

engine.save_to_file(text, 'audio.mp3')   # Save speech to an audio file

engine.runAndWait()   # Play the speech
