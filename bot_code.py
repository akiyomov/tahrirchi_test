import logging
import pandas as pd
from main import getText
import re
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

API_TOKEN = '5774000692:AAElHoa4kPwqc25z-MSuippuKdgyPcpMh0s'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Hi {message.from_user.first_name}!")
    await message.answer(f"Send me a link that consists text, then I will convert to csv.")




@dp.message_handler()
async def echo(message: types.Message):
    url = message.text
    source_url, access_datetime, content = getText(url)
    word = re.findall(r'(?<!\S)[a-zA-Z0-9]\S*[a-zA-Z](?!\S)', content)
    data = pd.DataFrame({"source_url":source_url,"access_datetime":access_datetime,"content":content,"word":word})
    counter = []
    for i in range(len(data)):
        counter.append(data['content'][i].count(data['word'][i]))
    data['count'] = counter
    data.to_csv('step_1&2&3.csv',) #mode='w+'
    path_csv = InputFile(path_or_bytesio="step_1&2&3.csv")
    await message.reply_document(path_csv,caption="Test mode")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)