from PyQt6.QtWidgets import QGroupBox, QGridLayout, QCheckBox

class CheckboxesArea(QGroupBox):
    def __init__(self):
        super().__init__("防治項目")

        # 創建複選框的佈局
        checkboxes_layout = QGridLayout()

        # 定義複選框的內容
        checkboxes = [
            ("一般害蟲防治 – Pest Control", 0, 0),
            ("白蟻防治 – Termite Control", 0, 1),
            ("鼠害防治 – Rodent Control", 0, 2),
            ("跳蚤防治 – Fleas Control", 1, 0),
            ("粉狀蛀蟲防治 – Powder Post Beetle", 1, 1),
            ("其他 – Others", 1, 2)
        ]

        # 動態添加複選框到佈局
        for text, row, col in checkboxes:
            checkbox = QCheckBox(text)
            checkboxes_layout.addWidget(checkbox, row, col)

        # 設置佈局
        self.setLayout(checkboxes_layout)
