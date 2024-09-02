from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def generate_pdf_with_chinese(customer_info, output_filename):
    # 創建PDF畫布
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4

    # 註冊中文字體
    pdfmetrics.registerFont(TTFont('twKai', 'tw_Kai.ttf'))  # 替換為你自己的字體文件

    # 設定字體和大小
    c.setFont("twKai", 12)

    # 輸出客戶資訊（中文）
    c.drawString(80, height - 30, f"{customer_info['name']}")
    c.drawString(80, height - 50, f"{customer_info['phone']}")
    c.drawString(315, height - 70, f"{customer_info['address']}")


    # 勾一
    c.drawString(40, height - 405, "V")
    c.drawString(40, height - 580, f"{customer_info['other']}")
    # 保存PDF
    c.save()

# 範例數據
customer_info = {
    "name": "張三",
    "phone": "0912345678",
    "address": "2024/02/02 14:00 - 2024/00/00 15:00",
    "other": "ljtkvjritojvijrktv;ldkgpkwl;emdlj010elermflmerlkmvlkemnr"
}

# 生成PDF
generate_pdf_with_chinese(customer_info, "customer_info_chinese.pdf")
