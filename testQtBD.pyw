from PyQt5 import QtWidgets, uic


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi(r'./testBD.ui', self)
        self.push_button_clear.clicked.connect(QtWidgets.qApp.quit)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
