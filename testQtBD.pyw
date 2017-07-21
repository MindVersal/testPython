from PyQt5 import QtWidgets, uic, QtCore, QtGui
import testQTBD_About


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi(r'./testBD.ui', self)
        QtWidgets.qApp.processEvents()
        self.init_table_view_bd()
        self.init_combobox_zodiak()
        self.init_all_listeners()

    def init_all_listeners(self):
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionAbout.triggered.connect(self.show_about_form)

    def init_table_view_bd(self):
        table_model = QtGui.QStandardItemModel()
        list_names_of_schema = ['Фамилия', 'Имя', 'Отчество',
                                'Год', 'Месяц', 'День',
                                'Документ', 'Город', 'Сельсовет',
                                'Улица', 'Дом', 'Кв.']
        table_model.setHorizontalHeaderLabels(list_names_of_schema)
        self.table_view_bd.setModel(table_model)
        self.table_view_bd.setColumnWidth(0, 120)  # family
        self.table_view_bd.setColumnWidth(1, 120)  # name
        self.table_view_bd.setColumnWidth(2, 120)  # farther
        self.table_view_bd.setColumnWidth(3, 50)  # year
        self.table_view_bd.setColumnWidth(4, 45)  # month
        self.table_view_bd.setColumnWidth(5, 40)  # day
        self.table_view_bd.setColumnWidth(6, 80)  # ksiva
        self.table_view_bd.setColumnWidth(7, 120)  # city
        self.table_view_bd.setColumnWidth(8, 100)  # selsovet
        self.table_view_bd.setColumnWidth(9, 150)  # street
        self.table_view_bd.setColumnWidth(10, 40)  # house
        self.table_view_bd.setColumnWidth(11, 40)  # flat

    def init_combobox_zodiak(self):
        list_zodiak = ['', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы',
                       'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
        combobox_zodiak_model = QtCore.QStringListModel(list_zodiak)
        self.combobox_zodiak.setModel(combobox_zodiak_model)

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
