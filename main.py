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

print(a)
async def log():
    if -1001203589911:
       await bot.send_message(-1001203589911, text=a)
       

bot.run(log())
idle()
