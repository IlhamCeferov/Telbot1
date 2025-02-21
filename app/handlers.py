from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Hello!', reply_markup=kb.main)
    await message.reply('How are you?')

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('You clicked on help button')

@router.message(F.text == 'Catalog')
async def catalog(message:Message):
    await message.answer('Choose category', reply_markup=kb.catalog)

@router.callback_query(F.data == 't-shirts')
async def t_shirts(callback: CallbackQuery):
    await callback.answer('You choosed category', show_alert=True)
    await callback.message.answer('You choosed T-shirts category')