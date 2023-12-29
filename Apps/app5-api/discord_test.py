import discord
from discord.ext import commands

# Configura il bot
bot = commands.Bot(command_prefix="!")

# Evento quando il bot è pronto
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Comando di esempio
@bot.command(name='saluta', help='Saluta il bot')
async def salute(ctx):
    await ctx.send(f'Ciao {ctx.author.name}!')


TOKEN = 'MTE5MDM4MDM4MjcyMjQ1NzcyMQ.GjWIeO.J-l5xfXJB1ILrMC7YrdqW8NK4Dq9IOFcNPwiZQ'

# Avvia il bot
bot.run(TOKEN)