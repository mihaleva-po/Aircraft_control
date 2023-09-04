import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from main import time_session_KA, day, formatted_100


class Window_1(QMainWindow):
    def __init__(self):
        super(Window_1, self).__init__()

        self.setObjectName("MainWindow")
        self.resize(900, 600)
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap("./картинки/Аватарка.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setWindowIcon(icon)
        self.setToolTipDuration(1)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.button_seeting = QtWidgets.QPushButton(self.centralwidget)
        self.button_seeting.setGeometry(QtCore.QRect(200, 320, 471, 91))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_seeting.setFont(font)
        self.button_seeting.setObjectName("button_seeting")

        self.button_seeting.setStyleSheet("background-color : black; color: "
                                          "white")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 100, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_3.setStyleSheet("background-color : black; color: white")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 100, 161, 51))
        self.label_2.setMaximumSize(QtCore.QSize(161, 51))
        self.label_2.setSizeIncrement(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_2.setStyleSheet("background-color : black; color: white")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(250, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhMultiLine)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(650, 100, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhMultiLine)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_2.raise_()
        self.button_seeting.raise_()
        self.label_3.raise_()
        self.plainTextEdit.raise_()
        self.plainTextEdit_2.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # Обои
        palette = QPalette()
        palette.setBrush(QPalette.Background,
                         QBrush(QPixmap("./картинки/1_form.jpg")))
        self.setPalette(palette)

        # Нажатие кнопки
        self.button_seeting.clicked.connect(self.onclick)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Расписание сеансов КА"))
        self.button_seeting.setText(_translate("MainWindow", "Просмотр расписания сеансов"))
        self.label_3.setText(_translate("MainWindow", "Количество НКУ"))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_2.setText(_translate("MainWindow", "Количество КА"))
        self.label_2.setAlignment(Qt.AlignCenter)


    def onclick(self):
        global kolvo_HKY
        global kolvo_KA

        kolvo_HKY = form.plainTextEdit.toPlainText()
        kolvo_KA = form.plainTextEdit_2.toPlainText()

        if kolvo_HKY == "":
            kolvo_HKY = 0
        else:
            kolvo_HKY = int(kolvo_HKY)

        if kolvo_KA == "":
            kolvo_KA = 0
        else:
            kolvo_KA = int(kolvo_KA)

        self.vvod(kolvo_HKY, kolvo_KA)

    # Проверка введенных данных на корректность
    def vvod(self, kolvo_HKY, kolvo_KA):
        # Ввод данных
        if (kolvo_HKY == 0 and kolvo_KA == 0):
            self.error_1()

        elif kolvo_HKY == 0:
            self.error_2()

        elif kolvo_KA == 0:
            self.error_3()

        elif (kolvo_KA > 26):
            self.error_4()

        elif kolvo_KA <= 1:
            self.error_5()

        elif (type(kolvo_HKY) == int and type(kolvo_KA) == int
              and kolvo_KA <= 26 and kolvo_KA > 1):
            calculate()
            form.close()
            open_form2()


    def error_1(self):
        error = QMessageBox()
        error.setWindowTitle("Предупреждение!")
        error.setText("Вы не ввели количество НКУ и КА!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def error_2(self):
        error = QMessageBox()
        error.setWindowTitle("Предупреждение!")
        error.setText("Вы не ввели количество НКУ!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def error_3(self):
        error = QMessageBox()
        error.setWindowTitle("Предупреждение!")
        error.setText("Вы не ввели количество КА!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def error_4(self):
        error = QMessageBox()
        error.setWindowTitle("Предупреждение!")
        error.setText("Количество КА должно быть не больше 26!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def error_5(self):
        error = QMessageBox()
        error.setWindowTitle("Предупреждение!")
        error.setText("Количество КА должно быть больше 1!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()


class Window_2(QMainWindow):
    def __init__(self):
        super(Window_2, self).__init__()

        self.setObjectName("MainWindow")
        self.resize(800, 785)
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap("./картинки/Аватарка.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setWindowIcon(icon)
        self.setToolTipDuration(1)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 0, 121, 50))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color : black; color: "
                                          "white")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(130, 0, 171, 50))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color : black; color: "
                                          "white")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(300, 0, 231, 50))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-color : black; color: "
                                          "white")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(540, 0, 221, 50))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background-color : black; color: "
                                          "white")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 781, 50))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 781, 50))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 781, 50))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 240, 781, 50))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 300, 781, 50))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 360, 781, 50))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 420, 781, 50))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 480, 781, 50))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 540, 781, 50))
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(10, 600, 781, 50))
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(210, 670, 93, 51))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("картинки/стрелка2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 670, 93, 51))
        self.pushButton_2.setText("")

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 730, 141, 41))
        self.pushButton_3.setText("Следующий день")


        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("картинки/стр.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.click_right)
        self.pushButton.clicked.connect(self.click_left)
        self.pushButton_3.clicked.connect(self.next_day)

        # Обои
        palette = QPalette()
        palette.setBrush(QPalette.Background,
                         QBrush(QPixmap("./картинки/IMG_8717.webp")))
        self.setPalette(palette)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Расписание сеансов КА"))
        self.label.setText(_translate("MainWindow", "Номер КА"))
        self.label_2.setText(_translate("MainWindow", "Номер НКУ"))
        self.label_3.setText(_translate("MainWindow", "Начало сеанса управления"))
        self.label_4.setText(_translate("MainWindow", "Конец сеанса управления"))

    def next_day(self):
        open_form2()


    def click_right(self):
        number_form()


    def end_spisok(self):
        error = QMessageBox()
        error.setWindowTitle("Информация!")
        error.setText("Это последние данные на выбранный день!")
        error.setIcon(QMessageBox.Information)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def end_spisok2(self):
        error = QMessageBox()
        error.setWindowTitle("Информация!")
        error.setText("Вы в самом начале!")
        error.setIcon(QMessageBox.Information)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()


    def click_left(self):
        number_form2()


    def output_text_2(self):
        line = calculate()

        self.lineEdit.setText(str(line[0]))
        self.lineEdit_2.setText(str(line[1]))
        self.lineEdit_3.setText(str(line[2]))
        self.lineEdit_4.setText(str(line[3]))
        self.lineEdit_5.setText(str(line[4]))
        self.lineEdit_6.setText(str(line[5]))
        self.lineEdit_7.setText(str(line[6]))
        self.lineEdit_8.setText(str(line[7]))
        self.lineEdit_9.setText(str(line[8]))
        self.lineEdit_10.setText(str(line[9]))



    def output_text_3(self):
        line = calculate()

        self.lineEdit.setText(line[10])
        self.lineEdit_2.setText(line[11])
        self.lineEdit_3.setText(line[12])
        self.lineEdit_4.setText(line[13])
        self.lineEdit_5.setText(line[14])
        self.lineEdit_6.setText(line[15])
        self.lineEdit_7.setText(line[16])
        self.lineEdit_8.setText(line[17])
        self.lineEdit_9.setText(line[18])
        self.lineEdit_10.setText(line[19])

    def output_text_4(self):
        line = calculate()

        self.lineEdit.setText(line[20])
        self.lineEdit_2.setText(line[21])
        self.lineEdit_3.setText(line[22])
        self.lineEdit_4.setText(line[23])
        self.lineEdit_5.setText(line[24])
        self.lineEdit_6.setText(line[25])
        self.lineEdit_7.setText(line[26])
        self.lineEdit_8.setText(line[27])
        self.lineEdit_9.setText(line[28])
        self.lineEdit_10.setText(line[29])


    def output_text_5(self):
        line = calculate()

        self.lineEdit.setText(line[30])
        self.lineEdit_2.setText(line[31])
        self.lineEdit_3.setText(line[32])
        self.lineEdit_4.setText(line[33])
        self.lineEdit_5.setText(line[34])
        self.lineEdit_6.setText(line[35])
        self.lineEdit_7.setText(line[36])
        self.lineEdit_8.setText(line[37])
        self.lineEdit_9.setText(line[38])
        self.lineEdit_10.setText(line[39])


    def output_text_6(self):
        line = calculate()

        self.lineEdit.setText(line[40])
        self.lineEdit_2.setText(line[41])
        self.lineEdit_3.setText(line[42])
        self.lineEdit_4.setText(line[43])
        self.lineEdit_5.setText(line[44])
        self.lineEdit_6.setText(line[45])
        self.lineEdit_7.setText(line[46])
        self.lineEdit_8.setText(line[47])
        self.lineEdit_9.setText(line[48])
        self.lineEdit_10.setText(line[49])


def calculate():
    line = formatted_100(day(kolvo_HKY, kolvo_KA, time_session_KA(kolvo_KA)))
    return line

def number_form2():
    if num == 2:
        form2.end_spisok2()

    elif num == 3:
        form3.close()
        open_form2()

    elif num == 4:
        form4.close()
        open_form3()

    elif num == 5:
        form5.close()
        open_form4()

    elif num == 6:
        form6.close()
        open_form5()


def number_form():
    if num == 2:
        form2.close()
        open_form3()

    elif num == 3:
        form3.close()
        open_form4()

    elif num == 4:
        form4.close()
        open_form5()

    elif num == 5:
        form5.close()
        open_form6()

    elif num == 6:
        form6.end_spisok()


def open_form1():
    global num
    num = 1
    app = QApplication(sys.argv)
    global form
    form = Window_1()
    form.show()
    sys.exit(app.exec_())


def open_form2():
    global form2
    global num
    num = 2
    form2 = Window_2()
    form2.output_text_2()
    form2.show()


def open_form3():
    global form3
    global num
    num = 3
    form3 = Window_2()
    form3.output_text_3()
    form3.show()


def open_form4():
    global form4
    global num
    num = 4
    form4 = Window_2()
    form4.output_text_4()
    form4.show()


def open_form5():
    global form5
    global num
    num = 5
    form5 = Window_2()
    form5.output_text_5()
    form5.show()


def open_form6():
    global form6
    global num
    num = 6
    form6 = Window_2()
    form6.output_text_6()
    form6.show()


if __name__ == "__main__":
    num = 1
    open_form1()


