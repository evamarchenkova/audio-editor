from logic.audio.audio import get_time_in_ms, get_instance, get_audio_from_path
from constants.logic.audio.editing_methods import *


def edit_audio(effect, **kwargs):
    audio = get_instance()
    match effect:
        case 'combine':
            audio_to_combine = get_audio_from_path(kwargs['audio_to_combine'])
            audio.audio = combine(audio.audio, audio_to_combine)
        case 'change_playback_speed':
            time_interval_beginning = get_time_in_ms(kwargs['time_interval'][0])
            time_interval_ending = get_time_in_ms(kwargs['time_interval'][1])
            audio.audio = audio.audio[:time_interval_beginning] + \
                          change_playback_speed(audio.audio[time_interval_beginning:time_interval_ending],
                                                kwargs['speed']) + \
                          audio.audio[time_interval_ending:]
        case 'change_volume':
            time_interval_beginning = get_time_in_ms(kwargs['time_interval'][0])
            time_interval_ending = get_time_in_ms(kwargs['time_interval'][1])
            audio.audio = audio.audio[:time_interval_beginning] + \
                          change_volume(audio.audio[time_interval_beginning:time_interval_ending], kwargs['volume']) + \
                          audio.audio[time_interval_ending:]
        case _:
            time_interval_beginning = get_time_in_ms(kwargs['time_interval'][0])
            time_interval_ending = get_time_in_ms(kwargs['time_interval'][1])
            if time_interval_ending <= time_interval_beginning:
                raise ValueError
            audio.audio = audio.audio[:time_interval_beginning] + \
                          apply_effect(audio.audio[time_interval_beginning:time_interval_ending], effect) + \
                          audio.audio[time_interval_ending:]


def apply_effect(part_to_edit, effect):
    match effect:
        case 'cut':
            return cut(part_to_edit)
        case 'reverse':
            return reverse(part_to_edit)


def parse_speed(playback_speed_factor):
    return float(playback_speed_factor.strip()[:-1])


def change_playback_speed(part_to_edit, playback_speed_factor):
    playback_speed_factor = parse_speed(playback_speed_factor)
    return part_to_edit._spawn(part_to_edit.raw_data, overrides={
        'frame_rate': int(part_to_edit.frame_rate * playback_speed_factor)
    })


def change_volume(part_to_edit, volume):
    volume = parse_speed(volume)
    return part_to_edit.apply_gain(volume - HUNDRED_VALUE)


def cut(part_to_edit):
    return part_to_edit[0:0]


def reverse(part_to_edit):
    return part_to_edit.reverse()


def combine(audio, audio_to_combine):
    return audio + audio_to_combine


def save(path_to_save_audio, audio_format):
    audio = get_instance()
    audio.audio.export('{}.{}'.format(path_to_save_audio, audio_format), format=audio_format)
    audio.is_saved = TRUE_VALUE


def change_state_to_unsaved():
    audio = get_instance()
    audio.is_saved = FALSE_VALUE
