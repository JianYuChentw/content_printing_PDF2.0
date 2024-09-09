import json
import os
import sys

class DrugData:
    def __init__(self, json_file='save/drugs.json'):
        # 使用 get_resource_path 確保打包後的正確路徑
        self.json_file = self.get_resource_path(json_file)
        print(f"藥物資料路徑: {self.json_file}")  # 新增路徑檢查
        self.data = self.load_data()

    def get_resource_path(self, relative_path):
        """返回正確的資源路徑，處理 PyInstaller 打包和未打包的情況"""
        if getattr(sys, 'frozen', False):
            # 如果是打包後運行，使用 sys.executable 定位到 dist 資料夾
            base_dir = os.path.dirname(sys.executable)
        else:
            # 未打包時，使用當前腳本的絕對路徑
            base_dir = os.path.abspath(os.path.dirname(__file__))
            # 如果當前在較深的目錄下，我們回到上一層資料夾
            base_dir = os.path.dirname(base_dir)  # 回到上一層目錄

        # 返回目標文件的完整路徑
        return os.path.join(base_dir, relative_path)

    def load_data(self):
        """從 JSON 文件讀取藥物資料，如果文件不存在則返回空字典"""
        if os.path.exists(self.json_file):
            print(f"載入檔案: {self.json_file}")  # 確認是否找到檔案
            with open(self.json_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        print(f"找不到檔案: {self.json_file}")  # 檔案找不到時顯示
        return {}

    def save_data(self):
        """將藥物資料保存回 JSON 文件"""
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_drug(self, drug_name, drug_info):
        """新增藥物資料"""
        if drug_name == "-":
            print("無法新增藥物資料，藥物名稱無效。")  # 可以替換成訊息框或日誌
            return
        self.data[drug_name] = drug_info
        self.save_data()

    def update_drug(self, drug_name, drug_info):
        """更新藥物資料"""
        if drug_name == "-":
            print("無法更新藥物資料，藥物名稱無效。")  # 可以替換成訊息框或日誌
            return
        if drug_name in self.data:
            self.data[drug_name] = drug_info
            self.save_data()

    def delete_drug(self, drug_name):
        """刪除藥物資料"""
        if drug_name == "-":
            print("無法刪除藥物資料，藥物名稱無效。")  # 可以替換成訊息框或日誌
            return
        if drug_name in self.data:
            del self.data[drug_name]
            self.save_data()

    def get_drug_info(self, drug_name):
        """根據藥物名稱取得藥物資料"""
        return self.data.get(drug_name, {})

    def get_all_drugs(self):
        """取得所有藥物名稱"""
        return list(self.data.keys())
