from pydub import AudioSegment
from pydub.playback import play

from logic.singleton import Singleton
from constants.logic.audio.audio import *


def create_instance(path_to_audio, is_saved):
    Audio(get_audio_from_path(path_to_audio), is_saved)


def get_instance():
    for item in Singleton._instances.items():
        return item[1]


def get_audio_from_path(path_to_audio):
    return AudioSegment.from_file(path_to_audio)


def get_audio_duration_in_seconds():
    return len(get_instance().audio) // MILLISECONDS_PER_SECOND


def get_formatted_audio_duration():
    audio_duration = get_audio_duration_in_seconds()
    minutes = audio_duration // SECONDS_PER_MINUTE
    seconds = audio_duration % SECONDS_PER_MINUTE
    return '{}:0{}'.format(minutes, seconds) if seconds < 10 else '{}:{}'.format(minutes, seconds)


def get_time_in_ms(time_stamp):
    minutes, seconds = map(int, time_stamp.split(':'))
    return (minutes * SECONDS_PER_MINUTE + seconds) * MILLISECONDS_PER_SECOND


def play_audio():
    audio = get_instance()
    play(audio.audio)


class Audio(metaclass=Singleton):
    def __init__(self, audio, is_saved):
        self.audio = audio
        self.is_saved = is_saved
