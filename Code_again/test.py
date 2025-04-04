from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Qt
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Thiết lập cửa sổ chính
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        
        # Tạo widget trung tâm
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Tạo layout
        self.layout = QVBoxLayout(self.centralwidget)
        
        # Tạo các nút pushButton
        self.pushButton1 = QPushButton("Mở các nút khác", self.centralwidget)
        self.pushButton2 = QPushButton("Nút 2", self.centralwidget)
        self.pushButton3 = QPushButton("Nút 3", self.centralwidget)
        
        # Thêm các nút vào layout
        self.layout.addWidget(self.pushButton1)
        self.layout.addWidget(self.pushButton2)
        self.layout.addWidget(self.pushButton3)
        
        # Đặt thuộc tính ẩn cho pushButton2 và pushButton3
        self.pushButton2.setVisible(False)
        self.pushButton3.setVisible(False)
        
        MainWindow.setCentralWidget(self.centralwidget)

        # Kết nối nút với sự kiện
        self.pushButton1.clicked.connect(self.show_other_buttons)

    def show_other_buttons(self):
        # Hiển thị các nút còn lại khi nút pushButton1 được nhấn
        self.pushButton2.setVisible(True)
        self.pushButton3.setVisible(True)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
