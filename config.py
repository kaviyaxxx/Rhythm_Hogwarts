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
WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>Type your query here..\nI'll respond to your query as earliest</code> π\n\nΡΟΟ ΟΞ±ΠΈΠΈΞ± ΡΟ ΠΊΠΈΟΟ Ξ±Π²ΟΟΡ ΠΌΡπ? ΡΡΞ±β Π²ΡβΟΟ\n\nΞ±Π²ΟΟΡ @ImDark_Empire:-\n β’ΠΌΡ ΠΈΞ±ΠΌΡ:- π―πππ π°πππππ \n β’ΠΌΡ Ξ±gΡ:- ΟΠΈΠΊΠΈΟΟΠΈπ\n β’Β’ΟΠΌΟΟΡΡΡ βΞ±ΠΈgΟΞ±gΡ:- [πππ ππππ](https://github.com/DARKEMPIRESL) \nβ’Β’Π½ΡΒ’ΠΊ [About π―πππ π°πππππ](https://t.me/darks_pm_bot) fΟΡ ΠΌΟΡΡ\n\nPlz Don't Send Stickers π₯²\nReason :- [This](https://t.me/ultchat/19589)"
USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
USER_DETAILS = "<b>FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
FORCESUB_TEXT = "**β Access Denied β**\n\β±€β±§Ιβ?β±§β₯ Γβ£ β±§Γβ²β©β³β±€β?β΄β’ eke nathuva Mokatada yako Botva Start Kare kkkππ\nβ»οΈJoin and Try Again.β»οΈ"
HELP_STRING = "If you need to contact admins use this bot...ππ"
START_STRING ="""
Hi {}, Welcome to  πβ€οΈπβ±€β±§Ιβ?β±§β₯ Γβ£ β±§Γβ²β©β³β±€β?β΄β’ππ Official Bot.
 Bot By [π―πππ π°πππππ π±π°πΈ π± π§ π΄ πΉ πΈ β’](https://t.me/ImDark_Empire)
"""


#Inline Btn
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here - πβ€οΈπβ±€β±§Ιβ?β±§β₯ Γβ£ β±§Γβ²β©β³β±€β?β΄β’ππ', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('π Κα΄α΄Κα΄ Κα΄Ι’s π', user_id=f"@SL_BOTS_TM")
                 ],
                 [
                 InlineKeyboardButton(text="β»οΈ Reload β»οΈ",callback_data="ref")
                 ]]
                  )
                  
CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("π?ππππ", callback_data="cloce")
                 ]]
                 )
                                                    
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="π» Κα΄α΄α΄ π»",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('π Owner π', user_id="@Scamander_01")
                 ],
                 [
                 InlineKeyboardButton(text="π΄ Κα΄Κα΄ π΄",callback_data="hlp"),
                 InlineKeyboardButton("π sα΄α΄Κα΄α΄ α΄α΄α΄α΄ π", url="https://github.com/kaviyaxxx/Rhythm_Hogwarts")
                 ],
                 [
                 InlineKeyboardButton("β sΚα΄Κα΄ β", switch_inline_query="share"),
                 InlineKeyboardButton("β sΚα΄Κα΄ α΄ΚΙ΄Κ β", switch_inline_query="cshare")
                 ],
                 [
                 InlineKeyboardButton("Team SL Botsπ±π°", url="https://t.me/SLBotOfficial"),
                 InlineKeyboardButton("Support - https://t.me/SLBotsChat ", url="https://t.me/SLBotsChat")
                 ]                 
                 [
                 InlineKeyboardButton("βπ°π»πΏπ·π° δΉ β’ Bots γπ±π°γ", url="https://t.me/AlphaTm_Botz"),
                 InlineKeyboardButton("Support - βπ°π»πΏπ·π° Botz Chat ", url="https://t.me/AlphaTm_Botz_chat")
                 ]]
                  )

