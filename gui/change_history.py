from PyQt6.QtWidgets import QWidget, QLabel

from logic.history.change_history_editing_methods import get_history


class ChangeHistory(QWidget):
    def __init__(self):
        super().__init__()
        self.set_size()
        self.set_label()

    def set_size(self):
        self.setMinimumSize(200, 200)
        self.resize(400, 350)

    def set_label(self):
        actions, actions_meta_information = get_history()[0], get_history()[1]
        label1 = QLabel(actions, self)
        label2 = QLabel(actions_meta_information, self)
        label1.setGeometry(0, 0, 200, 350)
        label2.setGeometry(200, 0, 200, 350)
