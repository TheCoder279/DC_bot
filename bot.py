import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Casual players")
    await member.add_roles(role)

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
