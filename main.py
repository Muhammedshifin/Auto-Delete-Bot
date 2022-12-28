import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get('SESSION', "BQCCe-vrxvCiBFOha-4DORMk7SmBtXMoQtgNrgEFBkaBUTyBy2ww2klIFJ0TZKlf1_JsGKUFEZ8f_K09bnr2iEinrbmpU9QDocBoliOiuONwjKhxA6D65Ij5mKpvrg3X0FP7dGD57weycLt5xqfCIjqy3Ns86dSFLZvfZGZceNrKhHdnrcM5s2QBY73mwCkWYW0K787UaEUoD7OoY5GXGmRVlT_zYVxE7Sbo144egOKpkW1rUHLh3RgAhVvoP2lGzY6VEvdGfXfV3-CQ6ybTJMCV_62Ief28LctRMktvpZdWDN5vRSgPPWFNhDHBbCm7voF2yokTVfR2V3LulKEXfsV6AAAAAWGbn2gA")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a private bot of @mh_world to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
