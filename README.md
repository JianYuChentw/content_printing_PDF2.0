# **Content Printing PDF App2.0**

> 一款將內容轉印至預設三聯單規格文件的生產應用程式

![演示第一頁](/save/AppDemo.gif)

## **功能說明**

### **客戶記錄功能**
- 可將客戶的基本資訊與相關數據記錄，方便後續查詢和管理。

### **藥品搭配紀錄功能**
- 記錄不同場域使用的藥物搭配資訊，為醫療與製藥領域提供數據支持。

### **轉印輸出 PDF 檔案**
- 將已記錄的內容轉印並輸出為 PDF 格式，支援自定義三聯單規格。

## **專案技術**

### **前端**
- **PyQt**: 使用 PyQt 構建桌面應用程式的圖形用戶界面。

### **後端**
- **Python**: 作為伺服器端邏輯的主要開發語言。
- **ReportLab**: 用於生成 PDF 文件，支持高度自定義。

### **工具與建構**
- **PyInstaller**: 用於將 Python 應用程式打包成可執行文件。
- **pip**: 管理 Python 專案的相依性。

## **安裝與運行**

### **前置需求**
- 需先安裝 [Python 3.x](https://www.python.org/) 與 [pip](https://pip.pypa.io/en/stable/)

### **安裝**
1. 進入專案目錄
    ```bash
    cd content_printing_pdf_app
    ```
2. 安裝所需的套件
    ```bash
    pip install -r requirements.txt
    ```

### **運行**
- 開發模式啟動
    ```bash
    python main.py
    ```
- 編譯與打包應用程式
- 請根據執行環境決定打包當下的作業系統
    ```bash
    pyinstaller --onefile main.py
    ```

