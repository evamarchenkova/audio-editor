def write_to_the_change_history(effect, **kwargs):
    with open("data/change_history.txt", "a") as file:
        match effect:
            case 'combine':
                audio_to_combine = kwargs['audio_to_combine']
                happened_change = '{};{}\n'.format(effect, audio_to_combine)
            case _:
                time_interval_beginning = kwargs['time_interval'][0]
                time_interval_ending = kwargs['time_interval'][1]
                happened_change = '{};{}-{}\n'.format(effect,
                                                      time_interval_beginning,
                                                      time_interval_ending)
        file.write(happened_change)


def clear_history():
    with open("data/change_history.txt", "w") as file:
        file.truncate()


def get_history():
    actions = ''
    actions_meta_information = ''
    with open("data/change_history.txt") as file:
        for line in file.readlines():
            action, action_meta_information = line.split(';')
            match action:
                case 'speedup':
                    action = 'Ускорить'
                case 'slowdown':
                    action = 'Замедлить'
                case 'cut':
                    action = 'Вырезать'
                case 'reverse':
                    action = 'Развернуть'
                case 'increase_volume':
                    action = 'Увеличить звук'
                case 'decrease_volume':
                    action = 'Уменьшить звук'
                case 'combine':
                    action = 'Склеить'
            actions += '{}\n'.format(action)
            actions_meta_information += action_meta_information
    return actions, actions_meta_information
