"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "25697264")
    API_HASH  = os.environ.get("API_HASH", "fc1bce8441f3c90b719bc86098137a3d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6343836266:AAHZjl71px5zLk9XumV71JhIrJhSl1Hv0Gk") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","rename")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://utahakane003:utahakane003@cluster0.xyoubmt.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/4e3b3a92124c048ca4e36.png")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '682111519').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Rename_File") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001537276104"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>𝗛𝗲𝗹𝗹𝗼!! 𝗖𝗼𝗺𝗽𝗮𝗱𝗿𝗲 {} ꈍ◡ꈍ
<i>» I'm A Very Powerful And Stable Rename Bot.
» I Can Rename Any Telegram Files Easily.
» Please Send Only 1 File At A Time As Per Telegram Restrictions.
» I Can Convert Any Video Into File And Other Way Around.
» I Am A Part of ⚡️⚡️Sonic Family⚡️⚡ So You Must Join @Sonic_Otakus And @Anime_Flix_Pro To Use Me.
» Enjoy Your Renaming Experience.</i></b>"""

    ABOUT_TXT = """<b><i>» I Am Created By - <a href='https://t.me/NORMAN_2_2_1_9_4'>𝗡𝗼𝗿𝗺𝗮𝗻</a>.
» If You're Intrested In Paid Promotion/Bot Script.
» Contact My <a href='https://t.me/NORMAN_2_2_1_9_4'>𝗠𝗮𝘀𝘁𝗲𝗿</a>.</i></b>"""

    HELP_TXT = """
🌌 <b><u>ʜᴏᴡ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>»</b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>»</b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>»</b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.

📑 <b><u>ʜᴏᴡ ᴛᴏ sᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ</u></b>
<b>»</b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>»</b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>»</b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

<b>ᴇ𝘅ᴀᴍᴩʟᴇ</b> - 
/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}

✏️ <b><u>ʜᴏᴡ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴀ ғɪʟᴇ</u></b>
<b>»</b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
» 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗠𝘆 :- <a href=https://t.me/NORMAN_2_2_1_9_4>𝗠𝗮𝘀𝘁𝗲𝗿</a>
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """» Special Thanks To ⚡️⚡️Sonic Family⚡️⚡ For Providing Such A Miraculous Bot In Hard Times. \nJoin @Sonic_Otakus And @Anime_Flix_Pro To Show Support."""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


