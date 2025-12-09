import xlrd

def reading_testdata(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)
    rows=worksheet.get_rows()
    header=next(rows)

    d={}
    for ele in rows:
        d[ele[0].value]=ele[1].value
        return d
