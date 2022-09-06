import os
import pathlib
from pydub import AudioSegment
from pydub.playback import play


def play_note(note_path, speed=1):
    # audio = AudioSegment.from_mp3(note_path)
    audio = AudioSegment.from_file(note_path, format="mp3")
    # Update frame_rate of the audio (how many samples to play per second)
    audio_with_updated_frame_rate = audio._spawn(audio.raw_data, overrides={
         "frame_rate": int(audio.frame_rate * speed)
      })
    # Convert the audio with updated frame rate to a standard frame rate
    # for the regular playback programs work properly. These programs usually
    # only play audio at standard frame rate
    updated_audio = audio_with_updated_frame_rate.set_frame_rate(audio.frame_rate)
    play(updated_audio)


def generate_stair_case(raga_notes, speed=1):
    """
    Plays staircase of a Raga with linear Arohana and Avarohana
    """
    l = len(raga_notes)
    # Staircase of Ascending notes/Arohana swaras
    for i in range(l):
        for j in range(i+1):
            play_note(raga_notes[j], speed=speed)
        for k in range(i-1, -1, -1):
            play_note(raga_notes[k], speed=speed)
        print("\n")
        
    # Staircase of Descending notes/Avarohana swaras
    for i in range(l-1, -1, -1):
        for j in range(l-1, i, -1):
            play_note(raga_notes[j], speed=speed)
        for k in range(i, l):
            play_note(raga_notes[k], speed=speed)
        print("\n")


p = pathlib.Path(__file__).parent / 'notes'
# notes = [p / 'key01.mp3', p / 'key02.mp3', p / 'key03.mp3', p / 'key04.mp3', p / 'key05.mp3', p / 'key06.mp3', p / 'key07.mp3', p / 'key08.mp3']
notes = [p / 'key01.mp3', p / 'key02.mp3', p / 'key04.mp3', p / 'key05.mp3', p / 'key07.mp3', p / 'key08.mp3']
if __name__ == '__main__':
    generate_stair_case(notes, speed=10)
