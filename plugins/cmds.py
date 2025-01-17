from pyrogram import *
from pyrogram.errors import *
from config import *


@Client.on_message(filters.command(["cmds", "cmd"]))
async def link(bot, message):  
      await message.reply_text("""
✘ Commands Available -

• `/invite or /getlink`
    Get Main Channel Custom Invite Link.

• `/invite [custom name] or /getlink [custom name]`
    Generate Invite Link With Custom Name.
    
• `/revoke [invite link] `
    Revoke Given Link **--[ADMIN CMD]--**.

• `/ilink [channel id] `
   Generate Invite Link With Given id.
   
• `/crevoke [chat id or username] [invite link] `
   Revoke Invite Link Using Given Chat And Invite Link.
""")
