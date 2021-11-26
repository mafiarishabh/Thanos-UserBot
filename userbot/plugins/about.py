import asyncio

from Thanosbot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

from . import *

CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG
# animation Idea by @The_LegendBoy (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 12
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/c66fad876cf0926662463.jpg"
file2 = "https://telegra.ph/file/63ccacdfe9e6cf2f31123.jpg"
file3 = "https://telegra.ph/file/05e7453665d6028bfe450.jpg"
file4 = "https://telegra.ph/file/e021b9b5ddb6fdecedc8e.jpg"
file5 = "https://telegra.ph/file/c66fad876cf0926662463.jpg"
""" =======================CONSTANTS====================== """

pm_caption = " __**🔥🔥ＴＨΛＮ♢Ｓ ＩＳ ΛＬＩＶΣ🔥🔥**__\n\n"

pm_caption = f"** {CUSTOM_ALIVE_TEXT}**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{thanos_mention}』«««\n"
pm_caption += f"┣TԋαɳσʂႦσƚ ~ {LEGENDversion}\n"
pm_caption += f"┣Tԋαɳσʂ  ~ [Owner](https://t.me/Mafiarishabh)\n"
pm_caption += f"┣Support ~ [G𝖗ουρ](https://t.me/thanosbot_chats)\n"
pm_caption += f"┣Řepô    ~ [Rєρο](https://github.com/thanosuser/ThanosBot)\n"
pm_caption += f"**╰────────────**\n"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)

    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)

    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("about").add_command("about", None, "BEST alive command").add_warning(
    "Harmless Module✅"
).add_info("Just Like Alive But Changing Alwayd Pic").add_type("Official").add()
