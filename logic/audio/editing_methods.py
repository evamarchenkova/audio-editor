from logic.audio.audio import get_time_in_ms, get_instance, get_audio_from_path
from constants.logic.audio.editing_methods import *


def edit_audio(effect, **kwargs):
    audio = get_instance()
    time_interval_beginning = get_time_in_ms(kwargs['time_interval'][0])
    time_interval_ending = get_time_in_ms(kwargs['time_interval'][1])
    effects = {'cut': cut, 'reverse': reverse}
    audio.audio = audio.audio[:time_interval_beginning] + \
                  effects[effect](audio.audio[time_interval_beginning:time_interval_ending]) + \
                  audio.audio[time_interval_ending:]


def parse(playback_speed_factor):
    return float(playback_speed_factor.strip()[:-1])


def change_playback_speed(time_interval_beginning, time_interval_ending, playback_speed_factor):
    playback_speed_factor = parse(playback_speed_factor)
    time_interval_beginning = get_time_in_ms(time_interval_beginning)
    time_interval_ending = get_time_in_ms(time_interval_ending)
    audio = get_instance()
    part_to_edit = audio.audio[time_interval_beginning:time_interval_ending]
    edited_part = part_to_edit._spawn(part_to_edit.raw_data, overrides={
        'frame_rate': int(part_to_edit.frame_rate * playback_speed_factor)
    })
    audio.audio = audio.audio[:time_interval_beginning] + edited_part + audio.audio[time_interval_ending:]


def change_volume(time_interval_beginning, time_interval_ending, volume):
    volume = parse(volume)
    time_interval_beginning = get_time_in_ms(time_interval_beginning)
    time_interval_ending = get_time_in_ms(time_interval_ending)
    audio = get_instance()
    part_to_edit = audio.audio[time_interval_beginning:time_interval_ending]
    edited_part = part_to_edit.apply_gain(volume - HUNDRED_VALUE)
    audio.audio = audio.audio[:time_interval_beginning] + edited_part + audio.audio[time_interval_ending:]


def cut(part_to_edit):
    return part_to_edit[0:0]


def reverse(part_to_edit):
    return part_to_edit.reverse()


def combine(audio_to_combine):
    audio = get_instance()
    audio_to_combine = get_audio_from_path(audio_to_combine)
    audio.audio = audio.audio + audio_to_combine


def save(path_to_save_audio, audio_format):
    audio = get_instance()
    audio.audio.export('{}.{}'.format(path_to_save_audio, audio_format), format=audio_format)
    audio.is_saved = TRUE_VALUE


def change_state_to_unsaved():
    audio = get_instance()
    audio.is_saved = FALSE_VALUE
