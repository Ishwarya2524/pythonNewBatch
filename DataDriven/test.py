import openpyxl
excel_loc=r"C:\Users\ARUL KUMARAN\PycharmProjects\pythonProjectselenium10.00 PM\Excel\sheet.xlsx"
w=openpyxl.load_workbook(excel_loc)
sheet=w.active
c=sheet.cell(1,1)
data=c.value
if data=="Name":
    c.value="iphone name"
w.save(excel_loc)
print("done...")
