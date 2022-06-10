import discord
from discord.ext import commands


class remove(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


        @commands.Cog.listener()
        async def on_ready():
            print("remove has been loaded")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        remove(bot)
    )