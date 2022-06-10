import discord
from discord.ext import commands
from discord import app_commands
import json
import datetime
from datetime import datetime
from datetime import date
import asyncio
from random import choice
import os
from os import listdir, system

with open('config.json') as cjson:
    config = json.load(cjson)

intents = discord.Intents.all()

token = config["token"]["bot_token"]

bot = commands.Bot(command_prefix="*", intents=intents, help_command=None)

@bot.listen("on_ready")
async def started():
    print("System Online")
    await load_extensions()


async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
        else:
            print(f'Unable to load {filename[:-3]}')


@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} has been loaded")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} has been unloaded")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f"Extension {extension} has been reloaded")


@bot.listen("on_command_error")
async def on_command_error(ctx, error):
        await ctx.send(error)
        print(f"A error has occured '{error}'")

@bot.command()
async def help(ctx):
            embed = discord.Embed(
                title="PBPD | Keeper SY Help Menu",
                description="This command contains all necessary information on all commands offered by PBPD | Keeper SY"
            )
            embed.set_footer(text="Help Section 1 ---- Keeper SY | PBPD High Command")
            await ctx.author.send(embed=embed)

keywords = ['about our crazy high command']
@bot.listen("on_message")
async def lol(message):
            for i in keywords:
                if i in message.content.lower():
                    await message.channel.send("Wow you some how found this")

bot.run(token)