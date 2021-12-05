# PLUGIN MADE BY @mafiarishabh FOR THANOSBOT 
# KEEP CREDITS ELSE GAY
import asyncio

from userbot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

@borg.on(admin_cmd(pattern="aok ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            """💙💙💙💙💙💙
     💙💙💙💙💙💙💙
   💙💙                     💙💙
 💙💙                         💙💙
💙💙                           💙💙
💙💙                           💙💙
 💙💙                         💙💙
   💙💙                     💙💙
      💙💙💙💙💙💙💙
            💙💙💙💙💙/n



💙💙               💙💙
💙💙            💙💙
💙💙        💙💙
💙💙💙💙💙
💙💙💙💙
💙💙💙💙💙
💙💙       💙💙
💙💙           💙 💙
💙💙               💙💙
💙💙                    💙💙/n """
        )


CmdHelp("aok").add_command(
  "aok", None, "ok"
).add_command(
 "ilu", None, "tag your gf"
).add()
