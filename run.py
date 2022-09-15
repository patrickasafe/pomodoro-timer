import sys

from PyQt5.QtWidgets import QApplication

from src.PomodoroCounter import PomodoroTimer
from src.PomodoroStyleSheet import style_sheet


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = PomodoroTimer()
    sys.exit(app.exec_())
