from aiogram.types import Message
from config import admins_id, users
from main import dp, orders

@dp.message_handler()
async def hand(message: Message):
    try:
        text = message.text.upper()
        orders_list = []
        flag = False
        if message.from_user.id not in admins_id:
            for order in orders:
                if order not in orders_list and (order.upper() in text 
                    or order.upper().replace('-', '--', 1) in text 
                    or order.upper().replace('-', ' ', 1) in text 
                    or order.upper().replace('-', '', 1) in text  
                    or order.upper().replace('-', ' -', 1) in text 
                    or order.upper().replace('-', '  ', 1) in text 
                    or order.upper().replace('-', '- ', 1) in text 
                    or order.upper().replace('-', ' - ', 1) in text 
                    or order.upper().replace('-', ' --', 1) in text 
                    or order.upper().replace('-16-', '16-', 1) in text 
                    or order.upper().replace('-', '_', 1) in text 
                    or order.upper().replace('-', '-- ', 1) in text):
                    flag = True
                    orders_list.append(order)
            if flag:
                mes = '\n'.join(orders_list) + '\n' + ' '.join(users)
                await message.answer(text=mes, reply=True)
    except:
        print('err')