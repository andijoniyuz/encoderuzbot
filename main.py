from pyrogram import Client

from config import BOT_TOKEN


app = Client("tilon", "2424010",
             "9fb173ded391c8aca77667709be270e3",
             bot_token=BOT_TOKEN,
             plugins={"root": "plugins"},
             )
app.run()
