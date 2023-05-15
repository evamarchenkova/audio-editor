from pydub import effects

from logic.audio.audio import get_time_in_ms, get_instance, get_audio_from_path


def edit_audio(effect, **kwargs):
    audio = get_instance()
    match effect:
        case 'combine':
            audio_to_combine = get_audio_from_path(kwargs['audio_to_combine'])
            audio.audio = combine(audio.audio, audio_to_combine)
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
        case 'speedup':
            return speedup(part_to_edit)
        case 'slowdown':
            return slowdown(part_to_edit)
        case 'cut':
            return cut(part_to_edit)
        case 'reverse':
            return reverse(part_to_edit)
        case 'increase_volume':
            return increase_volume(part_to_edit)
        case 'decrease_volume':
            return decrease_volume(part_to_edit)


def speedup(part_to_edit):
    return effects.speedup(part_to_edit)


def slowdown(part_to_edit):
    return part_to_edit._spawn(part_to_edit.raw_data, overrides={
        "frame_rate": int(part_to_edit.frame_rate * 0.5)
    })


def cut(part_to_edit):
    return part_to_edit[0:0]


def reverse(part_to_edit):
    return part_to_edit.reverse()


def increase_volume(part_to_edit):
    return part_to_edit + 50


def decrease_volume(part_to_edit):
    return part_to_edit - 20


def combine(audio, audio_to_combine):
    return audio + audio_to_combine


def save(path_to_save_audio, audio_format):
    audio = get_instance()
    audio.audio.export('{}.{}'.format(path_to_save_audio, audio_format), format=audio_format)
    audio.is_saved = 1


def change_state_to_unsaved():
    audio = get_instance()
    audio.is_saved = 0
