import os
from  text_to_speech import text_to_speech
from speech_to_text import speech_to_text
from translate_text import translate_text
from audio_to_speaker import audio_to_speaker

filename = "output"
translated_text = 'sample.txt'
# outputlang = "en"
# langs = ['es', 'en', 'fr']

if __name__ == "__main__":
    text2speech(translated_text, outputlang)
    play_audio(filename + ".mp3")
