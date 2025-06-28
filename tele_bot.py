import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import g4f
import sys

import g4f.Provider

class Reference:
    '''
    A class to store previously response from the chatGPT API
    '''
    def __init__(self) -> None:
        self.response = ""

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
reference = Reference()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

#model name
MODEL_NAME = "gpt-4"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """A function to clear the previous conversation and context.
    """
    reference.response = ""



@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):

    await message.reply("Hi\nI am Tele Bot!\Created by sarada. How can i assist you?")



@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")



@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm chatGPT Telegram bot created by PWskills! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)


@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    user_input= message.text
    print(f">>> USER: \n\t{user_input}")
    response = g4f.ChatCompletion.create(
        model = MODEL_NAME,
        messages = [
            {"role": "user", "content": message.text} #our query 
        ]
    )
    print(f">>>GPT:\n\t{response}")
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)
