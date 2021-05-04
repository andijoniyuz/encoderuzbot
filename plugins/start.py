from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.private & filters.command('start'))
async def _start(_, message: Message):
    await message.reply("Salom, menga musiqa yuboring va men uni sizga xajmini kichraytirib beraman.")
