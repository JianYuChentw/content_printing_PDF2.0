from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QGroupBox,
    QHBoxLayout, QPushButton, QComboBox, QMessageBox, QCheckBox
)
from PyQt6.QtCore import Qt
import sys
from .components import InputWidget  # 確認引入 InputWidget 正確
from .customer_data import CustomerData  # 引入客戶資料操作模組
# from .checkboxes_area import CheckboxesArea  # 引入拆分出的勾選單區域

class FrontPage(QWidget):

    def __init__(self):
        super().__init__()

        # 創建客戶資料操作對象
        self.customer_data = CustomerData()

        # 創建頂部區域的下拉選單、輸入框和按鈕
        top_layout = QHBoxLayout()

        # 下拉選單
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.customer_data.get_all_customers())  # 從客戶資料中載入客戶
        self.dropdown.setFixedWidth(150)  # 設置下拉選單固定寬度
        self.dropdown.currentTextChanged.connect(self.fill_form_with_customer_info)  # 監聽選擇變更
        top_layout.addWidget(self.dropdown)

        # 新增用的輸入框
        self.add_input = QLineEdit()
        self.add_input.setPlaceholderText("輸入新增項目...")
        self.add_input.setFixedWidth(100)  # 設置輸入框的固定寬度
        top_layout.addWidget(self.add_input)

        # 按鈕
        add_button = QPushButton("新增")
        update_button = QPushButton("更新")
        delete_button = QPushButton("刪除")
        clear_button = QPushButton("清空當前內容")  # 清空按鈕

        # 設置按鈕寬度
        add_button.setFixedWidth(60)
        update_button.setFixedWidth(60)
        delete_button.setFixedWidth(60)
        clear_button.setFixedWidth(100)  # 設置清空按鈕寬度

        # 添加按鈕事件
        add_button.clicked.connect(self.add_customer)
        update_button.clicked.connect(self.update_customer)
        delete_button.clicked.connect(self.delete_customer)
        clear_button.clicked.connect(self.clear_form)  # 連接到清空函數

        # 添加按鈕到布局
        top_layout.addWidget(add_button)
        top_layout.addWidget(update_button)
        top_layout.addWidget(delete_button)
        top_layout.addWidget(clear_button)  # 添加清空按鈕到布局

        # 包裝 QHBoxLayout 進一個 QWidget，並設置為置中
        top_widget = QWidget()
        top_widget.setLayout(top_layout)
        top_widget.setFixedWidth(600)  # 設置與頂部相同的固定寬度

        # 使用 QVBoxLayout 將 top_layout 置中
        central_layout = QVBoxLayout()
        central_layout.addStretch(1)  # 添加彈性空間
        central_layout.addWidget(top_widget, alignment=Qt.AlignmentFlag.AlignCenter)  # 將 top_widget 置中
        central_layout.addStretch(1)  # 添加彈性空間

        # 使用 QGridLayout 來放置左右兩邊的表單元素
        grid_layout = QGridLayout()
        grid_layout.setVerticalSpacing(10)  # set

        # 表單元素
        self.name_input = InputWidget("", "客戶名稱", 250, 30, 30)
        self.invoice_input = InputWidget("", "發票抬頭", 250, 30, 30)
        self.tax_id_input = InputWidget("", "統一編號", 250, 30, 30)
        self.phone_input = InputWidget("", "電話", 250, 30, 30)
        self.contact_person_input = InputWidget("", "聯絡人", 250, 30, 30)

        # 左邊表單部分
        grid_layout.addWidget(self.name_input, 0, 0)
        grid_layout.addWidget(self.invoice_input, 1, 0)
        grid_layout.addWidget(self.tax_id_input, 2, 0)
        grid_layout.addWidget(self.phone_input, 3, 0)
        grid_layout.addWidget(self.contact_person_input, 4, 0)

        # 右邊表單部分
        self.window_input = InputWidget("", "施作聯絡窗口", 250, 30, 30)
        self.window_phone_input = InputWidget("", "施作窗口電話", 250, 30, 30)
        self.date_input = InputWidget("", "施工日期/時間", 250, 30, 30)
        self.address_input = InputWidget("", "施作地址", 300, 30, orientation="vertical")

        grid_layout.addWidget(self.window_input, 0, 1)
        grid_layout.addWidget(self.window_phone_input, 1, 1)
        grid_layout.addWidget(self.date_input, 2, 1)
        grid_layout.addWidget(self.address_input, 3, 1)

        # 創建一個 QGroupBox 來包裹 grid_layout
        form_group_box = QGroupBox("")
        form_group_box.setLayout(grid_layout)

        # 創建施工頻率選擇區域
        frequency_layout = QHBoxLayout()
        frequency_label = QLabel("施工頻率:")
        frequency_layout.addWidget(frequency_label)
        self.frequency_dropdown = QComboBox()
        self.frequency_dropdown.addItems(["單次", "多次"])
        frequency_layout.addWidget(self.frequency_dropdown)

        # 創建每月、每季、每半年輸入框的水平布局
        monthly_layout = QHBoxLayout()
        monthly_label = QLabel("每月:")
        self.monthly_input = QLineEdit()
        self.monthly_input.setFixedWidth(50)
        monthly_layout.addWidget(monthly_label)
        monthly_layout.addWidget(self.monthly_input)

        quarterly_layout = QHBoxLayout()
        quarterly_label = QLabel("每季:")
        self.quarterly_input = QLineEdit()
        self.quarterly_input.setFixedWidth(50)
        quarterly_layout.addWidget(quarterly_label)
        quarterly_layout.addWidget(self.quarterly_input)

        halfyear_layout = QHBoxLayout()
        halfyear_label = QLabel("每半年:")
        self.halfyear_input = QLineEdit()
        self.halfyear_input.setFixedWidth(50)
        halfyear_layout.addWidget(halfyear_label)
        halfyear_layout.addWidget(self.halfyear_input)

        # 添加每月、每季、每半年輸入框到 frequency_layout
        frequency_layout.addLayout(monthly_layout)
        frequency_layout.addLayout(quarterly_layout)
        frequency_layout.addLayout(halfyear_layout)

        # 根據選擇的頻率動態更新輸入框的啟用狀態
        self.frequency_dropdown.currentTextChanged.connect(self.update_frequency_inputs)

        # 將 frequency_layout 包裝進 QWidget 並設置固定寬度
        frequency_widget = QWidget()
        frequency_widget.setLayout(frequency_layout)
        frequency_widget.setFixedWidth(500)  # 設置與頂部相同的固定寬度

        # 將 frequency_widget 和表單添加到主佈局中
        main_layout = QVBoxLayout()
        main_layout.addLayout(central_layout)
        main_layout.addWidget(form_group_box, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(frequency_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)

        # 初始化狀態
        self.update_frequency_inputs("單次")

    def clear_form(self):
        """清空所有輸入框的內容"""
        self.name_input.findChild(QLineEdit).clear()
        self.invoice_input.findChild(QLineEdit).clear()
        self.tax_id_input.findChild(QLineEdit).clear()
        self.phone_input.findChild(QLineEdit).clear()
        self.contact_person_input.findChild(QLineEdit).clear()
        self.window_input.findChild(QLineEdit).clear()
        self.window_phone_input.findChild(QLineEdit).clear()
        self.date_input.findChild(QLineEdit).clear()
        self.address_input.findChild(QLineEdit).clear()
        self.monthly_input.clear()
        self.quarterly_input.clear()
        self.halfyear_input.clear()

    def update_frequency_inputs(self, selection):
        """根據選擇的頻率更新輸入框的啟用狀態"""
        if selection == "單次":
            self.monthly_input.setEnabled(False)
            self.quarterly_input.setEnabled(False)
            self.halfyear_input.setEnabled(False)
        else:
            self.monthly_input.setEnabled(True)
            self.quarterly_input.setEnabled(True)
            self.halfyear_input.setEnabled(True)

    def fill_form_with_customer_info(self, customer_name):
        """根據選擇的客戶名稱自動填充表單"""
        customer_info = self.customer_data.get_customer_info(customer_name)
        self.name_input.findChild(QLineEdit).setText(customer_info.get("name", ""))
        self.invoice_input.findChild(QLineEdit).setText(customer_info.get("invoice_title", ""))
        self.tax_id_input.findChild(QLineEdit).setText(customer_info.get("tax_id", ""))
        self.phone_input.findChild(QLineEdit).setText(customer_info.get("phone", ""))
        self.contact_person_input.findChild(QLineEdit).setText(customer_info.get("contact_person", ""))
        self.window_input.findChild(QLineEdit).setText(customer_info.get("window", ""))
        self.window_phone_input.findChild(QLineEdit).setText(customer_info.get("window_phone", ""))
        self.date_input.findChild(QLineEdit).setText(customer_info.get("date", ""))
        self.address_input.findChild(QLineEdit).setText(customer_info.get("address", ""))

    def add_customer(self):
        """新增客戶"""
        customer_name = self.add_input.text()
        if customer_name == "-":
            self.show_message_box("客戶名稱無效，無法新增")
            return
        if customer_name:
            customer_info = self.get_form_data()
            self.customer_data.add_customer(customer_name, customer_info)
            self.dropdown.addItem(customer_name)
            self.show_message_box("新增成功")
            self.add_input.clear()

    def update_customer(self):
        """更新客戶"""
        customer_name = self.dropdown.currentText()
        if customer_name == "-":
            self.show_message_box("客戶名稱無效，無法更新")
            return
        customer_info = self.get_form_data()
        self.customer_data.update_customer(customer_name, customer_info)
        self.show_message_box("更新成功")

    def delete_customer(self):
        """刪除客戶"""
        customer_name = self.dropdown.currentText()
        if customer_name == "-":
            self.show_message_box("客戶名稱無效，無法刪除")
            return
        self.customer_data.delete_customer(customer_name)
        self.dropdown.removeItem(self.dropdown.currentIndex())
        self.show_message_box("刪除成功")
        self.reload_dropdown()

    def get_form_data(self):
        """取得表單中的客戶資料"""
        monthly = ""
        quarterly = ""
        halfyear = ""
        if self.frequency_dropdown.currentText() == "多次":
            monthly = self.monthly_input.text() or ""
            quarterly = self.quarterly_input.text() or ""
            halfyear = self.halfyear_input.text() or "" 


        return {
            "name": self.name_input.findChild(QLineEdit).text(),
            "invoice_title": self.invoice_input.findChild(QLineEdit).text(),
            "tax_id": self.tax_id_input.findChild(QLineEdit).text(),
            "phone": self.phone_input.findChild(QLineEdit).text(),
            "contact_person": self.contact_person_input.findChild(QLineEdit).text(),
            "window": self.window_input.findChild(QLineEdit).text(),
            "window_phone": self.window_phone_input.findChild(QLineEdit).text(),
            "date": self.date_input.findChild(QLineEdit).text(),
            "address": self.address_input.findChild(QLineEdit).text(),
            "frequency": self.frequency_dropdown.currentText(),
            "monthly": monthly,
            "quarterly": quarterly,
            "halfyear": halfyear
        }

    def show_message_box(self, message):
        """顯示提示訊息"""
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec()

    def reload_dropdown(self):
        """重新載入下拉選單的客戶列表"""
        self.dropdown.clear()
        self.dropdown.addItems(self.customer_data.get_all_customers())
