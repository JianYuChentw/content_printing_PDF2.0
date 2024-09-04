from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox
)
import sys

class InputWidget(QWidget):
    def __init__(self, label_title, label_text, width=200, height=50, input_height=30, orientation="horizontal", parent=None):
        super().__init__(parent)

        # 根據 orientation 決定使用哪種布局
        if orientation == "vertical":
            layout = QVBoxLayout()  # 垂直排列
        else:
            layout = QHBoxLayout()  # 水平排列（預設）

        # 創建標籤
        label = QLabel(f'{label_text}:')
        layout.addWidget(label)

        # 創建輸入框
        input_field = QLineEdit()
        input_field.setMinimumHeight(input_height)  # 設置輸入框的最小高度
        layout.addWidget(input_field)

        # 使用 QGroupBox 將它們包裹在一起
        group_box = QGroupBox(label_title)
        group_box.setLayout(layout)

        # 設置 QGroupBox 的寬度，但不固定高度
        group_box.setFixedWidth(width)

        # 設定主窗口的布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)


# # 測試這個元件
# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     # 水平排列
#     window_horizontal = InputWidget("表單標題", "輸入標籤", width=300, input_height=50, orientation="horizontal")
#     window_horizontal.show()

#     # 垂直排列
#     window_vertical = InputWidget("表單標題", "輸入標籤", width=300, input_height=50, orientation="vertical")
#     window_vertical.show()

#     sys.exit(app.exec())
