import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QCheckBox
from checkboxesArea.checkboxesArea import CheckboxesArea  # 引入 CheckboxesArea
from fornPage.fornPage import FrontPage  # 引入其他 UI 組件

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 創建主佈局
        self.main_layout = QVBoxLayout()

        # 創建並添加 FrontPage 組件
        self.front_page = FrontPage()
        self.main_layout.addWidget(self.front_page)

        # 創建並添加 CheckboxesArea 組件
        self.checkboxes_area = CheckboxesArea()
        self.main_layout.addWidget(self.checkboxes_area)

        # 創建輸出按鈕
        self.output_button = QPushButton("輸出")
        self.output_button.clicked.connect(self.output_data)  # 綁定按鈕點擊事件
        self.main_layout.addWidget(self.output_button)

        # 設置佈局
        self.setLayout(self.main_layout)

    def output_data(self):
        """當按下輸出按鈕時，取得資料並呼叫函數處理"""
        # 從 FrontPage 取得表單數據
        form_data = self.front_page.get_form_data()  # 假設 FrontPage 有一個 get_form_data 函數
        print("表單數據:", form_data)

        # 從 CheckboxesArea 取得勾選框的選擇
        checkboxes_data = self.get_checkboxes_data()
        print("勾選框選擇:", checkboxes_data)

        # 你可以在這裡將表單和勾選框的數據進行進一步處理，例如呼叫保存或輸出函數
        self.save_data(form_data, checkboxes_data)

    def get_checkboxes_data(self):
        """從 CheckboxesArea 中取得複選框狀態"""
        checkboxes_status = {}
        for checkbox in self.checkboxes_area.findChildren(QCheckBox):
            checkboxes_status[checkbox.text()] = checkbox.isChecked()
        return checkboxes_status

    def save_data(self, form_data, checkboxes_data):
        """處理和保存資料的函數"""
        # 這裡是保存或處理資料的邏輯
        # 可以將資料輸出到檔案、傳送到伺服器，或者顯示在介面上
        print("保存數據:", form_data, checkboxes_data)

def main():
    app = QApplication([])

    # 創建主視窗
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
