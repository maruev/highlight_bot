from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, executor
from utils import get_regs, get_orders_list
from config import regs_folder

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

regs = get_regs(regs_folder)
orders = get_orders_list(regs)

if __name__ == '__main__':
    from handlers import dp
    print(orders)
    while True:
        executor.start_polling(dp)
