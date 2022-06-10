import discord
from discord.ext import commands
from discord import Embed, Member, Role

class add(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready():
        print("add.py Loaded Avalible commands from this cog is addrole")

    @commands.command()
    @commands.has_any_role("PBPD | Field Training Division", "K9 | Command", "ARU | Command", "GSU | Command")
    async def addrole(self, ctx, role: Role = None, member: discord.Member=None):
        
        if role is None:
            return await ctx.reply('No Role Selected!')
        if member is None:
            member = ctx.author
        if role > ctx.author.top_role:
            await ctx.send(f"Sorry " + (str(role)) + ' is higher than your Top Role: ' + (str(ctx.author.top_role))+ f". Do to my restrictions i can not add this role")
        else:
            try:
                print("Access Granted to ", ctx.author.name, " ", ctx.author.id)

                await member.add_roles(role)

                print("Role Given" + (str(role)))

                await ctx.reply(str(role)+' has been added to '+ (str(member)))

        #Start Logging System

                channel = self.bot.get_channel(977372887449239552)

                msg = ctx.message
                await msg.add_reaction("✔️")
                author = ctx.author.name
                embed = discord.Embed(
                    color = discord.Color.blue()
                    )
                embed.set_author(name="[--Paleto Bay Police Department Add/Remove Logs--]")
                embed.add_field(name="add Log", value="Accsess Granted to" + (str(author)))
                embed.add_field(name="Person Having the role added", value=(member))
                embed.add_field(name="Roles added", value=(role))
                await channel.send(embed=embed)
            except Exception as e:
                return await ctx.reply(f'error has occured: {e}')

        
        



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        add(bot)
    )