import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QCheckBox, QScrollArea, QMessageBox
from checkboxesArea.checkboxesAreaServise import CheckboxesAreaServise  # 引入 CheckboxesAreaServise
from checkboxesArea.checkboxesAreaItem import CheckboxesAreaItem  # 引入 CheckboxesAreaItem
from fornPage.fornPage import FrontPage  # 引入其他 UI 組件
from drugForm.drugPage import DrugForm  # 引入 drugPage 的 FormWidget
from todoArea.todoArea import TodoArea  # 引入新的 TodoArea

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 設置視窗的寬高，例如850x800
        self.resize(850, 800)

        # 創建主佈局
        self.main_layout = QVBoxLayout()

        # 創建滾動區域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # 設置滾動區域大小自適應

        # 創建滾動區域內的主窗口
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        # 創建並添加 FrontPage 組件
        self.front_page = FrontPage()
        self.scroll_layout.addWidget(self.front_page)

        # 創建並添加 CheckboxesAreaServise 組件
        self.checkboxes_area = CheckboxesAreaServise()
        self.scroll_layout.addWidget(self.checkboxes_area)

        # 創建並添加 DrugForm 中的 FormWidget 表單
        self.form_widget = DrugForm()
        self.scroll_layout.addWidget(self.form_widget)

        # 創建並添加 CheckboxesAreaItem 組件
        self.checkboxes_item_area = CheckboxesAreaItem()
        self.scroll_layout.addWidget(self.checkboxes_item_area)

        # 創建並添加 TodoArea 組件
        self.todo_area = TodoArea()
        self.scroll_layout.addWidget(self.todo_area)

        # 創建輸出按鈕
        self.output_button = QPushButton("輸出")
        self.output_button.clicked.connect(self.output_data)  # 綁定按鈕點擊事件
        self.scroll_layout.addWidget(self.output_button)

        # 設置滾動區域的 widget
        self.scroll_area.setWidget(self.scroll_widget)

        # 將滾動區域添加到主佈局中
        self.main_layout.addWidget(self.scroll_area)

        # 設置主窗口佈局
        self.setLayout(self.main_layout)

    def output_data(self):
        """當按下輸出按鈕時，取得所有表單的數據並呼叫函數處理"""
        # 從 FrontPage 取得表單數據
        form_data = self.front_page.get_form_data()  # 假設 FrontPage 有一個 get_form_data 函數
        print("FrontPage 表單數據:", form_data)

        # 檢查發票標題和日期是否為空
        if not form_data.get('invoice_title') or not form_data.get('date'):
            QMessageBox.warning(self, "錯誤", "發票抬頭和日期不得為空！")
            return  # 終止輸出

        # 從 CheckboxesAreaServise 取得勾選框的選擇
        checkboxes_data = self.get_checkboxes_data()
        print("CheckboxesAreaServise 勾選框選擇:", checkboxes_data)

        # 從 DrugForm 取得四行五列的表單數據
        drug_data = self.form_widget.get_form_data()
        print("DrugForm 藥物數據 (四行五列):", drug_data)

        # 從 CheckboxesAreaItem 取得勾選框的選擇
        checkboxes_item_data = self.get_checkboxes_item_data()
        print("CheckboxesAreaItem 勾選框選擇:", checkboxes_item_data)

        # 從 TodoArea 取得輸入數據
        todo_data = self.todo_area.get_todo_data()
        print("TodoArea 輸入數據:", todo_data)

        # 將所有表單數據保存或進行其他處理
        self.save_data(form_data, checkboxes_data, drug_data, checkboxes_item_data, todo_data)

    def get_checkboxes_data(self):
        """從 CheckboxesAreaServise 中取得複選框狀態"""
        checkboxes_status = {}
        for checkbox in self.checkboxes_area.findChildren(QCheckBox):
            checkboxes_status[checkbox.text()] = checkbox.isChecked()
        return checkboxes_status

    def get_checkboxes_item_data(self):
        """從 CheckboxesAreaItem 中取得複選框狀態"""
        checkboxes_item_status = {}
        for checkbox in self.checkboxes_item_area.findChildren(QCheckBox):
            checkboxes_item_status[checkbox.text()] = checkbox.isChecked()

        # 取得 '更換捕蟲紙' 和 '捕獲老鼠' 的數值
        trap_paper_value = self.checkboxes_item_area.trap_paper_input.text() if self.checkboxes_item_area.trap_paper_checkbox.isChecked() else None
        catch_mouse_value = self.checkboxes_item_area.catch_mouse_input.text() if self.checkboxes_item_area.catch_mouse_checkbox.isChecked() else None

        if trap_paper_value:
            checkboxes_item_status['更換捕蟲紙數量'] = trap_paper_value
        if catch_mouse_value:
            checkboxes_item_status['捕獲老鼠數量'] = catch_mouse_value

        return checkboxes_item_status

    def save_data(self, form_data, checkboxes_data, drug_data, checkboxes_item_data, todo_data):
        """處理和保存資料的函數"""
        # 這裡是保存或處理資料的邏輯
        # 可以將資料輸出到檔案、傳送到伺服器，或者顯示在介面上
        print("保存數據:")
        print("FrontPage:", form_data)
        print("CheckboxesArea:", checkboxes_data)
        print("DrugForm:", drug_data)
        print("CheckboxesAreaItem:", checkboxes_item_data)
        print("TodoArea:", todo_data)

def main():
    app = QApplication([])

    # 創建主視窗
    main_window = MainWindow()
    
    # 設置視窗寬高
    main_window.resize(850, 800)  # 或使用 main_window.setFixedSize(850, 800)
    
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
