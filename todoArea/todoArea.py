from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFontMetrics

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
        self.report_input.setStyleSheet("""
            QTextEdit {
                font-family: Courier;
                font-size: 14px;
                background-color: #f0f0f0;
                border: 1px solid black;
            }
        """)
        self.main_layout.addLayout(self.create_layout("工作報告", 150, self.report_input, 400))

        # 創建顯示行數的標籤
        self.line_count_label = QLabel("行數: 0")
        self.main_layout.addWidget(self.line_count_label)

        # 將文本框文本變化信號連接到更新方法
        self.report_input.textChanged.connect(self.update_line_count)

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
        input_widget.setStyleSheet("font-size: 12px; margin: 0px;")
        layout.addWidget(input_widget)

        # 添加一個彈性空間來推動輸入框和標籤靠近
        spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)

        # 設置內邊距和間距
        layout.setContentsMargins(0, 0, 0, 0)  # 去除內邊距
        layout.setSpacing(0)  # 減少標籤與輸入框的間距

        return layout


    def update_line_count(self):
        """根據字元寬度和自動換行來更新行數顯示，並限制行數不超過 10 行"""
        # 獲取文本框的內容
        text = self.report_input.toPlainText()

        # 創建 QFontMetrics 對象來計算字元寬度
        font = self.report_input.font()
        metrics = QFontMetrics(font)

        # 獲取文本框的寬度（考慮自動換行的寬度）
        total_width = self.report_input.viewport().width()

        total_lines = 0
        current_line = ""
        current_width = 0

        # 遍歷每個字元來計算自動換行的行數
        for char in text:
            # 如果遇到手動換行符
            if char == '\n':
                total_lines += 1  # 增加行數
                current_line = ""
                current_width = 0
                continue

            # 計算當前字元的寬度
            char_width = metrics.horizontalAdvance(char)

            # 如果當前行加上這個字會超過文本框寬度，則換行
            if current_width + char_width > total_width:
                total_lines += 1  # 增加行數
                current_line = char
                current_width = char_width
            else:
                current_line += char
                current_width += char_width

        # 處理最後一行
        if current_line:
            total_lines += 1

        # 更新顯示的行數
        self.line_count_label.setText(f"行數: {total_lines}")

        # 如果行數大於等於 10，禁止進一步輸入
        if total_lines >= 10:
            self.report_input.blockSignals(True)  # 暫時禁止信號，以免影響後續操作
            cursor = self.report_input.textCursor()
            cursor.deletePreviousChar()  # 刪除最後輸入的字元
            self.report_input.setTextCursor(cursor)  # 重置游標位置
            self.report_input.blockSignals(False)  # 恢復信號

    def get_todo_data(self):
        """獲取所有輸入的數據"""
        return {
            "交辦事項": self.task_input.text(),
            "工作報告": self.report_input.toPlainText(),
            "技術員": self.technician_input.text(),
            "施藥人員": self.operator_input.text()
        }

    def clear_inputs(self):
        """清空所有輸入框和文本框的內容"""
        self.task_input.clear()  # 清空交辦事項的輸入框
        self.report_input.clear()  # 清空工作報告的文本框
        self.technician_input.clear()  # 清空技術員的輸入框
        self.operator_input.clear()  # 清空施藥人員的輸入框
