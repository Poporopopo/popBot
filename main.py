import discord, pathlib
# bot commands lib
from discord.ext import commands

# bot token finder
file_parent_location = str(pathlib.Path(__file__).parent)
bot_token = ""
with open(file_parent_location + "/data/bot_token.txt", "r") as token_file:
    bot_token = token_file.readline()

client = discord.Client()
bot = commands.Bot(command_prefix='popbot ')

#  callback: happens when an event happens
@bot.event
async def on_ready():
    # prints in terminal that bot is online
    print('We have logged in as {0.user}'.format(bot))

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

    # context is immutable
    # try:
    #      message_author.bot = False
    # except Exception as error:
    #     print (error)

    message_author_isBot = message_author.bot
    print (message_context)
    print (message_author)
    print (message_author_name)
    # print (message_author_nickname)
    print (message_author_isBot)
    print()
    #ignores bots
    await bot.process_commands(message)

# commands section
# example command
@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def test(ctx):
    channel = ctx.channel
    async for message in channel.history():
        print (message.author)
        print ()

# tracks sessions based on channels
sessions = []

# marks the channel as an open session
@bot.command()
async def open(ctx):
    # shows the channel marked
    channel_name = ctx.channel
    print (channel_name)
    sessions.append(channel_name)
    print (sessions)
    await ctx.send(f'Session has been opened in {channel_name}')



# run section; must be at end
bot.run(bot_token)
