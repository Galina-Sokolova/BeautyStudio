from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
ikb_start = InlineKeyboardMarkup(row_width=2)
ib1=InlineKeyboardButton(text='Палитра', callback_data='#')
ib2=InlineKeyboardButton(text='Свободные слоты', callback_data='#')
ib3=InlineKeyboardButton(text='Прайс на услуги', callback_data='#')
ib4=InlineKeyboardButton(text='Важная информация', callback_data='#')
ib5=InlineKeyboardButton(text='Инстаграмм', callback_data='#')


ikb_start.add(ib1, ib2).add(ib3).add(ib4, ib5)

#Принажатии на кнопку свободные слоты, обращение к гугл таблицам и нужна кнопка записи на прием
ikb_register_to_master = InlineKeyboardMarkup()
ikb_register_to_master.add(InlineKeyboardButton(text='Запись на прием', callback_data='Запись на прием'))