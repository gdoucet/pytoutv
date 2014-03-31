from PyQt4 import Qt
from toutvqt import utils


class QTouTvAboutDialog(Qt.QDialog, utils.QtUiLoad):
    _UI_NAME = 'about_dialog'

    def __init__(self):
        super(QTouTvAboutDialog, self).__init__()

        self._setup_ui()

    def _setup_ui(self):
        self._load_ui(QTouTvAboutDialog._UI_NAME)

    def show_move(self, pos):
        self.move(pos)
        self.exec()
