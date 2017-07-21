from PyQt5 import QtWidgets, uic, QtCore
import testQTBD_About


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi(r'./testBD.ui', self)
        QtWidgets.qApp.processEvents()
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionAbout.triggered.connect(self.show_about_form)

    def show_about_form(self):
        global modal_window
        modal_window = testQTBD_About.MyWindowAbout(parent=self)
        modal_window.setWindowModality(QtCore.Qt.WindowModal)
        modal_window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        modal_window.move(self.geometry().center() - modal_window.rect().center() + QtCore.QPoint(4, 50))
        modal_window.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
