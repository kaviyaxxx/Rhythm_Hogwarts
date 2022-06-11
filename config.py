import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Vars
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1120271521 1142823204 1436040399 1380582913 1670961080").split())
MONGO_URI = os.getenv("MONGO_URI")
MAIN_CHANNEL = int(os.environ.get("MAIN_CHANNEL", "-1001618208549"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001744145224"))
PRIVATE_LOG = int(os.environ.get("PRIVATE_LOG", "-1001744145224"))
force_subchannel = os.getenv("FSUB", "memehubtgsl")
OWNER_ID = int(os.environ.get("OWNER_ID", "1120271521"))
#Strings 
WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>Type your query here..\nI'll respond to your query as earliest</code> 😉\n\nуσυ ωαииα тσ киσω αвσυт мє😌? яєα∂ вєℓσω\n\nαвσυт @ImDark_Empire:-\n •му иαмє:- 𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 \n •му αgє:- υикиσωи🌝\n •¢σмρυтєя ℓαиgυαgє:- [𝖘𝖊𝖊 𝖍𝖊𝖗𝖊](https://github.com/DARKEMPIRESL) \n•¢нє¢к [About 𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊](https://t.me/darks_pm_bot) fσя мσяє\n\nPlz Don't Send Stickers 🥲\nReason :- [This](https://t.me/ultchat/19589)"
USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
USER_DETAILS = "<b>FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
FORCESUB_TEXT = "**❌ Access Denied ❌**\n\ⱤⱧɎ₮Ⱨ₥ Ø₣ ⱧØ₲₩₳Ɽ₮₴™ eke nathuva Mokatada yako Botva Start Kare kkk😒😒\n♻️Join and Try Again.♻️"
HELP_STRING = "If you need to contact admins use this bot...😎😎"
START_STRING ="""
Hi {}, Welcome to  𝄟❤️💚ⱤⱧɎ₮Ⱨ₥ Ø₣ ⱧØ₲₩₳Ɽ₮₴™💛💙 Official Bot.
 Bot By [𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](https://t.me/ImDark_Empire)
"""


#Inline Btn
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - 𝄟❤️💚ⱤⱧɎ₮Ⱨ₥ Ø₣ ⱧØ₲₩₳Ɽ₮₴™💛💙', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', user_id=f"@SL_BOTS_TM")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )
                  
CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖘𝖊", callback_data="cloce")
                 ]]
                 )
                                                    
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="👻 ʙᴀᴄᴋ 👻",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@Scamander_01")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp"),
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/kaviyaxxx/Rhythm_Hogwarts")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share"),
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ᴄʜɴʟ ➕", switch_inline_query="cshare")
                 ],
                 [
                 InlineKeyboardButton("Team SL Bots🇱🇰", url="https://t.me/SLBotOfficial"),
                 InlineKeyboardButton("Support - https://t.me/SLBotsChat ", url="https://t.me/SLBotsChat")
                 ]                 
                 [
                 InlineKeyboardButton("┊𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』", url="https://t.me/AlphaTm_Botz"),
                 InlineKeyboardButton("Support - ┊𝙰𝙻𝙿𝙷𝙰 Botz Chat ", url="https://t.me/AlphaTm_Botz_chat")
                 ]]
                  )

ADMIN_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('༒≛⃝❁🖤ᵏᵃᵛⁱʸᵃ🖤≛༻ 『 ȞP₣ŚĻ™️°』|【】ℙ𝕁𝔽𝕊𝕃™️°【】┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="Scamander_01")
                 ],
                 [                 
                 InlineKeyboardButton('ℚ𝕌𝔼𝔼ℕ 𝔻𝔼𝔼ℙ𝔻𝔸ℝ𝕂 ᴬᴷᴬ Morgana', user_id="Lily_MORGANA_DEEPDARK")
                 ],
                 [                 
                 InlineKeyboardButton('▪️', user_id="The_Girl_Who_Lived_2005")
                 ],
                 [                 
                 InlineKeyboardButton('𝄟≛⃝❁❖💙Eαʂԋαɳҽҽ Uɱαყαɳɠαɳα💙❖≛⃝❁𝄟', user_id="Eashaaa")
                 ],
                 [                 
                 InlineKeyboardButton('ঔ৫⃟➤ℍ𝕒𝕤𝕚𝕟𝕕𝕦 𝕋𝕙𝕖𝕖𝕜𝕤𝕙𝕒𝕟𝕒 💚༻༒ ༻💚', user_id="Iron_Voldy")
                 ],
                 [                 
                 InlineKeyboardButton('𝄟≛⃝❁❖💙 ℘ɑׁׅ ꩇׁׅɑׁׅ 💙❖≛⃝ 𝄟', user_id="Devil_lover21")
                 ],
                 [
                 InlineKeyboardButton('㊌𝕾𝕬𝕹𝕯𝖀𝕹𝕴㊌ 『 ȞP₣ŚĻ™️°』', user_id="Sas_2002")
                 ],
                 [                 
                 InlineKeyboardButton('꧁❤️ ᭄ Hermione ✿༒❤️꧂【】ℙ𝕁𝔽𝕊𝕃™️°【】 『 ȞP₣ŚĻ™️°』', user_id="phynix_06")
                 ],
                 [                 
                 InlineKeyboardButton('©Kolly_FanSLᵀᴹ Fiͥlmͫs͛Ziͥllaͣ🇱🇰™ 【】ℙ𝕁𝔽𝕊𝕃™️°【】', user_id="Kolly_FanSL_1301")
                 ],
                 [                 
                 InlineKeyboardButton('H.Rathnayake', user_id="H_Rathnayake")
                 ],
                 [
                 InlineKeyboardButton('Charaka Hashan', user_id="wolf_at_alone")
                 ],
                 [                 
                 InlineKeyboardButton('shin', url="Chenu1290")
                 ],
                 [                 
                 InlineKeyboardButton('𝄟💚᭄𝔼l𝕖ν𝕖ŋ 𝕀ν𝕖ֆ༒✿💚『 ȞP₣ŚĻ™️°』|【】ℙ𝕁𝔽𝕊𝕃™️°【】', user_id="Yaoyorozu_2005")
                 ],
                 [                 
                 InlineKeyboardButton('?≛⃝❁❖👻✝️💙Udan Akalanka ≛⃝❁❖💙✝️👻', user_id="Half_Blood_Prince2006")
                 ],
                 [
                 InlineKeyboardButton('TELEDARK AKA DEEPDARK ', user_id="Tele_DeepDark")
                 ],
                 [                 
                 InlineKeyboardButton('ঔ৫⃟➤Sanemi Shinazugawa 💚༻༒ ༻💚', user_id="WindHashira_Shinazugawa")
                 ]
                 ]
                  )

