from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QMessageBox, QGroupBox, QGridLayout, QLabel
)
from PyQt6.QtCore import Qt
from .drug_data import DrugData  # 引入修改過的 DrugData 類

class DrugForm(QWidget):
    def __init__(self):
        super().__init__()

        # 使用 JSON 來保存和讀取藥物資料
        self.drug_data = DrugData()

        # 創建頂部區域的下拉選單、輸入框和按鈕
        top_layout = QHBoxLayout()

        # 下拉選單
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.drug_data.get_all_drugs())  # 從藥物資料中載入藥物
        self.dropdown.setFixedWidth(150)  # 設置下拉選單固定寬度
        self.dropdown.currentTextChanged.connect(self.fill_form_with_drug_info)  # 監聽選擇變更
        top_layout.addWidget(self.dropdown)

        # 新增用的輸入框
        self.add_input = QLineEdit()
        self.add_input.setPlaceholderText("輸入新增藥物名稱...")
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
        add_button.clicked.connect(self.add_drug)
        update_button.clicked.connect(self.update_drug)
        delete_button.clicked.connect(self.delete_drug)
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

        # 使用 QGridLayout 來創建四行五列的表單
        grid_layout = QGridLayout()

        # 表單標題
        headers = ["施用藥劑及主要成份", "稀釋比例", "劑型", "許可證字號", "使用區域"]


        for i, header in enumerate(headers):
            label = QLabel(header)
            label.setStyleSheet("font-size: 16px;")  # 調整標題字體大小
            grid_layout.addWidget(label, 0, i)

        # 創建 4 行 5 列的輸入框
        self.inputs = []
        for row in range(1, 5):
            input_row = []
            for col in range(5):
                line_edit = QLineEdit()
                grid_layout.addWidget(line_edit, row, col)
                input_row.append(line_edit)
            self.inputs.append(input_row)

        # 創建一個 QGroupBox 來包裹 grid_layout
        form_group_box = QGroupBox("藥物資料表單")
        form_group_box.setLayout(grid_layout)

        # 將主佈局設置好
        main_layout = QVBoxLayout()
        main_layout.addLayout(central_layout)
        main_layout.addWidget(form_group_box, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)

    def fill_form_with_drug_info(self, drug_name):
        """根據選擇的藥物名稱自動填充四行五列的表單"""
        drug_info = self.drug_data.get_drug_info(drug_name)
        # 填充每個欄位對應的數據
        if drug_info:
            for row in range(4):
                for col in range(5):
                    self.inputs[row][col].setText(drug_info[row][col])

    def add_drug(self):
        """新增藥物"""
        drug_name = self.add_input.text()
        if drug_name == "-":
            self.show_message_box("藥物名稱無效，無法新增")
            return
        if drug_name:
            drug_info = self.get_form_data()
            self.drug_data.add_drug(drug_name, drug_info)
            self.dropdown.addItem(drug_name)
            self.show_message_box("新增成功")
            self.add_input.clear()

    def update_drug(self):
        """更新藥物"""
        drug_name = self.dropdown.currentText()
        if drug_name == "-":
            self.show_message_box("藥物名稱無效，無法更新")
            return
        drug_info = self.get_form_data()
        self.drug_data.update_drug(drug_name, drug_info)
        self.show_message_box("更新成功")

    def delete_drug(self):
        """刪除藥物"""
        drug_name = self.dropdown.currentText()
        if drug_name == "-":
            self.show_message_box("藥物名稱無效，無法刪除")
            return
        self.drug_data.delete_drug(drug_name)
        self.dropdown.removeItem(self.dropdown.currentIndex())
        self.show_message_box("刪除成功")

    def clear_form(self):
        """清空表單內容"""
        for row in self.inputs:
            for line_edit in row:
                line_edit.clear()

    def get_form_data(self):
        """取得表單中的四行五列的藥物資料"""
        return [[self.inputs[row][col].text() for col in range(5)] for row in range(4)]

    def show_message_box(self, message):
        """顯示提示訊息"""
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec()
