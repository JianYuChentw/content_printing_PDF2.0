from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QGroupBox, QHBoxLayout
)
from PyQt6.QtCore import Qt
import sys
from .components import InputWidget  # 確認引入 InputWidget 正確

class FrontPage(QWidget):
    def __init__(self):
        super().__init__()

        # 使用 QGridLayout 來放置左右兩邊的表單元素
        grid_layout = QGridLayout()

        # 左邊表單部分
        grid_layout.addWidget(InputWidget("", "客戶名稱", 250, 50), 0, 0)
        grid_layout.addWidget(InputWidget("", "發票抬頭", 250, 50), 1, 0)
        grid_layout.addWidget(InputWidget("", "統一編號", 250, 50), 2, 0)
        grid_layout.addWidget(InputWidget("", "電話", 250, 50), 3, 0)
        grid_layout.addWidget(InputWidget("", "聯絡人", 250, 50), 4, 0)

        # 右邊表單部分
        grid_layout.addWidget(InputWidget("", "施作聯絡窗口", 250, 50), 0, 1)
        grid_layout.addWidget(InputWidget("", "施作窗口電話", 250, 50), 1, 1)
        grid_layout.addWidget(InputWidget("", "施工日期/時間", 250, 50), 2, 1)

        # 施作地址部分，垂直排列
        grid_layout.addWidget(InputWidget("", "施作地址", 300, 100, orientation="vertical"), 3, 1)

        # 創建一個 QGroupBox 來包裹 grid_layout
        form_group_box = QGroupBox("客戶資訊表單")
        form_group_box.setLayout(grid_layout)

        # 創建一個 QVBoxLayout 將 QGroupBox 置中
        centered_layout = QVBoxLayout()
        centered_layout.addStretch(1)  # 添加彈性空間
        centered_layout.addWidget(form_group_box, alignment=Qt.AlignmentFlag.AlignCenter)  # 置中顯示 QGroupBox
        centered_layout.addStretch(1)  # 添加彈性空間

        # 設定主窗口的布局
        self.setLayout(centered_layout)



