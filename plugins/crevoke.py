from pyrogram import *
from pyrogram.errors import *
from config import *


@Client.on_message(filters.user(ADMIN) & filters.command(["crevoke"]))
async def link(bot, message):  
    if len(message.command) == 1:
      await message.reply_text('--**Use This Format**-- \n\n **/crevoke {chat id or username} {invite link}** ')
    else:
      try:
         link = message.text.split()[2]
         iid = message.text.split()[1]
         await bot.revoke_chat_invite_link(iid, invite_link=link)
         await message.reply_text(f'Succesfuly revoked `{link}`')
      except:
         await message.reply_text(f'**ERROR**')
