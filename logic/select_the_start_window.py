import os

from PyQt6.QtWidgets import QMessageBox

from constants.audio_file_extensions import MP3
from gui.audio_selection_for_processing import AudioSelectionForProcessing
from gui.editing_options import EditingOptions
from logic.audio.audio import create_instance
from logic.history.change_history_editing_methods import clear_history
from constants.paths import PATH_TO_TEMPORARY_AUDIO_FILE
from constants.logic.select_the_start_window import *


def show_continue_editing_message():
    message = QMessageBox()
    message.setWindowTitle('У вас есть несохраненные файлы')
    message.setText('Желаете продолжить?')
    message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    message.button(QMessageBox.StandardButton.Yes).setText('Да')
    message.button(QMessageBox.StandardButton.No).setText('Нет')
    message.setIcon(QMessageBox.Icon.Question)
    if message.exec() == QMessageBox.StandardButton.Yes:
        return 'yes'
    else:
        return 'no'


def select_the_start_window():
    path = '{}.{}'.format(PATH_TO_TEMPORARY_AUDIO_FILE, MP3)
    if os.path.isfile(path):
        if show_continue_editing_message() == 'yes':
            create_instance(path, FALSE_VALUE)
            start_window = EditingOptions()
        else:
            clear_history()
            start_window = AudioSelectionForProcessing()
        os.remove(path)
    else:
        clear_history()
        start_window = AudioSelectionForProcessing()
    return start_window
