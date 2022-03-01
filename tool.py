import os
from  text_to_speech import text_to_speech
from speech_to_text import speech_to_text
from translate_text import translate_text
from audio_to_speaker import audio_to_speaker

# outputlang = "en"
# langs = ['es', 'en', 'fr']

def main():
  FILE_NAME = "output"
  INPUT_TEXT = 'sample.txt'
  text2speech(INPUT_TEXT)
  play_audio(FILE_NAME)

if __name__ == "__main__":
  main()

