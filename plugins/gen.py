from pyrogram import *
from pyrogram.errors import *

'''
Cmds

/getlink or /getlink [any name]
/invite or /invite [any name]

'''

@Client.on_message(filters.chat(-1001203589911) & filters.command(["getlink", "invite"]))
async def link(bot, message):
    if len(message.command) == 1:
     link = await bot.create_chat_invite_link(-1001698267062, name=message.from_user.first_name)
     await message.reply_text(f"--**Link Generated**-- \n\n**Link -{link.invite_link}\nGenerated by - {link.name}\nGenerated Date - {link.date}**")
    else:
     name = message.text.split()[1]
     link = await bot.create_chat_invite_link(-1001698267062, name=name)
     await message.reply_text(f"--**Link Generated**-- \n\n**Link Name - {link.name}\nLink -{link.invite_link}\nGenerated by - {message.from_user.mention}\nGenerated Date - {link.date}**")
    
