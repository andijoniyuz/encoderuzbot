from collections import defaultdict

from pyrogram import filters


BOT_TOKEN = "BOT_TOKENI"
BANNED_USERS = filters.user()
USERS = defaultdict(list)
MESSAGES = 1
SECONDS = 15
