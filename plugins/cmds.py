from pyrogram import *
from pyrogram.errors import *
from config import *


@Client.on_message(filters.user(ADMIN) & filters.command(["cmds"]))
async def link(bot, message):  
      await message.reply_text("""
✘ Commands Available -

• `/invite`
    Get Main Chnnel Custom Invite Link.

• `/invite <text/reply to msg/reply to document>`
    Carbonise the text, with random bg colours.

• `{i}ccarbon <color ><text/reply to msg/reply to document>`
    Carbonise the text, with custom bg colours.
""")
