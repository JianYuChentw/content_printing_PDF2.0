from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox
)
import sys

class InputWidget(QWidget):
    def __init__(self, label_title, label_text, width=200, input_height=30, orientation="horizontal", parent=None):
        super().__init__(parent)

        # 根據 orientation 決定使用哪種布局
        if orientation == "vertical":
            layout = QVBoxLayout()  # 垂直排列
        else:
            layout = QHBoxLayout()  # 水平排列（預設）

        # 創建標籤
        label = QLabel(f'{label_text}:')
        label.setStyleSheet("font-size:16px")
        label.setFixedHeight(20)  # 可以固定標籤高度，進一步減少間距
        layout.addWidget(label)

        # 創建輸入框
        input_field = QLineEdit()
        input_field.setMinimumHeight(input_height)  # 設置輸入框的最小高度
        layout.addWidget(input_field)

        # 移除內部邊距和縮小元件間距
        layout.setContentsMargins(0, 0, 0, 0)  # 去除內邊距
        layout.setSpacing(2)  # 減少標籤和輸入框之間的間距

        # 設定主窗口的布局
        self.setLayout(layout)

        # 設定輸入框組件的寬度
        self.setFixedWidth(width)


