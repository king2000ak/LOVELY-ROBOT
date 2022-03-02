import os
from pyrogram import Client, filters
from pyrogram.types import *

from LovelyRobot.conf import get_str_key
from LovelyRobot import pbot
 
 # pls don't delete
REPO_TEXT = "*Ansi👶 [BOT](https://te.legra.ph/file/613fc2c835c8799cc8a79.jpg) will Make Your Groups Secured And it's have a lot of fun features (:  ! \n\n↼ Owner ⇀ : 『 [Ansi👶](https://telegra.ph/file/80aebbee694648b175378.mp4) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» Ansi👶 «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://te.legra.ph/file/93cb78f11711e44a5258d.jpg"),        
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
