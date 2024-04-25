from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app
from config import Almortagel

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not Almortagel:
        return
    try:
        try:
            await app.get_chat_member(Almortagel, msg.from_user.id)
        except UserNotParticipant:
            if Almortagel.isalpha():
                link = "https://t.me/" + Almortagel
            else:
                chat_info = await app.get_chat(Almortagel)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"~︙عزيزي {msg.from_user.mention} \n~︙عليك الأشتراك في قناة البوت \n~︙قناة البوت : @{Almortagel}.",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("<قناة البوت>", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat {Almortagel}!")
