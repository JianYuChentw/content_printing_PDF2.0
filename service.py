import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from textwrap import wrap

# 爭偽回傳勾號
def true_false_return(value):
    return "V" if value else ""

# 工作報告 - 多行文本處理
def add_wrapped_text(text_object, text, max_chars):
    # 將文本按指定的字元數進行換行
    lines = []
    for original_line in text.split('\n'):
        wrapped_lines = wrap(original_line, max_chars)
        lines.extend(wrapped_lines)
    for line in lines:
        text_object.textLine(line)

def generate_pdf_with_chinese(customer_info):
    # 定義輸出資料夾路徑
    output_dir = os.path.expanduser("~/Desktop/PDFout")
    
    # 檢查資料夾是否存在，若不存在則創建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 創建PDF畫布，替換斜杠為連字符
    safe_date = customer_info['constructionDate'].replace('/', '-')
    filename = f"{safe_date[:11]}-{customer_info['billName']}.pdf"
    output_filename = os.path.join(output_dir, filename)  # 組合完整的檔案路徑
    print(output_filename)
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4

    # 註冊中文字體
    pdfmetrics.registerFont(TTFont('twKai', 'fonts/twKai.ttf'))  # 替換為你自己的字體文件

    # 設定字體和大小
    c.setFont("twKai", 12)

    # 輸出客戶資訊（左側）
    c.drawString(80, height - 71, f"{customer_info['clientName']}")
    c.drawString(80, height - 90, f"{customer_info['billName']}")
    c.drawString(80, height - 110, f"{customer_info['invoiceNumber']}")
    c.drawString(80, height - 131, f"{customer_info['clientPhone']}")
    c.drawString(80, height - 148, f"{customer_info['clientContactPerson']}")

    # 輸出客戶資訊（右側）
    c.drawString(326, height - 80, f"{customer_info['constructionPersonInCharge']}")
    c.drawString(470, height - 80, f"{customer_info['constructionPersonInChargePhone']}")
    c.drawString(328, height - 108, f"{customer_info['constructionDate']}")
    c.drawString(325, height - 145, f"{customer_info['constructionAddress']}")

    # 施工頻率
    if customer_info['construction'] == "多次":
        c.drawString(180, height - 167, "V")
        c.drawString(315, height - 167, customer_info['monthly'])
        c.drawString(400, height - 167, customer_info['quarterly'])
        c.drawString(490, height - 167, customer_info['yearly'])
    else:
        c.drawString(81, height - 167, "V")

    # 防治項目勾選
    c.drawString(80, height - 195, true_false_return(customer_info['pestControl']))
    c.drawString(80, height - 220, true_false_return(customer_info['fleasControl']))

    c.drawString(239, height - 195, true_false_return(customer_info['temiteControl']))
    c.drawString(239, height - 220, true_false_return(customer_info['powerControl']))

    c.drawString(422, height - 195, true_false_return(customer_info['rodentControl']))
    c.drawString(422, height - 220, true_false_return(customer_info['otrher']))

    # 藥品使用
    c.drawString(25, height - 278, customer_info['drug1_1'])
    c.drawString(210, height - 278, customer_info['drug1_2'])
    c.drawString(266, height - 278, customer_info['drug1_3'])
    c.drawString(325, height - 278, customer_info['drug1_4'])
    c.drawString(430, height - 278, customer_info['drug1_5'])

    c.drawString(25, height - 301, customer_info['drug2_1'])
    c.drawString(210, height - 301, customer_info['drug2_2'])
    c.drawString(266, height - 301, customer_info['drug2_3'])
    c.drawString(325, height - 301, customer_info['drug2_4'])
    c.drawString(430, height - 301, customer_info['drug2_5'])

    c.drawString(25, height - 324, customer_info['drug3_1'])
    c.drawString(210, height - 324, customer_info['drug3_2'])
    c.drawString(266, height - 324, customer_info['drug3_3'])
    c.drawString(325, height - 324, customer_info['drug3_4'])
    c.drawString(430, height - 324, customer_info['drug3_5'])

    c.drawString(25, height - 348, customer_info['drug4_1'])
    c.drawString(210, height - 348, customer_info['drug4_2'])
    c.drawString(266, height - 348, customer_info['drug4_3'])
    c.drawString(325, height - 348, customer_info['drug4_4'])
    c.drawString(430, height - 348, customer_info['drug4_5'])

    # 勾選一般蟲害防治(左側)
    c.drawString(43, height - 385, true_false_return(customer_info['pestControlL1_1']))
    c.drawString(43, height - 410, true_false_return(customer_info['pestControlL1_2']))
    c.drawString(43, height - 437, true_false_return(customer_info['pestControlL1_3']))
    c.drawString(43, height - 462, true_false_return(customer_info['pestControlL1_4']))
    c.drawString(43, height - 490, true_false_return(customer_info['pestControlL1_5']))

    # 勾選一般蟲害防治(右側)
    c.drawString(180, height - 385, true_false_return(customer_info['pestControlR1_1']))
    c.drawString(180, height - 410, true_false_return(customer_info['pestControlR1_2']))
    c.drawString(180, height - 437, true_false_return(customer_info['pestControlR1_3']))
    c.drawString(180, height - 462, true_false_return(customer_info['pestControlR1_4']))
    c.drawString(180, height - 490, true_false_return(customer_info['pestControlR1_5']))

    # 蟲紙
    c.drawString(250, height - 490, customer_info['pestPaper'])

    # 勾選鼠害防治(左側)
    c.drawString(315, height - 385, true_false_return(customer_info['mouseControlL1_1']))
    c.drawString(315, height - 410, true_false_return(customer_info['mouseControlL1_2']))
    c.drawString(315, height - 437, true_false_return(customer_info['mouseControlL1_3']))
    c.drawString(315, height - 462, true_false_return(customer_info['mouseControlL1_4']))
    c.drawString(315, height - 490, true_false_return(customer_info['mouseControlL1_5']))

    # 勾選鼠害防治(右側)
    c.drawString(445, height - 385, true_false_return(customer_info['mouseControlR1_1']))
    c.drawString(445, height - 410, true_false_return(customer_info['mouseControlR1_2']))
    c.drawString(445, height - 437, true_false_return(customer_info['mouseControlR1_3']))
    c.drawString(445, height - 462, true_false_return(customer_info['mouseControlR1_4']))
    c.drawString(445, height - 490, true_false_return(customer_info['mouseControlR1_5']))

    # 捕鼠
    c.drawString(520, height - 435, customer_info['mouseQuantity'])

    # 其他資訊
    c.drawString(100, height - 525, customer_info['todoList']) 
    text_object = c.beginText(40, height - 547)
    text_object.setFont("twKai", 12)
    add_wrapped_text(text_object, customer_info['workReport'], 31)
    c.drawText(text_object)
    c.drawString(105, height - 695, customer_info['technician'])
    c.drawString(105, height - 725, customer_info['pharmaceuticalTechnician'])

    # 保存PDF
    c.save()

