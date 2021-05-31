from userbot import *
from CYBERWORRIORSBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "CYBER"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

aura = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={aura})"


PM_IMG = "https://telegra.ph/file/6749af524b4658e5c2b23.jpg"
pm_caption ="**CYBERWORRIORSBOT Is Online**\n\n"

pm_caption += f"**┏━━━━━━━━━━━━━┓**\n"
pm_caption += f"**┣★ Master : {mention}**\n"
pm_caption += f"**┣★ Telethon : `{version.__version__}`**\n"
pm_caption += f"**┣★ CYBERWORRIORSBOT : {CYBERversion}**\n"
pm_caption += f"**┣★ Sudo       : `{sudou}`**\n"
pm_caption += f"**┣★ Owner   : [CYBER](https://t.me/@The_Pro_Hacker)**\n"
pm_caption += f"**┣★ Creater    : [CYBER](https://t.me/@The_Pro_Hacker)**\n"
pm_caption += f"**┗━━━━━━━━━━━━━┛**\n"

pm_caption += "    [✨REPO✨](https://github.com/CYBERWORRIORS/CYBERWORRIORSBOT) 🔹 [📜License📜](https://github.com/CYBERWORRIORS/CYBERWORRIORSBOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'CYBER', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Are u alive?'
).add()
