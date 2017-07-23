from PyQt5 import QtWidgets, uic, QtCore, QtGui
import testQTBD_About
import testQTBD_controller


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi(r'./testBD.ui', self)
        QtWidgets.qApp.processEvents()
        self.table_model = QtGui.QStandardItemModel()
        self.combobox_zodiak_model = QtCore.QStringListModel()
        self.init_table_view_bd()
        self.init_combobox_zodiak()
        self.init_all_listeners()

    def init_all_listeners(self):
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionAbout.triggered.connect(self.show_about_form)
        self.push_button_clear.clicked.connect(self.clear_inputs_and_table)
        self.push_button_search.clicked.connect(self.update_into_table)
        self.actionReset.triggered.connect(self.clear_inputs_and_table)

    def init_table_view_bd(self):
        list_names_of_schema = ['Фамилия', 'Имя', 'Отчество',
                                'Год', 'Месяц', 'День',
                                'Документ', 'Город', 'Сельсовет',
                                'Улица', 'Дом', 'Кв.']
        self.table_model.setHorizontalHeaderLabels(list_names_of_schema)
        self.table_view_bd.setModel(self.table_model)
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

    def update_into_table(self):
        self.table_model.clear()
        text_family = self.edit_family.text()
        text_name = self.edit_name.text()
        text_farther = self.edit_farther.text()
        text_birthday_year = self.edit_birthday_year.text()
        text_birthday_month = self.edit_birthday_month.text()
        text_birthday_day = self.edit_birthday_day.text()
        text_ksiva = self.edit_ksiva.text()
        text_city = self.edit_city.text()
        text_selsovet = self.edit_selsovet.text()
        text_street = self.edit_street.text()
        text_house = self.edit_house.text()
        text_flat = self.edit_flat.text()
        # for row in testQTBD_controller.select_from_bd(text_family, text_name, text_farther,
        #                                               text_birthday_year, text_birthday_month, text_birthday_day,
        #                                               text_ksiva, text_city, text_selsovet,
        #                                               text_street, text_house, text_flat):
        #     self.table_model.appendRow([QtGui.QStandardItem(item) for item in row])
        for row in testQTBD_controller.select_all_from_bd():
            self.table_model.appendRow([QtGui.QStandardItem(item) for item in row])
        self.init_table_view_bd()

    def init_combobox_zodiak(self):
        list_zodiak = ['', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы',
                       'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
        self.combobox_zodiak_model = QtCore.QStringListModel(list_zodiak)
        self.combobox_zodiak.setModel(self.combobox_zodiak_model)

    def clear_inputs_and_table(self):
        self.table_model.clear()
        self.init_table_view_bd()
        self.edit_family.setText('')
        self.edit_name.setText('')
        self.edit_farther.setText('')
        self.edit_birthday_year.setText('')
        self.edit_birthday_month.setText('')
        self.edit_birthday_day.setText('')
        self.edit_ksiva.setText('')
        self.edit_city.setText('')
        self.edit_selsovet.setText('')
        self.edit_street.setText('')
        self.edit_house.setText('')
        self.edit_flat.setText('')
        self.combobox_zodiak.setCurrentIndex(0)
        self.check_box_interactive.setChecked(False)

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
