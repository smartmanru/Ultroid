# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}wg `
• `{i}bash -c <cmds>` Carbon image as command output.
    Run linux commands on telegram.
"""
from . import *

_ignore_eval = []


@ultroid_cmd(
    pattern="wg( (.*)|$)",
)
async def _(event):
    match = str(event.pattern_match.group(1).strip())
    if match:
        try:
            config = "_"+match
        except Exception as er:
            return await event.eor(str(er))
    else:
        config=""
    if event.is_reply:
        rpl = await event.get_reply_message()
        user = str(rpl.sender_id)
    else:
        user = str(event.chat_id)
    xx = await event.eor(get_string("com_1"))

    output, error = await bash(
        "ssh shtxt.info '/root/wg/wireguard-install.sh " + user + "" + config + "'"
    )
    if error and error.endswith("NOT_FOUND"):
        return await xx.edit(f"Error: `{error}`")
    file = "/root/wg/" + user + "" + config + "-wg1.conf"
    try:
        await event.client.send_file(event.chat_id, file, thumb=None)
    except Exception as er:
        return await event.eor(str(er))

    await xx.delete()
