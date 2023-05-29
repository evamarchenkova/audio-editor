from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from superqt import QRangeSlider

from gui.audio_visualization import get_audio_visualization
from gui.messages.error_message import ErrorMessage
from logic.audio import audio, editing_methods
from logic.history.change_history_editing_methods import write_to_the_change_history
from constants.paths import PATH_TO_AUDIO_PLOT_IMAGE

import datetime


class EffectDurationSelection(QWidget):
    def __init__(self, effect):
        super().__init__()
        self.effect = effect
        self.set_size()
        self.set_labels()
        self.set_ready_button()
        self.set_range_slider()
        self.set_audio_visualization()

    def set_size(self):
        self.setMinimumSize(200, 200)
        self.resize(400, 350)

    def set_labels(self):
        label1 = QLabel('Выбранный отрезок: ', self)
        label1.move(120, 50)
        label2 = QLabel('-', self)
        label2.move(268, 50)
        self.time_interval_beginning = QLabel('0:00', self)
        self.time_interval_beginning.setGeometry(240, 52, 30, 10)
        self.time_interval_ending = QLabel(audio.get_formatted_audio_duration(), self)
        self.time_interval_ending.setGeometry(275, 52, 30, 10)

    def set_ready_button(self):
        ready_button = QPushButton('Готово', self)
        ready_button.move(163, 250)
        ready_button.clicked.connect(self.on_ready_button_clicked)

    def on_ready_button_clicked(self):
        try:
            editing_methods.edit_audio(self.effect,
                                       time_interval=[self.time_interval_beginning.text(),
                                                      self.time_interval_ending.text()]
                                       )
            write_to_the_change_history(self.effect,
                                        time_interval=[self.time_interval_beginning.text(),
                                                       self.time_interval_ending.text()]
                                        )
        except Exception as e:
            self.show_error_message(e)

    def show_error_message(self, response):
        self.error_message_window = ErrorMessage(response)
        self.error_message_window.show()

    def set_range_slider(self):
        range_slider = QRangeSlider(self)
        range_slider.setRange(0, audio.get_audio_duration_in_seconds())
        range_slider.setSliderPosition([0, audio.get_audio_duration_in_seconds()])
        range_slider.setOrientation(Qt.Orientation.Horizontal)
        range_slider.setGeometry(82, 110, 242, 10)
        range_slider.valueChanged.connect(lambda: self.on_range_slider_value_changed(range_slider))

    def on_range_slider_value_changed(self, range_slider):
        beginning_time = str(datetime.datetime.utcfromtimestamp(range_slider.value()[0]).strftime('%M:%S'))
        ending_time = str(datetime.datetime.utcfromtimestamp(range_slider.value()[1]).strftime('%M:%S'))
        self.time_interval_beginning.setText(beginning_time)
        self.time_interval_ending.setText(ending_time)

    def set_audio_visualization(self):
        get_audio_visualization()
        label = QLabel(self)
        label.setGeometry(30, 70, 340, 80)
        label.lower()
        pixmap = QPixmap(PATH_TO_AUDIO_PLOT_IMAGE)
        pixmap = pixmap.scaledToHeight(label.height())
        pixmap = pixmap.scaledToWidth(label.width())
        label.setPixmap(pixmap)
