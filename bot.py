import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Casual players")
    await member.add_roles(role)

bot.run("MTA5ODkyNTM3MjQyODUzNzk4Mw.GUabNg.cXopdaQXad4H46zZpEM6v8OWAKF5-r0HINDF9w")
