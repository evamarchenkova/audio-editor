from PyQt6.QtWidgets import QMessageBox


class SuccessfulSavingMessage(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('Файл успешно сохранен')
