from collections import defaultdict

from pyrogram import filters

BANNED_USERS = filters.user()
USERS = defaultdict(list)
MESSAGES = 1
SECONDS = 3
