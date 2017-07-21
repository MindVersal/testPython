from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindowAbout(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.setWindowTitle('Form About from PNG.')
        self.resize(800, 480)
        pixmap = QtGui.QPixmap(r'./123456.png')
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        self.setPalette(pal)
        self.setMask(pixmap.mask())
        button = QtWidgets.QPushButton('Согласен!', self)
        button.setFixedSize(100, 25)
        button.move(350, 420)
        button.clicked.connect(self.on_quit_event)

    def on_quit_event(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindowAbout()
    window.show()
    sys.exit(app.exec_())

