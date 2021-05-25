import random

import discord
from discord.ext import commands
import asyncio

from datetime import datetime
from pytz import timezone

bot = commands.Bot(command_prefix=".", self_bot=True)

# ~~~ EDIT THIS ~~~
awake_statuses = {
    0: ["STATUS_1", "EMOJI_1"],
    1: ["STATUS_2", "EMOJI_2"],
    2: ["STATUS_3", "EMOJI_3"],
}

# ~~~ EDIT THIS ~~~
sleeping_statuses = {
    0: ["STATUS_1", "EMOJI_1"],
    1: ["STATUS_2", "EMOJI_2"],
    2: ["STATUS_3", "EMOJI_3"],
}

# ~~~ EDIT THIS ~~~
list_of_time_sleep = []


async def set_status(name, status_discord, emoji):
    await bot.change_presence(
        activity=discord.CustomActivity(name=name, state=name, emoji=emoji), status=discord.Status[status_discord])


@bot.event
async def on_ready():
    while True:
        # ~~~ EDIT THIS ~~~
        tz = timezone('TIMEZONE')
        datetime.now(tz)
        time = int(datetime.now(tz).strftime('%H'))
        if time in list_of_time_sleep:
            array_of_info = sleeping_statuses[random.randint(0, len(list(sleeping_statuses.keys())) - 1)]
            await set_status(array_of_info[0], "idle", array_of_info[1])
        else:
            array_of_info = awake_statuses[random.randint(0, len(list(awake_statuses.keys())) - 1)]
            await set_status(array_of_info[0], "dnd", array_of_info[1])
        await asyncio.sleep(15)


# ~~~ EDIT THIS ~~~
bot.run("YOUR_TOKEN", bot=False)