from pydub import AudioSegment
from pydub.playback import play


def audio_to_speaker(file_name):
  # name = (file_name[:-4]) + ".wav"
  # song.export(newName, format = "wav")
  wav_file = AudioSegment.from_file(file = file_name,
                                  format = "wav")
  play(wav_file)