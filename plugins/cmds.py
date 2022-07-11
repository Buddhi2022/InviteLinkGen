from pyrogram import *
from pyrogram.errors import *
from config import *


@Client.on_message(filters.user(ADMIN) & filters.command(["revoke"]))
async def link(bot, message):  
    if len(message.command) == 1:
      await message.reply_text('--**Use This Format**-- \n\n **/revoke {invite link}** ')
