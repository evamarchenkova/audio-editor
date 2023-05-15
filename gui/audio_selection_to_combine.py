from PyQt6.QtWidgets import QWidget, QLineEdit, QLabel

from gui.messages.error_message import ErrorMessage
from logic.audio import editing_methods
from logic.history.change_history_editing_methods import write_to_the_change_history


class AudioSelectionToCombine(QWidget):
    def __init__(self):
        super().__init__()
        self.effect = 'combine'
        self.set_size()
        self.set_label()
        self.set_audio_selection_to_combine_line()

    def set_size(self):
        self.setMinimumSize(200, 200)
        self.resize(400, 350)

    def set_label(self):
        label = QLabel('Выберите файл для склейки', self)
        label.move(130, 150)

    def set_audio_selection_to_combine_line(self):
        audio_selection_to_combine = QLineEdit(self)
        audio_selection_to_combine.move(140, 180)
        audio_selection_to_combine.returnPressed.connect(
            lambda: self.audio_selection_to_combine_pressed(audio_selection_to_combine.text()))

    def show_error_message(self, response):
        self.error_message_window = ErrorMessage(response)
        self.error_message_window.show()

    def audio_selection_to_combine_pressed(self, audio_selection_to_combine):
        try:
            editing_methods.edit_audio(self.effect, audio_to_combine=audio_selection_to_combine)
            write_to_the_change_history(self.effect,
                                        audio_to_combine=audio_selection_to_combine)
        except Exception as e:
            self.show_error_message(e)
