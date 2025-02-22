from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='Busket')],
                                     [KeyboardButton(text='Contacts'),
                                      KeyboardButton(text='About us')]],
                                      resize_keyboard=True,
                                      input_field_placeholder='Choose section from menu...')

catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='T-shirts', callback_data='t-shirts')],
                                                [InlineKeyboardButton(text='Sneakers',callback_data='sneakers')],
                                                [InlineKeyboardButton(text='Hats', callback_data='hats')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Send number', request_contact=True)]],
                                 resize_keyboard=True)