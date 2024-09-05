import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QCheckBox
from checkboxesArea.checkboxesArea import CheckboxesArea  # 引入 CheckboxesArea
from fornPage.fornPage import FrontPage  # 引入其他 UI 組件
from drugForm.drugPage import DrugForm  # 引入 drugPage 的 FormWidget

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

        # 創建並添加 DrugForm 中的 FormWidget 表單
        self.form_widget = DrugForm()
        self.main_layout.addWidget(self.form_widget)

        # 創建輸出按鈕
        self.output_button = QPushButton("輸出")
        self.output_button.clicked.connect(self.output_data)  # 綁定按鈕點擊事件
        self.main_layout.addWidget(self.output_button)

        # 設置佈局
        self.setLayout(self.main_layout)

    def output_data(self):
        """當按下輸出按鈕時，取得所有表單的數據並呼叫函數處理"""
        # 從 FrontPage 取得表單數據
        form_data = self.front_page.get_form_data()  # 假設 FrontPage 有一個 get_form_data 函數
        print("FrontPage 表單數據:", form_data)

        # 從 CheckboxesArea 取得勾選框的選擇
        checkboxes_data = self.get_checkboxes_data()
        print("CheckboxesArea 勾選框選擇:", checkboxes_data)

        # 從 DrugForm 取得四行五列的表單數據
        drug_data = self.form_widget.get_form_data()
        print("DrugForm 藥物數據 (四行五列):", drug_data)

        # 將所有表單數據保存或進行其他處理
        self.save_data(form_data, checkboxes_data, drug_data)

    def get_checkboxes_data(self):
        """從 CheckboxesArea 中取得複選框狀態"""
        checkboxes_status = {}
        for checkbox in self.checkboxes_area.findChildren(QCheckBox):
            checkboxes_status[checkbox.text()] = checkbox.isChecked()
        return checkboxes_status

    def save_data(self, form_data, checkboxes_data, drug_data):
        """處理和保存資料的函數"""
        # 這裡是保存或處理資料的邏輯
        # 可以將資料輸出到檔案、傳送到伺服器，或者顯示在介面上
        print("保存數據:")
        print("FrontPage:", form_data)
        print("CheckboxesArea:", checkboxes_data)
        print("DrugForm:", drug_data)

def main():
    app = QApplication([])

    # 創建主視窗
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
