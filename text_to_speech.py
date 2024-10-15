import os
from gtts import gTTS

text = input('Enter the text: ')

sound = gTTS(text, lang='en')

#create a audio file
audio_file = 'audio.mp3'
sound.save(audio_file)

sound.os(f"start {audio_file}")