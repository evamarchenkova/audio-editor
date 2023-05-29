from enum import Enum


class Action(Enum):
    change_playback_speed = 'Изменить скорость'
    change_volume = 'Изменить громкость'
    cut = 'Вырезать'
    reverse = 'Развернуть'
    combine = 'Склеить'
