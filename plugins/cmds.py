from pyrogram import *
from pyrogram.errors import *
from config import *


@Client.on_message(filters.user(ADMIN) & filters.command(["revoke"]))
async def link(bot, message):  
      await message.reply_text('--**Use This Format**-- \n\n **/revoke {invite link}** ')
