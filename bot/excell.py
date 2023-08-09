import openpyxl
from typing import Optional

def get_xlsx_rows(folder: str, file: str, cell = 'D', range_start = 1, range_stop = 3000, row_include = '-') -> list[str]:
        wb = openpyxl.reader.excel.load_workbook(filename= folder + '/' + file)
        wb.active = 0
        sheet = wb.active
        rows_list = []
        for i in range(range_start, range_stop):
            val = sheet[cell.upper()+str(i)].value
            if val != None and row_include in val:
                rows_list.append(val)
        return rows_list

if __name__ == '__main__':
    print(get_xlsx_rows(folder='./reg', file='DNS1.xlsx'))