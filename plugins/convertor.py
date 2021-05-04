from time import time
from typing import Union

from pyrogram import Client, filters
from pyrogram.types import Message

from .config import MESSAGES, SECONDS, USERS, BANNED_USERS
from functions.convertor_mp3 import convert_mp3

def is_flood(uid: int) -> Union[bool, None]:

    USERS[uid].append(time())
    if len(list(filter(lambda x: time() - int(x) < SECONDS, USERS[uid]))) > MESSAGES:
        USERS[uid] = list(filter(lambda x: time() - int(x) < SECONDS, USERS[uid]))
        return True


@Client.on_message(filters.private & filters.audio)
async def new_user(client: Client, message: Message):
    await convert_mp3(message)