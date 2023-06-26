import openpyxl

path = openpyxl.Workbook()

def create_row(*args):
    args = list(args)
    sheet = path.active
    for number in args:
        sheet.append([number])
    path.save('minha_planilha.xlsx')

receb_number = 231232131,'JJJJJ','JCAIOJJ',21,0

create_row(*receb_number)

path.close()