# 範例數據
# data = '已完成施工，無異常，這句話看似簡單，卻承載著大量的工作與責任。首先，施工過程是一個繁瑣而複雜的任務，涉及到許多不同的階段和專業技能。從最初的設計圖紙到材料選擇，再到實際施工，每一個環節都需要嚴格的監督與管理。施工人員必須確保所有的工序都按照計劃進行，並且在過程中必須處理各種突發情況，例如天氣變化、材料延遲或意外的技術問題。其次，「無異常」這三個字代表了施工過程中沒有出現任何問題或偏差。這不僅僅是一個簡單的結果，更是施工質量和管理水平的體現。在現代建築施工中，無異常的完成意味著所有的設計規範都得到了嚴格遵守，所有的安全措施都得到了有效的實施。'

# customer_info = {
#     'clientName': '張三',
#     'billName': '張三的帳單',
#     'invoiceNumber': 'INV-123456',
#     'clientPhone': '0912-345-678',
#     'clientContactPerson': '李四',
#     'constructionPersonInCharge': '王五哥',
#     'constructionPersonInChargePhone': '0912-345-678',
#     'constructionDate': '2024/10/11 00:00 - 2024/01/01 00:00',
#     'constructionAddress': '台北市中正區',
#     'construction': "多次",
#     'monthly': "10",
#     'quarterly': "10",
#     'yearly': "10",
#     'pestControl': True,
#     'fleasControl': True,
#     'temiteControl': True,
#     'powerControl': True,
#     'rodentControl': True,
#     'otrher': True,
#     'drug1_1': "E一之一",
#     'drug1_2': "E一之二",
#     'drug1_3': "E一之三",
#     'drug1_4': "E一之四",
#     'drug1_5': "E一之五",
#     'drug2_1': "B二之一",
#     'drug2_2': "B二之二",
#     'drug2_3': "B二之三",
#     'drug2_4': "B二之四",
#     'drug2_5': "B二之五",
#     'drug3_1': "C二之一",
#     'drug3_2': "C二之二",
#     'drug3_3': "C二之三",
#     'drug3_4': "C二之四",
#     'drug3_5': "C二之五",
#     'drug4_1': "D二之一",
#     'drug4_2': "D二之二",
#     'drug4_3': "D二之三",
#     'drug4_4': "D二之四",
#     'drug4_5': "D二之五",
#     'pestControlL1_1': True,
#     'pestControlL1_2': True,
#     'pestControlL1_3': True,
#     'pestControlL1_4': True,
#     'pestControlL1_5': True,

#     'pestControlR1_1': True,
#     'pestControlR1_2': True,
#     'pestControlR1_3': True,
#     'pestControlR1_4': True,
#     'pestControlR1_5': True,
#     'pestPaper': "10",

#     'mouseControlL1_1': True,
#     'mouseControlL1_2': True,
#     'mouseControlL1_3': True,
#     'mouseControlL1_4': True,
#     'mouseControlL1_5': True,

#     'mouseControlR1_1': True,
#     'mouseControlR1_2': True,
#     'mouseControlR1_3': True,
#     'mouseQuantity': "10",

#     'mouseControlR1_4': True,
#     'mouseControlR1_5': True,

#     'todoList': '施工項目一、施工項目二',
#     'workReport': data,
#     'technician': "我操作",
#     'pharmaceuticalTechnician': "我施藥",
# }

# 生成PDF
# generate_pdf_with_chinese(customer_info)