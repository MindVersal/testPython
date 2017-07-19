import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QMessageBox, QDesktopWidget, qApp)
from PyQt5.QtGui import QIcon
from PyQt5 import uic


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        qbtn = QPushButton('Close', self)
        qbtn.setToolTip('Press for <b>Quit</b>')
        qbtn.clicked.connect(qApp.quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 150)

        self.resize(500, 300)
        self.center()
        self.setWindowTitle('BD')
        self.setWindowIcon(QIcon('icon_1.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # ex = Example()
    window = uic.loadUi("testQt.ui")  # type: <class 'PyQt4.QtGui.QWidget'>
    window.show()
    sys.exit(app.exec_())
