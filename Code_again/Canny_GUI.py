
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d
import cv2
import sys
import os
from PIL import Image
from io import BytesIO

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1384, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(740, 140, 641, 651))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 10, 221, 41))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 581, 561))
        self.pushButton_10 = QPushButton(self.groupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(450, 10, 131, 41))
        self.pushButton_11 = QPushButton(self.groupBox)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(40, 10, 131, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 0, 891, 121))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 130, 711, 651))
        self.Select = QWidget()
        self.Select.setObjectName(u"Select")
        self.pushButton = QPushButton(self.Select)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 30, 181, 61))
        self.pushButton_2 = QPushButton(self.Select)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 160, 181, 61))
        self.pushButton_3 = QPushButton(self.Select)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 290, 181, 61))
        self.tabWidget.addTab(self.Select, "")
        self.sosanh = QWidget()
        self.sosanh.setObjectName(u"sosanh")
        self.pushButton_4 = QPushButton(self.sosanh)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 30, 181, 61))
        self.pushButton_5 = QPushButton(self.sosanh)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 180, 181, 61))
        self.pushButton_6 = QPushButton(self.sosanh)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(30, 310, 181, 61))
        self.tabWidget.addTab(self.sosanh, "")
        self.congthuc = QWidget()
        self.congthuc.setObjectName(u"congthuc")
        self.pushButton_7 = QPushButton(self.congthuc)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(30, 30, 181, 61))
        self.pushButton_8 = QPushButton(self.congthuc)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(30, 290, 181, 61))
        self.pushButton_9 = QPushButton(self.congthuc)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(30, 160, 181, 61))
        self.tabWidget.addTab(self.congthuc, "")
        self.histogram = QWidget()
        self.histogram.setObjectName(u"histogram")
        self.pushButton_12 = QPushButton(self.histogram)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(210, 10, 261, 41))
        self.label_4 = QLabel(self.histogram)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 80, 651, 511))
        self.tabWidget.addTab(self.histogram, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1384, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">H\u00ecnh \u1ea3nh hi\u1ec3n th\u1ecb</span></p></body></html>", None))
        self.label_3.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"T\u1ea3i h\u00ecnh \u1ea3nh", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Gray Scale", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">Tr\u01b0\u1eddng \u0110\u1ea1i H\u1ecdc C\u00f4ng Ngh\u1ec7 TP.HCM-HUTECH</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#00aaff;\">L\u1edbp: 22DRTA1 - Robot v\u00e0 Tr\u00ed tu\u1ec7 Nh\u00e2n t\u1ea1o</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#00aaff;\">2286300010- Nguy\u1ec5n V\u0103n \u0110\u1ea1t 2286300028-Hu\u1ef3nh Long 2286300020-Nguy\u1ec5n Ch\u1ea5n Huy </span><br/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Prewitt", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Select), QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ph\u01b0\u01a1ng ph\u00e1p", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Prewitt - Sobel", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Prewitt-Canny", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Canny-Sobel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sosanh), QCoreApplication.translate("MainWindow", u"So s\u00e1nh ph\u01b0\u01a1ng ph\u00e1p", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Prewitt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.congthuc), QCoreApplication.translate("MainWindow", u"C\u00f4ng th\u1ee9c", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Hi\u1ec7n histogram ", None))
        self.label_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histogram), QCoreApplication.translate("MainWindow", u"Histogram", None))
    # retranslateUi

class ConsoleMainWindow(QMainWindow):
    def __init__(self):
        super(ConsoleMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_image = None

        # Kết nối các nút bấm
        self.ui.pushButton_10.clicked.connect(self.load_image)
        self.ui.pushButton_11.clicked.connect(self.convert_to_grayscale)
        self.ui.pushButton_12.clicked.connect(self.histogram_show)  # Kết nối nút pushButton_12

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Chọn hình ảnh",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.tif)"
        )

        if not file_path:
            return

        # Đọc hình ảnh và hiển thị
        self.current_image = cv2.imread(file_path)
        if self.current_image is not None:
            # Chuyển ảnh sang RGB vì OpenCV sử dụng BGR
            image = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.ui.label_3.setPixmap(pixmap.scaled(self.ui.label_3.size(), Qt.KeepAspectRatio))

    def convert_to_grayscale(self):
        if self.current_image is None:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có hình ảnh được tải.")
            return

        # Chuyển đổi sang grayscale
        gray_image = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
        height, width = gray_image.shape
        bytes_per_line = width
        q_image = QImage(gray_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(q_image)
        self.ui.label_3.setPixmap(pixmap.scaled(self.ui.label_3.size(), Qt.KeepAspectRatio))

    def histogram_show(self):
        """Hiển thị histogram của ảnh hiện tại lên label_4"""
        if self.current_image is None:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có hình ảnh được tải.")
            return

        # Chuyển sang grayscale nếu cần
        if len(self.current_image.shape) == 3:  # Nếu ảnh không phải grayscale
            gray_image = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = self.current_image

        # Tính histogram
        hist, bins = np.histogram(gray_image.ravel(), bins=256, range=[0, 256])

        # Vẽ histogram với matplotlib
        plt.figure(figsize=(4, 3), dpi=100)
        plt.plot(hist, color='blue')
        plt.title("Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.grid(True)

        # Chuyển biểu đồ sang ảnh QPixmap
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        # Chuyển đổi ảnh từ buffer sang QPixmap
        pil_image = Image.open(buf)
        qt_image = QImage(pil_image.tobytes(), pil_image.width, pil_image.height, pil_image.mode)
        pixmap = QPixmap.fromImage(qt_image)

        # Hiển thị lên label_4
        self.ui.label_4.setPixmap(pixmap)
        self.ui.label_4.setScaledContents(True)

if __name__ == "__main__":
    os.environ["QT_NO_EUDC_FONTS"] = "1"  # Tắt EUDC fonts
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial", 12))  # Đặt phông chữ mặc định
    main = ConsoleMainWindow()
    main.show()  # Gọi show() đúng cách
    sys.exit(app.exec_())


if __name__ == "__main__":
    os.environ["QT_NO_EUDC_FONTS"] = "1"  # Tắt EUDC fonts
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial", 12))  # Đặt phông chữ mặc định
    main = ConsoleMainWindow()
    main.show()  # Gọi show() đúng cách
    sys.exit(app.exec_())
