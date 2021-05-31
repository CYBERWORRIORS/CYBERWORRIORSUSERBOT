import asyncio
from collections import deque

from userbot import *
from CYBERWORRIORSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern=f"bigoof$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 7)
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])

@bot.on(admin_cmd(pattern=f"g1$", outgoing=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await event.edit(pay)

@bot.on(admin_cmd(pattern=f"uff$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "U",
        "Uf",
        "Uff",
        "Ufffff",
        "Uffffff",
        "Ufffffff",
        "Uffffffff",
        "Ufffffffff",
        "Uffffffffff",
        "Ufffffffffff",
        "Uffffffffffff",
        "Ufffffffffffff",
        "Uffffffffffffff",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])

@bot.on(admin_cmd(pattern=f"ctext$", outgoing=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 8,
        paytext * 8,
    )
    await event.edit(pay)

@bot.on(admin_cmd(pattern=f"ftext$", outgoing=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await event.edit(pay)


@bot.on(admin_cmd(pattern=f"kf$", outgoing=True))
async def _(event):
    r = random.randint(0, 3)
    logger.debug(r)
    if r == 0:
        await event.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    else:
        r == 1
        await event.edit("╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")

@bot.on(admin_cmd(pattern=f"f$", outgoing=True))
async def payf(e):
    paytext = e.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 5,
        paytext * 1,
        paytext * 1,
        paytext * 4,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )



CmdHelp("animations6").add_command(
  'bigoof', None, '🇮🇳🇮🇳🇮🇳'
).add_command(
  'g1', None, 'Use and see'
).add_command(
  'uff', None, 'Use and see'
).add_command(
  'ctext', None, 'Use and see'
).add_command(
  'ftext', None, 'Use and see'
).add_command(
  'kf', None, 'Use and see'
).add_command(
  'f', None, 'Use and see'
).add_command(
  'muth', None, 'Use And See'
).add()
