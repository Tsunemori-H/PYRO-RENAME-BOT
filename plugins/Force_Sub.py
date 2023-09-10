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
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from pyrogram import Client, filters
from pyrogram.types import (
    ChatJoinRequest,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config import Config
from helper.database import db


async def not_subscribed(_, client: Client, message: Message):
    await db.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    if await db.is_req_user(message.from_user.id):
        return False
    else:
        return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client: Client, message: Message):
    buttons = [[InlineKeyboardButton(text="Join Channel", url=Config.FORCE_SUB)]]
    text = "We Create Codes, We Buy Server, We Host Bots, We Provide Free Service. \nJoining Our Channel is The Least You Can Do To Respect Our Hardwork."
    if await db.is_req_user(message.from_user.id):
        return
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_chat_join_request(filters.chat(Config.FSUB_ID))
async def new_member_join(client: Client, request: ChatJoinRequest):
    user_id = request.from_user.id
    name = request.from_user.first_name
    username = request.from_user.username
    date = request.date
    context = {
        "user_id": user_id,
        "name": name,
        "username": username,
        "date": date,
    }
    if await db.is_req_user(user_id):
        return
    await db.add_req_user(context)
