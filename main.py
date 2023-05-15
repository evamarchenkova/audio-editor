from PyQt6.QtWidgets import QApplication

import sys

from logic import select_the_start_window


def main():
    app = QApplication(sys.argv)
    start_window = select_the_start_window.select_the_start_window()
    start_window.show()
    app.exec()


if __name__ == '__main__':
    main()
