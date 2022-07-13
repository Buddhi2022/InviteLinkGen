from pyrogram import Client ,idle
from config import *

plugins = dict(root="plugins")

bot=Client( 
    "teInvi",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins)

bot.start()
uname = (bot.get_me()).username
a = f"""
`╭━━╮╱╱╱╭━━━┳╮
╰┫┣╯╱╱╱┃╭━╮┃┃
╱┃┃╭╮╭╮┃┃╱┃┃┃╭┳╮╭┳━━╮
╱┃┃┃╰╯┃┃╰━╯┃┃┣┫╰╯┃┃━┫
╭┫┣┫┃┃┃┃╭━╮┃╰┫┣╮╭┫┃━┫
╰━━┻┻┻╯╰╯╱╰┻━┻╯╰╯╰━━╯`
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➖➖➖➖➖➖➖➖➖➖
@{uname} has been deployed!
➖➖➖➖➖➖➖➖➖➖
Support: @AlphaTm_Botz_chat
➖➖➖➖➖➖➖➖➖➖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
L = -1001522887959
print(a)
async def log():
    if L:
       await bot.send_message(L, text=a)
       

bot.run(log())
idle()
