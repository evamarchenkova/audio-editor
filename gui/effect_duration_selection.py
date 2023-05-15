from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

from gui.messages.error_message import ErrorMessage
from logic.audio import audio, editing_methods
from logic.history.change_history_editing_methods import write_to_the_change_history


class EffectDurationSelection(QWidget):
    def __init__(self, effect):
        super().__init__()
        self.effect = effect
        self.set_size()
        self.set_labels()
        self.time_interval_beginning = self.set_time_interval_beginning_edit_line()
        self.time_interval_ending = self.set_time_interval_ending_edit_line()
        self.set_ready_button()

    def set_size(self):
        self.setMinimumSize(200, 200)
        self.resize(400, 350)

    def set_labels(self):
        label1 = QLabel('Выберите отрезок', self)
        label1.move(150, 50)
        label2 = QLabel('Длительность аудио {}'.format(audio.get_formatted_audio_duration()), self)
        label2.move(135, 70)
        label3 = QLabel('-', self)
        label3.move(195, 90)

    def set_time_interval_beginning_edit_line(self):
        time_interval_beginning_edit_line = QLineEdit(self)
        time_interval_beginning_edit_line.setGeometry(160, 90, 30, 20)
        return time_interval_beginning_edit_line

    def set_time_interval_ending_edit_line(self):
        time_interval_ending_edit_line = QLineEdit(self)
        time_interval_ending_edit_line.setGeometry(210, 90, 30, 20)
        return time_interval_ending_edit_line

    def set_ready_button(self):
        ready_button = QPushButton('Готово', self)
        ready_button.move(163, 120)
        ready_button.clicked.connect(
            lambda: self.on_ready_button_clicked(self.time_interval_beginning.text(), self.time_interval_ending.text()))

    def on_ready_button_clicked(self, time_interval_beginning, time_interval_ending):
        try:
            editing_methods.edit_audio(self.effect,
                                       time_interval=[time_interval_beginning, time_interval_ending]
                                       )
            write_to_the_change_history(self.effect,
                                        time_interval=[time_interval_beginning, time_interval_ending]
                                        )
        except Exception as e:
            self.show_error_message(e)

    def show_error_message(self, response):
        self.error_message_window = ErrorMessage(response)
        self.error_message_window.show()
