import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import requests
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    channel = bot.get_channel(กำหนด channel_id ที่อยากให้บอทประกาศ)
    await channel.send(f'เข้าสู่ระบบในฐานะ {bot.user} (ID: {bot.user.id})')
    message = "ปัจจุบันมี {0} คนในเซิร์ฟเวอร์นี้: {1}".format(
        len(bot.users), ", ".join([user.name for user in bot.users])
    )
    channel = bot.get_channel(กำหนด channel_id ที่อยากให้บอทประกาศ)
    if channel:
        if len(message) <= 2000:
            await channel.send(message)
        else:
            # แบ่งข้อความออกเป็นส่วนย่อย 2000 ตัวอักษร
            messages = [message[i:i+2000] for i in range(0, len(message), 2000)]
            for msg in messages:
                await channel.send(msg)


    
load_dotenv()
token = os.getenv(ประกาศตัวแปรใน env)
bot.run(token)

