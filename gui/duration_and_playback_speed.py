from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QSlider
from superqt import QRangeSlider

from gui.audio_visualization import get_audio_visualization
from gui.messages.error_message import ErrorMessage
from logic.audio import audio, editing_methods
from logic.history.change_history_editing_methods import write_to_the_change_history
from constants.gui.duration_and_playback_speed import *
from constants.paths import PATH_TO_AUDIO_PLOT_IMAGE

import datetime


class DurationAndPlaybackSpeed(QWidget):
    def __init__(self):
        super().__init__()
        self.set_size()
        self.set_labels()
        self.set_ready_button()
        self.set_range_slider()
        self.set_audio_visualization()
        self.set_slider()

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
        self.playback_speed_factor = QLabel('1.0x    ', self)
        self.playback_speed_factor.move(324, 195)

    def set_ready_button(self):
        ready_button = QPushButton('Готово', self)
        ready_button.move(163, 250)
        ready_button.clicked.connect(self.on_ready_button_clicked)

    def on_ready_button_clicked(self):
        try:
            editing_methods.edit_audio('change_playback_speed',
                                       time_interval=[self.time_interval_beginning.text(),
                                                      self.time_interval_ending.text()],
                                       speed=self.playback_speed_factor.text()
                                       )
            write_to_the_change_history('change_playback_speed',
                                        time_interval=[self.time_interval_beginning.text(),
                                                       self.time_interval_ending.text()],
                                        speed=self.playback_speed_factor.text()
                                        )
        except Exception as e:
            self.show_error_message(e)

    def show_error_message(self, response):
        self.error_message_window = ErrorMessage(response)
        self.error_message_window.show()

    def set_range_slider(self):
        range_slider = QRangeSlider(self)
        range_slider.setRange(ZERO_VALUE, audio.get_audio_duration_in_seconds())
        range_slider.setSliderPosition([ZERO_VALUE, audio.get_audio_duration_in_seconds()])
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

    def set_slider(self):
        slider = QSlider(self)
        slider.setOrientation(Qt.Orientation.Horizontal)
        slider.setGeometry(82, 200, 222, 10)
        slider.setRange(SLIDER_RANGE_MIN, SLIDER_RANGE_MAX)
        slider.setSingleStep(SLIDER_SINGLE_STEP)
        slider.setSliderPosition(SLIDER_POSITION)
        slider.valueChanged.connect(lambda: self.on_slider_value_changed(slider))

    def on_slider_value_changed(self, slider):
        self.playback_speed_factor.setText('{}x'.format(slider.value() / HUNDRED_VALUE))
