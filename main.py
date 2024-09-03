from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from textwrap import wrap

    # 工作報告 - 多行文本處理
def add_wrapped_text(text_object, text, max_chars):
        # 將文本按指定的字元數進行換行
        lines = []
        for original_line in text.split('\n'):
            wrapped_lines = wrap(original_line, max_chars)
            lines.extend(wrapped_lines)
        for line in lines:
            text_object.textLine(line)
  



def generate_pdf_with_chinese(customer_info, output_filename):
    # 創建PDF畫布
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4

    # 註冊中文字體
    pdfmetrics.registerFont(TTFont('twKai', 'fonts/twKai.ttf'))  # 替換為你自己的字體文件

    # 設定字體和大小
    c.setFont("twKai", 12)

    # 輸出客戶資訊（左側）
    c.drawString(80, height - 71, f"{customer_info['clientName']}")
    c.drawString(80, height - 85, f"{customer_info['billName']}")
    c.drawString(80, height - 98, f"{customer_info['invoiceNumber']}")
    c.drawString(80, height - 111, f"{customer_info['clientPhone']}")
    c.drawString(80, height - 124, f"{customer_info['clientContactPerson']}")

    # 輸出客戶資訊（右側）
    c.drawString(320, height - 80, f"{customer_info['constructionPersonInCharge']}")
    c.drawString(461, height - 80, f"{customer_info['constructionPersonInChargePhone']}")
    c.drawString(320, height - 100, f"{customer_info['constructionDate']}")
    c.drawString(320, height - 120, f"{customer_info['constructionAddress']}")

    # 施工頻率
    c.drawString(80, height - 137, f"{customer_info['singleConstruction']}")
    c.drawString(178.5, height - 137, f"{customer_info['repeatedlyConstruction']}")
    c.drawString(315, height - 137, "10")
    c.drawString(400, height - 137, "10")
    c.drawString(485, height - 137, "10")

    # 防治項目勾選
    c.drawString(80, height - 165, "V")
    c.drawString(80, height - 185, "V")

    c.drawString(235, height - 165, "V")
    c.drawString(235, height - 185, "V")

    c.drawString(420, height - 165, "V")
    c.drawString(420, height - 185, "V")
 

    # 勾選一般蟲害防治(左側)
    c.drawString(42, height - 400, "V")

    # 勾選一般蟲害防治(右側)
    c.drawString(170, height - 400, "V")

    # 勾選鼠害防治(左側)
    c.drawString(310, height - 400, "V")
    

    # 勾選鼠害防治(右側)
    c.drawString(435, height - 400, "V")


  
    text_object = c.beginText(40, height - 590)
    text_object.setFont("twKai", 12)
    add_wrapped_text(text_object, customer_info['workReport'], 31)
    c.drawText(text_object)

    # 保存PDF
    c.save()

# 範例數據

data='已完成施工，無異常，這句話看似簡單，卻承載著大量的工作與責任。首先，施工過程是一個繁瑣而複雜的任務，涉及到許多不同的階段和專業技能。從最初的設計圖紙到材料選擇，再到實際施工，每一個環節都需要嚴格的監督與管理。施工人員必須確保所有的工序都按照計劃進行，並且在過程中必須處理各種突發情況，例如天氣變化、材料延遲或意外的技術問題。其次，「無異常」這三個字代表了施工過程中沒有出現任何問題或偏差。這不僅僅是一個簡單的結果，更是施工質量和管理水平的體現。在現代建築施工中，無異常的完成意味著所有的設計規範都得到了嚴格遵守，所有的安全措施都得到了有效的實施。這要求施工團隊具有高度的專業知識和豐富的經驗，同時也要求他們在工作中保持高度的警惕和細心，從而及時發現和解決任何可能影響施工質量的問題。'

customer_info = {
    'clientName': '張三',
    'billName': '張三的帳單',
    'invoiceNumber': 'INV-123456',
    'clientPhone': '0912-345-678',
    'clientContactPerson': '李四',
    'constructionPersonInCharge': '王五哥',
    'constructionPersonInChargePhone': '0912-345-678',
    'constructionDate': '2024/01/01 00:00 - 2024/01/01 00:00',
    'constructionAddress': '台北市中正區',
    'singleConstruction': 'V',
    'repeatedlyConstruction': 'V',
    'todoList': '施工項目一、施工項目二',
    'workReport': data
}

# 生成PDF
generate_pdf_with_chinese(customer_info, 'example.pdf')
