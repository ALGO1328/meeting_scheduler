from telebot.async_telebot import AsyncTeleBot

import config

import aiohttp

import database_users

BOT = AsyncTeleBot(token=config.TOKEN)

async def main():
    """Асинхронный обработчик отправки команды регистрации, database_users.check_user_exist проверяет,
    зарегистрирован ли пользователь, database_users.register_user регистрирует пользователя"""
    @BOT.message_handler(commands=['register'])
    async def register(message):
        if database_users.check_user_exist(message):
            await BOT.send_message(message.chat.id, text="Вы уже зарегистрированы")
        else:
            if database_users.register_user(message):
                await BOT.send_message(message.chat.id, text="Вы успешно зарегистрировались")
                await BOT.send_message(message.chat.id, text=config.INSTRUCTIONS)
            else:
                await BOT.send_message(message.chat.id, text="Ошибка регистрации, попробуйте позже")

    @BOT.message_handler(commands=['meet'])
    async def meeting(message):
        if database_users.check_user_exist(message):
            if "/meet" in message.text and "@" in message.text:
                args = [arg for arg in message.text.split()][1:]
                print(args)

        else:
            await BOT.send_message(message.chat.id, text="Сначала вам необходимо зарегистрироваться командой /register")
    await BOT.infinity_polling()

main()



