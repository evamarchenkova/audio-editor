from PyQt6.QtWidgets import QWidget, QLabel, QPushButton

from gui.change_history import ChangeHistory
from gui.duration_and_playback_speed import DurationAndPlaybackSpeed
from gui.duration_and_volume_changing import DurationAndVolumeChanging
from gui.saving.audio_change_saving import AudioChangeSaving
from gui.audio_selection_to_combine import AudioSelectionToCombine
from gui.effect_duration_selection import EffectDurationSelection
from logic.audio.audio import get_instance
from logic.audio.editing_methods import save


class EditingOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.set_label()
        self.set_buttons()

    def set_label(self):
        label = QLabel('Выбор действия', self)
        label.move(150, 10)

    def set_buttons(self):
        self.set_change_playback_speed_button()
        self.set_cut_button()
        self.set_reverse_button()
        self.set_change_volume_button()
        self.set_combine_button()
        self.set_save_button()
        self.set_history_button()

    def set_change_playback_speed_button(self):
        button = QPushButton('Изменить скорость', self)
        button.move(160, 70)
        button.clicked.connect(self.show_duration_and_playback_speed)

    def set_cut_button(self):
        button = QPushButton('Вырезать', self)
        button.move(160, 100)
        button.clicked.connect(lambda: self.show_effect_duration_selection('cut'))

    def set_reverse_button(self):
        button = QPushButton('Развернуть', self)
        button.move(160, 130)
        button.clicked.connect(lambda: self.show_effect_duration_selection('reverse'))

    def set_change_volume_button(self):
        button = QPushButton('Изменить громкость', self)
        button.move(160, 160)
        button.clicked.connect(self.show_duration_and_volume_changing)

    def set_combine_button(self):
        button = QPushButton('Склеить', self)
        button.move(160, 190)
        button.clicked.connect(self.show_audio_selection_to_combine)

    def set_save_button(self):
        button = QPushButton('Сохранить', self)
        button.move(160, 220)
        button.clicked.connect(self.show_audio_change_saving)

    def set_history_button(self):
        button = QPushButton('История', self)
        button.move(160, 250)
        button.clicked.connect(self.show_change_history)

    def show_effect_duration_selection(self, effect):
        self.effect_duration_selection_window = EffectDurationSelection(effect)
        self.effect_duration_selection_window.show()

    def show_duration_and_playback_speed(self):
        self.duration_and_playback_speed_window = DurationAndPlaybackSpeed()
        self.duration_and_playback_speed_window.show()

    def show_duration_and_volume_changing(self):
        self.duration_and_volume_changing_window = DurationAndVolumeChanging()
        self.duration_and_volume_changing_window.show()

    def show_audio_selection_to_combine(self):
        self.audio_selection_to_combine_window = AudioSelectionToCombine()
        self.audio_selection_to_combine_window.show()

    def show_audio_change_saving(self):
        self.audio_change_saving_window = AudioChangeSaving()
        self.audio_change_saving_window.show()

    def show_change_history(self):
        self.change_history_window = ChangeHistory()
        self.change_history_window.show()

    def closeEvent(self, event):
        audio = get_instance()
        if not audio.is_saved:
            save(r'data\temporary_file', 'mp3')
        super().closeEvent(event)
