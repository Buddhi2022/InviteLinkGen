from pyrogram import *
from pyrogram.errors import *
from config import *


@Client.on_message(filters.user(ADMIN) & filters.command(["revoke"]))
async def link(bot, message):  
    if len(message.command) == 1:
      await message.reply_text('--**Use This Format**-- \n\n **/revoke {invite link}** ')
    else:
      try:
         link = message.text.split()[1]
         await bot.revoke_chat_invite_link(-1001758633913, invite_link=link)
         await message.reply_text(f'Succesfuly revoked `{link}`')
      except:
         await message.reply_text(f'**ERROR**')
