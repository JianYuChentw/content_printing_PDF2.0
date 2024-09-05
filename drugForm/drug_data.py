import json
import os

class DrugData:
    def __init__(self, json_file='save/drugs.json'):
        # 獲取當前腳本的目錄，並拼接出 JSON 文件的絕對路徑
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.json_file = os.path.join(base_dir, json_file)
        print(f"藥物資料路徑: {self.json_file}")  # 新增路徑檢查
        self.data = self.load_data()

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
