import serial
import time
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ser = serial.Serial('COM4', 9600) #Maybe in your arduino will be another port
time.sleep(2) 

API_TOKEN = '8616031036:AAHlPfGmqo9CEXO9BTEFy6Chl1CVWBuJjzI' #there you insert token of your bot


bot = Bot(token=API_TOKEN)
dp = Dispatcher()
def get_main_keyboard():
    buttons = [[KeyboardButton(text="red"), 
               KeyboardButton(text="green")], 
               [KeyboardButton(text="both")]]
    
    Keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="Select mode")
    return Keyboard
    
    


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Salute {message.from_user.full_name} which state of led you will choose?",  reply_markup=get_main_keyboard())


@dp.message(F.text == "green")
async def light_on_green(message: types.Message):
    try:
       ser.write(b'2')
       await message.answer("turn on green led")
    except Exception as e:
        print(f"Something went wrong :0, {e}")
    



@dp.message(F.text == "red")
async def light_on_red(message: types.Message):
    try:
       ser.write(b'1')
       await message.answer("turn on red led")
    except Exception as e:
        print(f"Something went wrong :0, {e}")
    


@dp.message(F.text == "both")
async def light_on_both(message: types.Message):
    try:
       ser.write(b'3')
       await message.answer("turn on both led")
    except Exception as e:
        print(f"Something went wrong :0, {e}")
    


async def main():
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stoped")