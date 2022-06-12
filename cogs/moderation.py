from code import interact
from logging.handlers import MemoryHandler
from multiprocessing.sharedctypes import Value
from tkinter import Y
from turtle import color
from unicodedata import name
import discord
from discord import app_commands
from numpy import tile
import typedef as typedef
from discord.ext import commands, menus, tasks
from discord.voice_client import VoiceClient
from discord import Embed, Member, Role
import json
import datetime
from datetime import datetime
from datetime import date
from discord.ui import Select, View
import asyncio
from random import choice
import os
from os import listdir, system



class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        bannedwords = ['nigger', 'faggot', 'niggers', 'faggots']

        @commands.Cog.listener()
        async def on_ready():
            print("Moderation Has Been Loaded")


        @commands.Cog.listener()
        async def on_message(message):
            author = message.author
            if (message.author.bot):
                log = open(".log/ignorelog", "a")
                log.write(f".")
                log.close()
            else:
                # DISCORD LOGGER & BAN SYSTEM
                for i in bannedwords:
                    if i in message.content.lower():
                        channel = self.bot.get_channel(977068776086437938)

                        await message.delete()
                        embed = discord.Embed(
                            color=discord.Color.red(),
                        )
                        embed.set_author(name="Keeper Auto Moderation System")
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/971537791001440286/971609509980155925/Keeper_WD_Logo.jpg")
                        embed.add_field(name=f"Blacklisted Word Detected:", value=f"Message: {message.content}")
                        embed.add_field(name=f"Message Author:", value=f"{message.author}")
                        embed.add_field(name="Punishment:", value="Blacklisted Word In CaliRP System set to Ban")
                        embed.set_footer(
                            text='Keeper System, If you feel this punishment is not deserved please contact High Command of PBPD')
                        await message.author.send(embed=embed)
                        await channel.send(embed=embed)

                        await message.author.ban(reason="Blacklisted Word")

                        # Start Hard Logger
                        log = open("log/banlogs", "a")
                        log.write(f'====================================================')
                        log.write("\n")
                        log.write(f'Keeper Auto Moderation System Hard Logs')
                        log.write("\n")
                        log.write(f'Person Banned: {message.author}, ID: {message.author.id}')
                        log.write("\n")
                        log.write(f'Reason Banned: Blacklisted Word, Message Content: "{message.content}"')
                        log.write("\n")
                        log.write(f'Time for Ban: Perm')
                        log.write("\n")
                        log.write("====================================================")
                        log.close()
                        # Console Logger
                        print(f'=========Keeper Auto Moderation System=====================')
                        print(f'Person Banned: {message.author}, ID: {message.author.id}')
                        print(f'Reason Banned: Blacklisted Word, Message Content: "{message.content}"')
                        print(f'Time Banned For: Perm')
                        print(f'============================================================')
