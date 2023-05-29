from constants.paths import PATH_TO_CHANGE_HISTORY_FILE
from logic.history.action import Action


def write_to_the_change_history(effect, **kwargs):
    with open(PATH_TO_CHANGE_HISTORY_FILE, "a") as file:
        if effect == Action.combine.name:
            audio_to_combine = kwargs['audio_to_combine']
            happened_change = '{};{}\n'.format(effect, audio_to_combine)
        elif effect == Action.change_playback_speed.name:
            time_interval_beginning = kwargs['time_interval'][0]
            time_interval_ending = kwargs['time_interval'][1]
            happened_change = '{};{}-{}, {}\n'.format(effect,
                                                      time_interval_beginning,
                                                      time_interval_ending,
                                                      kwargs['speed'])
        elif effect == Action.change_volume.name:
            time_interval_beginning = kwargs['time_interval'][0]
            time_interval_ending = kwargs['time_interval'][1]
            happened_change = '{};{}-{}, {}\n'.format(effect,
                                                      time_interval_beginning,
                                                      time_interval_ending,
                                                      kwargs['volume'])
        else:
            time_interval_beginning = kwargs['time_interval'][0]
            time_interval_ending = kwargs['time_interval'][1]
            happened_change = '{};{}-{}\n'.format(effect,
                                                  time_interval_beginning,
                                                  time_interval_ending)
        file.write(happened_change)


def clear_history():
    with open(PATH_TO_CHANGE_HISTORY_FILE, "w") as file:
        file.truncate()


def get_history():
    actions = ''
    actions_meta_information = ''
    with open(PATH_TO_CHANGE_HISTORY_FILE) as file:
        for line in file.readlines():
            action, action_meta_information = line.split(';')
            if action == Action.change_playback_speed.name:
                action = Action.change_playback_speed.value
            elif action == Action.change_volume.name:
                action = Action.change_volume.value
            elif action == Action.cut.name:
                action = Action.cut.value
            elif action == Action.reverse.name:
                action = Action.reverse.value
            elif action == Action.combine.name:
                action = Action.combine.value
            actions += '{}\n'.format(action)
            actions_meta_information += action_meta_information
    return actions, actions_meta_information
