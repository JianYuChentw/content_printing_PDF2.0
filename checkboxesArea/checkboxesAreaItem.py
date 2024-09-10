from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLineEdit, QLabel, QGroupBox

class CheckboxesAreaItem(QWidget):
    def __init__(self):
        super().__init__()

        # 創建主水平佈局，左右放置兩組選項
        self.main_layout = QHBoxLayout()

        # ---- 第一組項目：一般蟲害防治 ---- #
        self.group1_layout = QVBoxLayout()
        self.group1_box = QGroupBox("一般蟲害防治")
        self.group1_box.setLayout(self.group1_layout)
        self.group1_box.setStyleSheet("font-size: 16px;")  # 設置字體大小

        # 將第一組項目添加到佈局中
        self.create_checkbox(self.group1_layout, "手提式噴灑器")
        self.create_checkbox(self.group1_layout, "電動式噴灑器")
        self.create_checkbox(self.group1_layout, "中型電動式噴灑器")
        self.create_checkbox(self.group1_layout, "大型氣動式噴灑器")
        self.create_checkbox(self.group1_layout, "動力式噴灑機")
        self.create_checkbox(self.group1_layout, "微粒子空間冷霧機")
        self.create_checkbox(self.group1_layout, "熱霧機")
        self.create_checkbox(self.group1_layout, "蟑螂餌膠")
        self.create_checkbox(self.group1_layout, "縫隙處理機")

        # "更換捕蟲紙"選項和輸入框
        self.trap_paper_checkbox = QCheckBox("更換捕蟲紙")
        self.trap_paper_checkbox.setStyleSheet("font-size: 16px;")  # 設置字體大小
        self.trap_paper_input = QLineEdit()
        self.trap_paper_input.setPlaceholderText("張")
        self.trap_paper_input.setStyleSheet("font-size: 16px;")  # 設置字體大小
        self.trap_paper_input.setEnabled(False)  # 預設不可用
        self.trap_paper_checkbox.stateChanged.connect(self.toggle_trap_paper_input)

        # 設置 "更換捕蟲紙" 的水平佈局
        self.trap_paper_layout = QHBoxLayout()
        self.trap_paper_layout.addWidget(self.trap_paper_checkbox)
        self.trap_paper_layout.addWidget(self.trap_paper_input)
        self.group1_layout.addLayout(self.trap_paper_layout)

        # ---- 第二組項目：鼠疫防治工程 ---- #
        self.group2_layout = QVBoxLayout()
        self.group2_box = QGroupBox("鼠疫防治工程")
        self.group2_box.setLayout(self.group2_layout)
        self.group2_box.setStyleSheet("font-size: 16px;")  # 設置字體大小

        # 將第二組項目添加到佈局中
        self.create_checkbox(self.group2_layout, "檢視老鼠入侵點")
        self.create_checkbox(self.group2_layout, "檢視鼠跡狀況")
        self.create_checkbox(self.group2_layout, "補充或更換餌劑")
        self.create_checkbox(self.group2_layout, "補充、更換或新增鼠板")
        self.create_checkbox(self.group2_layout, "鼠洞封阻工程")
        self.create_checkbox(self.group2_layout, "設計老鼠活動路徑")
        self.create_checkbox(self.group2_layout, "施用忌避劑")

        # "捕獲老鼠" 選項和輸入框
        self.catch_mouse_checkbox = QCheckBox("捕獲老鼠")
        self.catch_mouse_checkbox.setStyleSheet("font-size: 16px;")  # 設置字體大小
        self.catch_mouse_input = QLineEdit()
        self.catch_mouse_input.setPlaceholderText("隻")
        self.catch_mouse_input.setStyleSheet("font-size: 16px;")  # 設置字體大小
        self.catch_mouse_input.setEnabled(False)  # 預設不可用
        self.catch_mouse_checkbox.stateChanged.connect(self.toggle_catch_mouse_input)

        # 設置 "捕獲老鼠" 的水平佈局
        self.catch_mouse_layout = QHBoxLayout()
        self.catch_mouse_layout.addWidget(self.catch_mouse_checkbox)
        self.catch_mouse_layout.addWidget(self.catch_mouse_input)
        self.group2_layout.addLayout(self.catch_mouse_layout)

        # 其他鼠疫防治項目
        self.create_checkbox(self.group2_layout, "除臭、除菌處理")
        self.create_checkbox(self.group2_layout, "架設震動或超音波器")

        # 將兩個組件佈局加入到主水平佈局中
        self.main_layout.addWidget(self.group1_box)
        self.main_layout.addWidget(self.group2_box)

        self.setLayout(self.main_layout)

    def create_checkbox(self, layout, label_text):
        """建立勾選框並添加到指定的佈局"""
        checkbox = QCheckBox(label_text)
        checkbox.setStyleSheet("font-size: 16px;")  # 設置字體大小
        layout.addWidget(checkbox)

    def toggle_trap_paper_input(self, state):
        """當勾選 '更換捕蟲紙' 後啟用輸入框"""
        if state == 2:  # 勾選時啟用
            self.trap_paper_input.setEnabled(True)
        else:
            self.trap_paper_input.setEnabled(False)

    def toggle_catch_mouse_input(self, state):
        """當勾選 '捕獲老鼠' 後啟用輸入框"""
        if state == 2:  # 勾選時啟用
            self.catch_mouse_input.setEnabled(True)
        else:
            self.catch_mouse_input.setEnabled(False)
    
    def clear_checkboxes(self):
        """清空所有勾選框和輸入框的內容"""
        # 清空第一組的勾選框
        for checkbox in self.group1_box.findChildren(QCheckBox):
            checkbox.setChecked(False)

        # 清空 "更換捕蟲紙" 的輸入框
        self.trap_paper_input.clear()
        self.trap_paper_input.setEnabled(False)  # 清空後禁用輸入框

        # 清空第二組的勾選框
        for checkbox in self.group2_box.findChildren(QCheckBox):
            checkbox.setChecked(False)

        # 清空 "捕獲老鼠" 的輸入框
        self.catch_mouse_input.clear()
        self.catch_mouse_input.setEnabled(False)  # 清空後禁用輸入框

