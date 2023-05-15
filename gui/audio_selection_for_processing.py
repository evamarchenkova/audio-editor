from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit

from logic.audio.audio import create_instance
from gui.messages.error_message import ErrorMessage
from gui.editing_options import EditingOptions


class AudioSelectionForProcessing(QWidget):
    def __init__(self):
        super().__init__()
        self.set_size()
        self.set_label()
        self.set_audio_selection_line()

    def set_size(self):
        self.setMinimumSize(200, 200)
        self.resize(400, 350)

    def set_label(self):
        label = QLabel('Выберите файл', self)
        label.move(150, 120)

    def set_audio_selection_line(self):
        audio_selection = QLineEdit(self)
        audio_selection.move(130, 150)
        audio_selection.returnPressed.connect(lambda: self.audio_selection_line_pressed(audio_selection))

    def audio_selection_line_pressed(self, audio_selection):
        try:
            create_instance(audio_selection.text(), 0)
            self.show_editing_options_and_change_history()
        except Exception as e:
            self.show_error_message(e)

    def show_editing_options_and_change_history(self):
        self.editing_options_window = EditingOptions()
        self.editing_options_window.show()

    def show_error_message(self, exception):
        self.error_message_window = ErrorMessage(exception)
        self.error_message_window.show()
