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


class security(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    
    # Moderate
    @commands.command()
    async def moderate(self, ctx, user):
        if user is None:
            user = ctx.author
            

        if discord.utils.get(ctx.author.roles, name="PBPD | Moderation Panel") is not None:
            await ctx.message.delete()
            select = Select(
                placeholder="Select a Option",
                options=[
                    discord.SelectOption(label="Ban", emoji="🔨", description="Moderation Command: Bans the user"),
                    discord.SelectOption(label="Kick", emoji="🔨", description="Moderation Command: Kick the user"),
                    discord.SelectOption(label="Userinfo", emoji="📜", description="Information Commands: Displays Users Information"),
                ]
            )

            async def my_callback(interaction):
                if select.values[0] == "Ban":
                    if user.top_role > ctx.author.top_role:
                        await interaction.response.send_message("You can't ban people higher than you")

                        return
                    else:
                        if ctx.author == user:
                            await interaction.response.send_message("You can't ban your self!")
                        else:
                            await interaction.response.send_message(f"Identity check complete! Banning {user}!")
                            await ctx.author.send(f"{user} has been banned by {ctx.author}, if you feel this is a mistake please contact HC")
                            embed = discord.Embed(
                                color=discord.Color.red()
                            )
                            embed.set_author(name="[--Paleto Bay Moderation System--]")
                            embed.add_field(name=f"You have been Banned from Paleto Bay Police Department by {ctx.author}", value="If you feel this is a mistake please contact HC or make a general support ticket in the main CaliRP Discord!")
                            await ctx.author.send(embed=embed)
                        return

            
                elif select.values[0] == "Kick":
                    if user.top_role > ctx.author.top_role:
                        await interaction.response.send_message("You can't kick people higher than you")
                    else:
                        if user == ctx.author:
                            await interaction.response.send_message("you cant kick your self")

                        else:
                            await interaction.response.send_message(f"Identity check complete! Kicking {user}!")
                            try:

                                await user.kick(reason=f"{user} has been kicked by {ctx.author}, if you feel this is a mistake please contact HC")
                                embed = discord.Embed(
                                    color=discord.Color.red()
                                )
                                embed.set_author(name="[--Paleto Bay Moderation System--]")
                                embed.add_field(name=f"You have been kicked from Paleto Bay Police Department by {ctx.author}", value="If you feel this is a mistake please contact HC or make a general support ticket in the main CaliRP Discord!")
                                await user.send(embed=embed)
                            except Exception as e:
                                return await ctx.author.send(f'Please make a ticket and send this error code\nError: {e}')



                elif select.values[0] == "Userinfo":
                    member = user
                    embed=discord.Embed(
                        title="User Information", 
                        colour=discord.Colour.random()
                        )
                    embed.set_thumbnail(url=member.avatar)
                    embed.add_field(name="Name", value=member.name)
                    embed.add_field(name="Nickname", value=member.nick)
                    embed.add_field(name="ID", value=member.id)
                    embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))
                    embed.add_field(name="Joined",value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))

                    embed.add_field(name="Status", value=member.status)
                    message = await ctx.author.send(embed=embed)
                    await asyncio.sleep(60)
                    await message.delete()
                    


            select.callback = my_callback
            view = View()
            view.add_item(select)

            message2 = await ctx.author.send(f"User Selected {user}, this will delete in 2 Minutes", view=view)
            await asyncio.sleep(120)
            await message2.delete()
        else:
            await ctx.send("You do not have the perms to use this command")

    #lockdown commands
    @commands.command()
    @commands.has_any_role("PBPD | High Command", "PBPD | Low Command")
    async def lockdown(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send( ctx.channel.mention + " ***is now in lockdown.***")

    @commands.command()
    @commands.has_any_role("PBPD | High Command", "PBPD | Low Command")
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + f" ***has been unlocked.*** By {ctx.author}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        security(bot)
    )