OWNER_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('༒≛⃝❁🖤ᵏᵃᵛⁱʸᵃ🖤≛༻ 『 ȞP₣ŚĻ™️°』|【】ℙ𝕁𝔽𝕊𝕃™️°【】┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="Scamander_01")
                 ]]
                  )               

DEV_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™', user_id="SL_BOTS_TM")
                 ],
                 [
                 InlineKeyboardButton('ŦħȺɍᵾꝁ ɌɇnᵾɉȺ', user_id="ImTharuk")
                 ],
                 [
                 InlineKeyboardButton('unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="UnknownB_o_y")
                 ],
                 [
                 InlineKeyboardButton('༒❣️☢️╣IrØή❂mคŇ╠☢️❣️༒ ', user_id="ImGishan")
                 ],
                 [
                 InlineKeyboardButton('𝘿𝙚𝙣𝙪𝙬𝙖𝙣 🇱🇰', user_id="ImDenuwan")
                 ]]
                  )


#Rndm Stkr

OWNER_STICKER = ["CAADAgADtA8AAhUWiEuTU2os6PSW-AI",
                "CAADAgADCwMAAm2wQgN_tBzazKZEJQI",
                "CAADAgADtwEAAladvQr3FVtdLiA1jgI", 
                "CAADBQADSwQAAnxrOFaYSIaXhBE_YAI"              
         ]

STAT_STICKER = ["CAADAQAD7gMAAv5DwUe0nbeQnSoavAI",
                "CAADAgAD8QEAAladvQohKm5i6iYv7gI"              
         ]  

ADMIN_STICKER = ["CAADAgADzhMAAhDzcElTIbO4ZQ8stAI",
                "CAADBQADxwQAAgcbUFea8nhgWIiuGwI",
                "CAADBQADPAUAAtzIoFWtMe3LazkiKQI", 
                "CAADBQADDgQAAkKxWVZAvhW5fKSifwI"              
         ]
         
DEV_STICKER = ["CAADAgADaRsAAsOUWUpHrmf5mZp3EgI",
                "CAADAgADbAIAAladvQoqGV6cxNDenwI",
                "CAADAgADgQEAAiteUwteCmw-bAABeLQC", 
                "CAADBQADZgMAAvIEcFVMnMXcAqRX7gI",
                "CAADAgADFwADlp-MDlZMBDUhRlElAg"                
         ] 

HELP_STICKER = ["CAADAgADYgADWbv8JXMOJcSM3-2OAg",
                "CAADAgADzwEAAhZCawpc3d8UgDDcaQI",
                "CAADAgAD9AIAAvPjvgtVDXi3hHimOQI", 
                "CAADAgADiQEAAiteUwt812TG6sLw9AI"               
         ]


#Menu Btn

start_menu = ReplyKeyboardMarkup(
      [
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "ⱤⱧɎ₮Ⱨ₥ Ø₣ ⱧØ₲₩₳Ɽ₮₴™ Admins 👮‍♂️"],
            ["📊 Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

next_1 = ReplyKeyboardMarkup(
      [
            ["📊 Statistics"],
            ["BACK 🔙"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )

back = ReplyKeyboardMarkup(
      [
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "👮‍♂️ ⱤⱧɎ₮Ⱨ₥ Ø₣ ⱧØ₲₩₳Ɽ₮₴™ Admins 👮‍♂️"],
            ["📊 Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )     





print("Config Working....")
