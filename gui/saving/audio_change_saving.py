from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QComboBox

from gui.messages.error_message import ErrorMessage
from gui.messages.successful_saving_message import SuccessfulSavingMessage
from logic.audio.audio import play_audio
from logic.audio.editing_methods import save


class AudioChangeSaving(QWidget):
    def __init__(self):
        super().__init__()
        self.set_size()
        self.set_label()
        self.path_to_save_audio = self.set_line_edit()
        self.audio_format = self.set_combo_box()
        self.set_ready_button()
        self.set_play_button()

    def set_size(self):
        self.setMinimumSize(200, 200)
        self.resize(400, 350)

    def set_label(self):
        label = QLabel('Выберите имя и путь для сохранения файла', self)
        label.move(100, 120)

    def set_line_edit(self):
        line_edit = QLineEdit(self)
        line_edit.move(100, 150)
        return line_edit

    def set_combo_box(self):
        combo_box = QComboBox(self)
        combo_box.addItems(['mp3', 'wav', 'raw', 'ogg'])
        combo_box.move(235, 150)
        return combo_box

    def set_ready_button(self):
        button = QPushButton('Готово', self)
        button.move(155, 210)
        button.clicked.connect(
            lambda: self.on_button_clicked(self.path_to_save_audio.text(), self.audio_format.currentText()))

    def on_button_clicked(self, path_to_save_audio, audio_format):
        try:
            save(path_to_save_audio, audio_format)
            self.show_successful_saving_message()
        except Exception as e:
            self.show_error_message(e)

    def show_error_message(self, response):
        self.error_message_window = ErrorMessage(response)
        self.error_message_window.show()

    def show_successful_saving_message(self):
        self.successful_saving_message_window = SuccessfulSavingMessage()
        self.successful_saving_message_window.show()

    def set_play_button(self):
        button = QPushButton('Прослушать', self)
        button.move(155, 180)
        button.clicked.connect(lambda: play_audio())
