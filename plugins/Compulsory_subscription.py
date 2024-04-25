from pyrogram import Client,filters, types
import asyncio
import json 
import requests

API_KEY = "<TOKN>"

app = Client('bots', 
    bot_token=API_KEY,  # API_KEY _ TOKN
    api_id=12345678,      # API_ID TELEGRMA ACCONET
    api_hash='95f5f60488u996e33a34f297c734d048'    # API_HAHS TELEGRMA ACCONET
)

def JOIN_CHANNL(channl_username: str, ) : 
    return types.InlineKeyboardMarkup([
        [types.InlineKeyboardButton(' ⤷ CHECK ', callback_data='CHECK_JOIN'),types.InlineKeyboardButton(' ⤷ CH ', url=f't.me/{channl_username}')]])

Message_Bot = {'JOIN_CHANNL':
                u"عذرن عزيزي انت لست مشترك في قناة البوت 🧩💬."
                u"\n\n • يجب عليك الاشترك في قناة البوت لي تتمكن من استخدام البوت  ✅💭. "
                u"\n CH → @{}    "
                u"\n\n ⤷ 𝗕𝗬 @R_AFX - @radfx2 . 💭"
                u"      ",}

async def CHECK_USER_JOIN(channls_join: list, user_id : int):
    c ,r = None ,False
    statues = ['administrator','creator','member','restricted']
    for channl in channls_join:
        url =f"https://api.telegram.org/bot{API_KEY}/getChatMember?chat_id=@{channl}&user_id={str(user_id)}"
        respons = requests.get(url)
        JSObj = json.loads(respons.text) 
        user_state = JSObj['result']['status']
        if user_state in statues:r = True 
        else : 
            r = False
            c = channl
            return r,c
    return r,c


Channls = ['radfx2', 'W7_7WW']

@app.on_message(filters.regex('^/start$') & filters.private)
async def START_BOT(_, Message: types.Message):
    chat_id, message_id, user_id = Message.chat.id, Message.id, Message.from_user.id
    CHECK, Channl= await CHECK_USER_JOIN(Channls, user_id)
    if not CHECK:
        await app.send_message(chat_id=chat_id, text=Message_Bot['JOIN_CHANNL'].format(Channl), reply_markup=JOIN_CHANNL(Channl))
        return 
    await app.send_message(chat_id=chat_id, text='Hey, Broo .')
    

@app.on_callback_query(filters.regex('^CHECK_JOIN$'))
async def  CHECK_JOIN(_, query: types.CallbackQuery):
    CHECK, Channl= await CHECK_USER_JOIN(Channls, query.from_user.id)
    if not CHECK:
        await app.answer_callback_query(query.id, 'Be sure to subscribe to my channel first .', show_alert=True)
        return 
    await app.edit_message_text(chat_id=query.message.chat.id, text='Hey, IS Bots .', message_id=query.message.id)


asyncio.run(app.run())