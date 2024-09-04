import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from fornPage.fornPage import FrontPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('客戶資訊表單')
        self.setGeometry(100, 100, 600, 400)

        # 引入 FornPage 表單
        self.form_page = FrontPage()
        self.setCentralWidget(self.form_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
