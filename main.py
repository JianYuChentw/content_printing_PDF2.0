import sys,os
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QCheckBox, QScrollArea, QMessageBox
from PyQt6.QtGui import QIcon, QFont
from checkboxesArea.checkboxesAreaServise import CheckboxesAreaServise  # 引入 CheckboxesAreaServise
from checkboxesArea.checkboxesAreaItem import CheckboxesAreaItem  # 引入 CheckboxesAreaItem
from fornPage.fornPage import FrontPage  # 引入其他 UI 組件
from drugForm.drugPage import DrugForm  # 引入 drugPage 的 FormWidget
from todoArea.todoArea import TodoArea  # 引入新的 TodoArea
from service import generate_pdf_with_chinese

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("三聯單輸出工具")
        base_dir = os.path.dirname(sys.executable)
        imgPath = os.path.join(base_dir, 'save/form96.png')
        self.setWindowIcon(QIcon(imgPath))  # 設置圖標路徑
        # 設置視窗的寬高，例如850x800
        self.resize(850, 750)

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
        self.output_button.setStyleSheet(
            "background-color: #02C874; color: black; border-radius:5px;"  # 設置背景顏色和文字顏色
        )
        self.output_button.setFixedHeight(50)
        font = QFont("Arial", 18)
        self.output_button.setFont(font)
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
        # print("FrontPage 表單數據:", form_data)

        # 檢查發票標題和日期是否為空
        if not form_data.get('invoice_title') or not form_data.get('date'):
            QMessageBox.warning(self, "錯誤", "發票抬頭和日期不得為空！")
            return  # 終止輸出

        # 從 CheckboxesAreaServise 取得勾選框的選擇
        checkboxes_data = self.get_checkboxes_data()
        # print("CheckboxesAreaServise 勾選框選擇:", checkboxes_data)

        # 從 DrugForm 取得四行五列的表單數據
        drug_data = self.form_widget.get_form_data()
        # print("DrugForm 藥物數據 (四行五列):", drug_data)

        # 從 CheckboxesAreaItem 取得勾選框的選擇
        checkboxes_item_data = self.get_checkboxes_item_data()
        # print(" 勾選框選擇:", checkboxes_item_data)

        # 從 TodoArea 取得輸入數據
        todo_data = self.todo_area.get_todo_data()
        # print("TodoArea 輸入數據:", todo_data)

        # 將所有表單數據保存或進行其他處理
        self.output(form_data, checkboxes_data, drug_data, checkboxes_item_data, todo_data)

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

    def output(self, form_data, checkboxes_data, drug_data, checkboxes_item_data, todo_data):
        """處理和保存資料的函數"""
        # 可以將資料輸出到檔案
        print("輸出檔案:")
        # print("FrontPage:", form_data)
        # print("CheckboxesArea:", checkboxes_data)
        # print("DrugForm:", drug_data)
        # print("CheckboxesAreaItem:", checkboxes_item_data)
        print("TodoArea:", todo_data)
        customer_info = {
            'clientName':form_data['name'], 
            'billName': form_data['invoice_title'],
            'invoiceNumber': form_data['tax_id'],
            'clientPhone': form_data['phone'],
            'clientContactPerson': form_data['contact_person'],
            'constructionPersonInCharge': form_data['window'],
            'constructionPersonInChargePhone':form_data['window_phone'], 
            'constructionDate': form_data['date'],
            'constructionAddress': form_data['address'],
            'construction': form_data['frequency'],
            'monthly': form_data['monthly'],
            'quarterly': form_data['quarterly'],
            'yearly': form_data['halfyear'],
            'pestControl':checkboxes_data['一般害蟲防治 – Pest Control'] ,
            'fleasControl': checkboxes_data['白蟻防治 – Termite Control'],
            'temiteControl': checkboxes_data['鼠害防治 – Rodent Control'],
            'powerControl': checkboxes_data['跳蚤防治 – Fleas Control'],
            'rodentControl': checkboxes_data['粉狀蛀蟲防治 – Powder Post Beetle'],
            'otrher': checkboxes_data['其他 – Others'],
            'drug1_1': drug_data[0][0],
            'drug1_2': drug_data[0][1],
            'drug1_3': drug_data[0][2],
            'drug1_4': drug_data[0][3],
            'drug1_5': drug_data[0][4],
            'drug2_1': drug_data[1][0],
            'drug2_2': drug_data[1][1],
            'drug2_3': drug_data[1][2],
            'drug2_4': drug_data[1][3],
            'drug2_5': drug_data[1][4],
            'drug3_1': drug_data[2][0],
            'drug3_2': drug_data[2][1],
            'drug3_3': drug_data[2][2],
            'drug3_4': drug_data[2][3],
            'drug3_5': drug_data[2][4],
            'drug4_1': drug_data[3][0],
            'drug4_2': drug_data[3][1],
            'drug4_3': drug_data[3][2],
            'drug4_4': drug_data[3][3],
            'drug4_5': drug_data[3][4],

            'pestControlL1_1': checkboxes_item_data['手提式噴灑器'],
            'pestControlL1_2': checkboxes_item_data['電動式噴灑器'],
            'pestControlL1_3': checkboxes_item_data['中型電動式噴灑器'],
            'pestControlL1_4': checkboxes_item_data['大型氣動式噴灑器'],
            'pestControlL1_5': checkboxes_item_data['動力式噴灑機'],
            'pestPaper':checkboxes_item_data.get('更換捕蟲紙數量', ""),

            'pestControlR1_1': checkboxes_item_data['微粒子空間冷霧機'],
            'pestControlR1_2': checkboxes_item_data['熱霧機'],
            'pestControlR1_3': checkboxes_item_data['蟑螂餌膠'],
            'pestControlR1_4': checkboxes_item_data['縫隙處理機'],
            'pestControlR1_5': checkboxes_item_data['更換捕蟲紙'],

            'mouseControlL1_1': checkboxes_item_data['檢視老鼠入侵點'],
            'mouseControlL1_2': checkboxes_item_data['檢視鼠跡狀況'],
            'mouseControlL1_3': checkboxes_item_data['補充或更換餌劑'],
            'mouseControlL1_4': checkboxes_item_data['補充、更換或新增鼠板'],
            'mouseControlL1_5': checkboxes_item_data['鼠洞封阻工程'],

            'mouseControlR1_1': checkboxes_item_data['設計老鼠活動路徑'],
            'mouseControlR1_2': checkboxes_item_data['施用忌避劑'],
            'mouseControlR1_3': checkboxes_item_data['捕獲老鼠'],
            'mouseQuantity': checkboxes_item_data.get('捕獲老鼠數量', ""),


            'mouseControlR1_4': checkboxes_item_data['除臭、除菌處理'],
            'mouseControlR1_5': checkboxes_item_data['架設震動或超音波器'],


            'todoList': todo_data['交辦事項'],
            'workReport': todo_data['工作報告'],
            'technician': todo_data['技術員'],
            'pharmaceuticalTechnician': todo_data['施藥人員'],
        }

        generate_pdf_with_chinese(customer_info)
        # 彈出完成訊息框
        QMessageBox.information(self, "完成", "資料已成功輸出！")
        self.clear_all_inputs()
    
    def clear_all_inputs(self):
        """清空所有表單和勾選框的內容"""
        # 清空 FrontPage 表單
        self.front_page.clear_form()  

        # 清空 CheckboxesAreaServise 中的複選框
        self.checkboxes_area.clear_checkboxes()


        # 清空 DrugForm 的表單內容
        self.form_widget.clear_form()  

        # 清空 CheckboxesAreaItem 的複選框及輸入框
        self.checkboxes_item_area.clear_checkboxes()

        # 清空 TodoArea 的輸入框
        self.todo_area.clear_inputs()  

def main():
    app = QApplication([])
    base_dir = os.path.dirname(sys.executable)
    imgPath = os.path.join(base_dir, 'save/form96.png')
    app.setWindowIcon(QIcon(imgPath))

    # 創建主視窗
    main_window = MainWindow()
    
    # 設置視窗寬高
    main_window.resize(850, 800)  # 或使用 main_window.setFixedSize(850, 800)
    
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
