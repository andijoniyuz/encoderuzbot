from os.path import lexists
from os import remove
from asyncio import subprocess, create_subprocess_exec
from uuid import uuid4


async def convert_mp3(message):
    messag = await message.reply("Audio yuklanmoqda...")
    new_mp3_file = f"{uuid4()}.mp3"
    mp3_file = await message.download(file_name=new_mp3_file)
    
    if lexists(mp3_file):
        messa = await messag.edit("Audio yuklandi")
        commands = [
            "ffmpeg",
            "-i",
            mp3_file,
            "-b:a",
            "16k",
            "-af",
            "afftdn=nf=-25",
            new_mp3_file
        ]
        process = await create_subprocess_exec(
            *commands,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if lexists(new_mp3_file):
            mes = await messa.edit("Yuborilmoqda...")
            await message.reply_audio(new_mp3_file, title=message.audio.title, performer=message.audio.performer)
            await mes.delete()
            remove(new_mp3_file)
            remove(mp3_file)
        else:
           return False
