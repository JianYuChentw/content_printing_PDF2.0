from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy

class TodoArea(QWidget):
    def __init__(self):
        super().__init__()

        # 創建外層水平佈局來實現水平居中
        outer_layout = QHBoxLayout()

        # 添加左側彈性空間
        outer_layout.addStretch(1)

        # 創建主佈局
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(5)  # 減少垂直佈局的間距

        # 創建每個標籤和輸入框對應的佈局
        self.task_input = QLineEdit()  # 保存交辦事項的輸入框
        self.main_layout.addLayout(self.create_layout("交辦事項", 30, self.task_input, 250))

        self.report_input = QTextEdit()  # 保存工作報告的文本框
        self.main_layout.addLayout(self.create_layout("工作報告", 150, self.report_input, 400))

        self.technician_input = QLineEdit()  # 保存技術員的輸入框
        self.main_layout.addLayout(self.create_layout("技術員", 30, self.technician_input, 150))

        self.operator_input = QLineEdit()  # 保存施藥人員的輸入框
        self.main_layout.addLayout(self.create_layout("施藥人員", 30, self.operator_input, 150))

        # 將主佈局添加到外層水平佈局中
        outer_layout.addLayout(self.main_layout)

        # 添加右側彈性空間
        outer_layout.addStretch(1)

        # 設置主佈局
        self.setLayout(outer_layout)

    def create_layout(self, label_text, input_height, input_widget, input_width):
        layout = QHBoxLayout()  # 水平佈局

        # 創建標籤
        label = QLabel(f'{label_text}:')
        label.setStyleSheet("font-size: 16px; padding-right: 5px;")  # 減少標籤與輸入框的間距
        label.setFixedWidth(80)  # 控制標籤寬度
        layout.addWidget(label)

        # 設置輸入框的最小高度和最大寬度
        input_widget.setMinimumHeight(input_height)
        input_widget.setFixedWidth(input_width)
        input_widget.setStyleSheet("font-size: 16px; margin: 0px;")
        layout.addWidget(input_widget)

        # 添加一個彈性空間來推動輸入框和標籤靠近
        spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)

        # 設置內邊距和間距
        layout.setContentsMargins(0, 0, 0, 0)  # 去除內邊距
        layout.setSpacing(0)  # 減少標籤與輸入框的間距

        return layout

    def get_todo_data(self):
        """獲取所有輸入的數據"""
        return {
            "交辦事項": self.task_input.text(),
            "工作報告": self.report_input.toPlainText(),
            "技術員": self.technician_input.text(),
            "施藥人員": self.operator_input.text()
        }
