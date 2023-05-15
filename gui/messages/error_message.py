from PyQt6.QtWidgets import QMessageBox

from logic.exceptions.handling_exceptions import handle_exception


class ErrorMessage(QMessageBox):
    def __init__(self, exception):
        super().__init__()
        self.setText(handle_exception(exception))
