from PyQt6.QtWidgets import QWidget, QLabel, QPushButton

from gui.change_history import ChangeHistory
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
        self.set_speed_up_button()
        self.set_slow_down_button()
        self.set_cut_button()
        self.set_reverse_button()
        self.set_increase_volume_button()
        self.set_decrease_volume_button()
        self.set_combine_button()
        self.set_save_button()
        self.set_history_button()

    def set_speed_up_button(self):
        button = QPushButton('Ускорить', self)
        button.move(160, 40)
        button.clicked.connect(lambda: self.show_effect_duration_selection('speedup'))

    def set_slow_down_button(self):
        button = QPushButton('Замедлить', self)
        button.move(160, 70)
        button.clicked.connect(lambda: self.show_effect_duration_selection('slowdown'))

    def set_cut_button(self):
        button = QPushButton('Вырезать', self)
        button.move(160, 100)
        button.clicked.connect(lambda: self.show_effect_duration_selection('cut'))

    def set_reverse_button(self):
        button = QPushButton('Развернуть', self)
        button.move(160, 130)
        button.clicked.connect(lambda: self.show_effect_duration_selection('reverse'))

    def set_increase_volume_button(self):
        button = QPushButton('Увеличить звук', self)
        button.move(160, 160)
        button.clicked.connect(lambda: self.show_effect_duration_selection('increase_volume'))

    def set_decrease_volume_button(self):
        button = QPushButton('Уменьшить звук', self)
        button.move(160, 190)
        button.clicked.connect(lambda: self.show_effect_duration_selection('decrease_volume'))

    def set_combine_button(self):
        button = QPushButton('Склеить', self)
        button.move(160, 220)
        button.clicked.connect(self.show_audio_selection_to_combine)

    def set_save_button(self):
        button = QPushButton('Сохранить', self)
        button.move(160, 250)
        button.clicked.connect(self.show_audio_change_saving)

    def set_history_button(self):
        button = QPushButton('История', self)
        button.move(160, 280)
        button.clicked.connect(self.show_change_history)

    def show_effect_duration_selection(self, effect):
        self.effect_duration_selection_window = EffectDurationSelection(effect)
        self.effect_duration_selection_window.show()

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
