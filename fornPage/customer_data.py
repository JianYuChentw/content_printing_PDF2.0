import json
import os
import sys

class CustomerData:
    def __init__(self, json_file='save/customers.json'):
        # 使用 get_resource_path 確保打包後的正確路徑
        self.json_file = self.get_resource_path(json_file)
        print(f"客戶資料路徑: {self.json_file}")  # 確認 JSON 文件的最終路徑
        self.data = self.load_data()

    def get_resource_path(self, relative_path):
        """返回正確的資源路徑，處理 PyInstaller 打包和未打包的情況"""
        if getattr(sys, 'frozen', False):
            # 如果是打包後運行，使用 sys.executable 定位到 dist 資料夾
            base_dir = os.path.dirname(sys.executable)
        else:
            # 未打包時，使用當前腳本的絕對路徑
            # 這裡的關鍵是確保我們找到的是應用根目錄
            base_dir = os.path.abspath(os.path.dirname(__file__))
            # 如果你知道確定要回到某個上層資料夾（如根目錄），可以上移多層
            base_dir = os.path.dirname(base_dir)  # 回到上一層資料夾
            # 如果還需要再上移一層，可以再加一行 base_dir = os.path.dirname(base_dir)

        return os.path.join(base_dir, relative_path)

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
        if customer_name == "-":
            print("客戶名稱無效，無法新增客戶。")  # 顯示提示訊息
            return
        self.data[customer_name] = customer_info
        self.save_data()

    def update_customer(self, customer_name, customer_info):
        """更新客戶資料"""
        if customer_name == "-":
            print("客戶名稱無效，無法更新客戶。")  # 顯示提示訊息
            return
        if customer_name in self.data:
            self.data[customer_name] = customer_info
            self.save_data()

    def delete_customer(self, customer_name):
        """刪除客戶資料"""
        if customer_name == "-":
            print("客戶名稱無效，無法刪除客戶。")  # 顯示提示訊息
            return
        if customer_name in self.data:
            del self.data[customer_name]
            self.save_data()

    def get_customer_info(self, customer_name):
        """根據客戶名稱取得客戶資料"""
        return self.data.get(customer_name, {})

    def get_all_customers(self):
        """取得所有客戶名稱"""
        return list(self.data.keys())
