from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from views.view import TaskView as t
from controllers.task_controller import TaskController as c
import kb



class BotApp:

    def __init__(self,token):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot)
        self.state = 0
        self.commands = ['/add ','/list','/done','/remove']

        

        self.register_handlers()

    def register_handlers(self):
        self.dp.register_message_handler(self.start_command, commands=['start'])
        self.dp.register_message_handler(self.add_task_command, commands=['add'])
        self.dp.register_message_handler(self.list_tasks_command, commands=['list'])
        self.dp.register_message_handler(self.remove_task_command, commands=['remove'])
        self.dp.register_message_handler(self.done_task_command, commands=['done'])
        self.dp.register_message_handler(self.command)


    async def start_command(self, message: types.Message):
        greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        for command in self.commands:
            button = KeyboardButton(command)
            greet_kb.insert(button)

        await message.reply("Привет!", reply_markup=greet_kb)
        result = t.start_message()
        await message.reply(result)


    async def command(self, message: types.Message):
        if self.state == 1:
            await self.add_task(message)
        elif self.state == 2:
            await self.remove_task(message)
        elif self.state == 3:
            await self.done_task(message)
        else:
            await self.start_command(message)

        self.state = 0

    

    async def add_task_command(self, message: types.Message):
        await message.reply("Enter the task description:")
        self.state = 1
    
    async def remove_task_command(self, message: types.Message):
        await message.reply("Enter the task id:")
        self.state = 2

    async def done_task_command(self, message: types.Message):
        await message.reply("Enter the task id:")
        self.state = 3
    
    
    
    
    async def add_task(self,message: types.Message):
        task_description = message.text
        task_id = message.message_id

        result = c().add_task(task_description, task_id)
        await message.reply(result)

    

    async def remove_task(self, message: types.Message):
        task_id = message.text
        result = c().delete_task(int(task_id))
        await message.reply(result)


    async def done_task(self, message: types.Message):
        task_id = message.text
        result = c().done_task(int(task_id))
        await message.reply(result)
    

    async def list_tasks_command(self, message: types.Message):
        result = c().task_list()
        await message.answer(result)

    def start(self):
        from aiogram import executor
        executor.start_polling(self.dp, skip_updates=True)

    

