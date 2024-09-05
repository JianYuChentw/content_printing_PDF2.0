import json
import os

class CustomerData:
    def __init__(self, json_file='save/customers.json'):
        # 獲取當前腳本的目錄，並拼接出 JSON 文件的絕對路徑
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.json_file = os.path.join(base_dir, json_file)
        print(f"客戶資料路徑: {self.json_file}")  # 新增路徑檢查
        self.data = self.load_data()

    def load_data(self):
        """從 JSON 文件讀取客戶資料，如果文件不存在則返回空字典"""
        if os.path.exists(self.json_file):
            print(f"載入檔案: {self.json_file}")  # 確認是否找到檔案
            with open(self.json_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        print(f"找不到檔案: {self.json_file}")  # 檔案找不到時顯示
        return {}

    def save_data(self):
        """將客戶資料保存回 JSON 文件"""
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_customer(self, customer_name, customer_info):
        """新增客戶資料"""
        self.data[customer_name] = customer_info
        self.save_data()

    def update_customer(self, customer_name, customer_info):
        """更新客戶資料"""
        if customer_name in self.data:
            self.data[customer_name] = customer_info
            self.save_data()

    def delete_customer(self, customer_name):
        """刪除客戶資料"""
        if customer_name in self.data:
            del self.data[customer_name]
            self.save_data()

    def get_customer_info(self, customer_name):
        """根據客戶名稱取得客戶資料"""
        return self.data.get(customer_name, {})

    def get_all_customers(self):
        """取得所有客戶名稱"""
        return list(self.data.keys())
