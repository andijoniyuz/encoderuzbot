from pyrogram import Client

app = Client("tilon", "2424010",
             "9fb173ded391c8aca77667709be270e3",
             bot_token='1280184771:AAFtbT9NL-E4ZH0JrpjiHutkj3O-Xz9JSRQ',
             plugins={"root": "plugins"},
             )
app.run()
