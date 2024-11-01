from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from laba2 import ImageIterator
from laba2.ImageIterator import Iterator


class Ui_MainWindow(object):
    def __init__(self):
        self.file_name = None
        self.iterator = None
        self.image_iter = None

    def setupUi(self, MainWindow: QtWidgets.QMainWindow)->None:
        """
        Sets up the main UI components of the MainWindow
        :param MainWindow: The main window instance where UI elements are added
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button_forward = QtWidgets.QPushButton(self.centralwidget)
        self.button_forward.setGeometry(QtCore.QRect(90, 700, 170, 70))
        self.button_forward.setStyleSheet("background-color: rgb(114, 147, 255)")
        self.button_forward.setObjectName("forward")
        self.button_forward.clicked.connect(self.show_next_img)

        self.select_file = QtWidgets.QPushButton(self.centralwidget)
        self.select_file.setGeometry(QtCore.QRect(1340, 700, 170, 70))
        self.select_file.setStyleSheet("background-color: rgb(114, 147, 255)")
        self.select_file.setObjectName("select_file")
        self.select_file.clicked.connect(self.open_file_dialog)

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 10, 1580, 680))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("istockphoto-1442799465-640x640.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow)->None:
        """
        Sets the text for UI elements, allowing for translations.
        :param MainWindow: The main window instance where UI elements are added
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.button_forward.setText(_translate("MainWindow","forward"))
        self.select_file.setText(_translate("MainWindow", "Select file"))


    def get_images(self)->list:
        """
        #Gets paths to images
        #:return: list of relative paths to images from csv file
        """
        self.data = ImageIterator.Iterator(self.file_name)
        img = []
        for row in self.data:
            img.append(row[1])
        return img


    def open_file_dialog(self)->None:
        """
        #Allows to select specific csv file by pressing clicking the desired button
        """
        options = QtWidgets.QFileDialog.Options()
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите изображение", "",
                                                             "CSV Files (*.csv)", options=options)
        if not self.file_name: return

        self.img = self.get_images()
        self.load_image(0)
        self.init_iterator()

    def init_iterator(self):
        self.iterator = Iterator(self.file_name)
        self.image_iter = iter(self.iterator)

    def show_next_img(self)->None:
        """
        Displays the next image from selected csv file
        """
        if self.file_name == None:
            self.msg_box = QMessageBox()
            self.msg_box.setText("The list of the images is empty")
            self.msg_box.move(450, 700)
            self.msg_box.resize(170, 70)

            self.msg_box.exec_()
            return

        try:
            row = next(self.image_iter)
            image_path = row[1]
            self.photo.setPixmap(QtGui.QPixmap(image_path))

        except StopIteration:
            self.init_iterator()
            row = next(self.image_iter)
            image_path = row[1]
            self.photo.setPixmap(QtGui.QPixmap(image_path))



    def load_image(self, count)->None:
        """
        #Displays the image on the screen
        #:param count: the index of current image
        """
        if len(self.img) == 0:
            self.msg_box = QMessageBox()
            self.msg_box.setText("The list of the images is empty")
            self.msg_box.move(450, 700)
            self.msg_box.resize(170, 70)

            self.msg_box.exec_()
            return
        image_path=self.img[count]
        self.photo.setPixmap(QtGui.QPixmap(image_path))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
