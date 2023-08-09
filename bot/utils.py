import os
from excell import get_xlsx_rows
from config import regs_folder

def get_regs(regs_folder: str) -> list[str]:
    regs = []
    for root, dirs, files in os.walk(regs_folder):
        for filename in files:
            regs.append(filename)
    return regs

def get_orders_list(regs_list: list[str]) -> list[str]:
    orders_list = []
    for reestr in regs_list:
        orders_list.extend(get_xlsx_rows(folder=regs_folder, file=reestr))
    return orders_list

if __name__ == '__main__':
    print(get_orders_list(get_regs(regs_folder)))