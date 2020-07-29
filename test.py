import discord, pathlib
from discord.ext import commands

file_parent_location = str(pathlib.Path(__file__).parent)
prefix = "$"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Everything's all ready to go~")


@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''
    print('testing')
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

bot_token = ""
with open(file_parent_location + "/data/bot_token.txt", "r") as tokenfile:
    bot_token = tokenfile.readline()
bot.run(bot_token)