ADMIN_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('ΰΌβββπ€α΅α΅α΅β±ΚΈα΅π€βΰΌ» γ ΘPβ£ΕΔ»β’οΈΒ°γ|γγβππ½ππβ’οΈΒ°γγβπ°π»πΏπ·π° δΉ β’', user_id="Scamander_01")
                 ],
                 [                 
                 InlineKeyboardButton('βππΌπΌβ π»πΌπΌβπ»πΈβπ α΄¬α΄·α΄¬ Morgana', user_id="Lily_MORGANA_DEEPDARK")
                 ],
                 [                 
                 InlineKeyboardButton('βͺοΈ', user_id="The_Girl_Who_Lived_2005")
                 ],
                 [                 
                 InlineKeyboardButton('πββββπEΞ±ΚΤΞ±Ι³?½?½ UΙ±Ξ±α§Ξ±Ι³Ι Ξ±Ι³Ξ±πββββπ', user_id="Eashaaa")
                 ],
                 [                 
                 InlineKeyboardButton('ΰ¦ΰ§«ββ€βππ€ππππ¦ ππππππ€ππππ πΰΌ»ΰΌ ΰΌ»π', user_id="Iron_Voldy")
                 ],
                 [                 
                 InlineKeyboardButton('πββββπ βΙΧΧ κ©ΧΧΙΧΧ πβββ π', user_id="Devil_lover21")
                 ],
                 [
                 InlineKeyboardButton('γπΎπ¬πΉπ―ππΉπ΄γ γ ΘPβ£ΕΔ»β’οΈΒ°γ', user_id="Sas_2002")
                 ],
                 [                 
                 InlineKeyboardButton('κ§β€οΈ α­ Hermione βΏΰΌβ€οΈκ§γγβππ½ππβ’οΈΒ°γγ γ ΘPβ£ΕΔ»β’οΈΒ°γ', user_id="phynix_06")
                 ],
                 [                 
                 InlineKeyboardButton('Β©Kolly_FanSLα΅α΄Ή FiΝ₯lmΝ«sΝZiΝ₯llaΝ£π±π°β’ γγβππ½ππβ’οΈΒ°γγ', user_id="Kolly_FanSL_1301")
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
                 InlineKeyboardButton('ππα­πΌlπΞ½πΕ πΞ½πΦΰΌβΏπγ ΘPβ£ΕΔ»β’οΈΒ°γ|γγβππ½ππβ’οΈΒ°γγ', user_id="Yaoyorozu_2005")
                 ],
                 [                 
                 InlineKeyboardButton('?ββββπ»βοΈπUdan Akalanka ββββπβοΈπ»', user_id="Half_Blood_Prince2006")
                 ],
                 [
                 InlineKeyboardButton('TELEDARK AKA DEEPDARK ', user_id="Tele_DeepDark")
                 ],
                 [                 
                 InlineKeyboardButton('ΰ¦ΰ§«ββ€Sanemi Shinazugawa πΰΌ»ΰΌ ΰΌ»π', user_id="WindHashira_Shinazugawa")
                 ]
                 ]
                  )

OWNER_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('ΰΌβββπ€α΅α΅α΅β±ΚΈα΅π€βΰΌ» γ ΘPβ£ΕΔ»β’οΈΒ°γ|γγβππ½ππβ’οΈΒ°γγβπ°π»πΏπ·π° δΉ β’', user_id="Scamander_01")
                 ]]
                  )               

DEV_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('π―πππ π°πππππ π±π°πΈ π± π§ π΄ πΉ πΈ β’', user_id="SL_BOTS_TM")
                 ],
                 [
                 InlineKeyboardButton('Ε¦Δ§ΘΊΙα΅Ύκ ΙΙnα΅ΎΙΘΊ', user_id="ImTharuk")
                 ],
                 [
                 InlineKeyboardButton('unknown boyβπ°π»πΏπ·π° δΉ β’', user_id="UnknownB_o_y")
                 ],
                 [
                 InlineKeyboardButton('ΰΌβ£οΈβ’οΈβ£IrΓΞ?βmΰΈΕβ β’οΈβ£οΈΰΌ ', user_id="ImGishan")
                 ],
                 [
                 InlineKeyboardButton('πΏππ£πͺπ¬ππ£ π±π°', user_id="ImDenuwan")
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
            ["π€΄ OWNER π€΄"],
            ["π» Bot Devs π»", "β±€β±§Ιβ?β±§β₯ Γβ£ β±§Γβ²β©β³β±€β?β΄β’ Admins π?ββοΈ"],
            ["π Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

next_1 = ReplyKeyboardMarkup(
      [
            ["π Statistics"],
            ["BACK π"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )

back = ReplyKeyboardMarkup(
      [
            ["π€΄ OWNER π€΄"],
            ["π» Bot Devs π»", "π?ββοΈ β±€β±§Ιβ?β±§β₯ Γβ£ β±§Γβ²β©β³β±€β?β΄β’ Admins π?ββοΈ"],
            ["π Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
      )     





print("Config Working....")
