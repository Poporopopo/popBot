import discord, pathlib
# bot commands lib
from discord.ext import commands

file_parent_location = str(pathlib.Path(__file__).parent)
client = discord.Client()
bot = commands.Bot(command_prefix='popbot ')

#  callback: happens when an event happens
@bot.event
async def on_ready():
    # prints in terminal that bot is online
    print('We have logged in as {0.user}'.format(client))

# reads messages
@bot.event
async def on_message(message):
    print("The message's content was", message.content)

    # # testing: works for tupper bots
    # print(message.author.name)
    # print (message.author.name == "Poporopopo")
    # if message.author.name == "Poporopopo":
    #     return

    message_context = await bot.get_context(message)
    message_author = message_context.author
    message_author_name = message_author.name
    # message_author_nickname = message_author.nick
    message_author_isBot = message_author.bot
    print (message_context)
    print (message_author)
    print (message_author_name)
    # print (message_author_nickname)
    print (message_author_isBot)
    #ignores bots
    await bot.process_commands(message)

# commands section
@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

# run section; must be at end
bot_token = ""
with open(file_parent_location + "/data/bot_token.txt", "r") as tokenfile:
    bot_token = tokenfile.readline()
bot.run(bot_token)
