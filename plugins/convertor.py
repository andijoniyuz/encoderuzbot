from pyrogram import Client, filters
from pyrogram.types import Message

from functions import convertor_mp3, is_flood
from config import BANNED_USERS


@Client.on_message(filters.private & filters.audio)
async def new_user(_, message: Message):
    if is_flood.is_flooder(message.from_user.id):
        BANNED_USERS.add(message.from_user.id)
        try:
            await message.reply("Bitta musiqani 10 soniyada xajmini kichaytirishingiz mumkin.\nKuting...")
        except:
            pass
    elif message.from_user.id in BANNED_USERS:
        await convertor_mp3.convert_mp3(message)
        BANNED_USERS.remove(message.from_user.id)
    else:
        await convertor_mp3.convert_mp3(message)
