import discord, pathlib
# bot commands lib
from discord.ext import commands
from utl.cogs.session_management import session_cog

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
    if message.author == bot.user:
        return

    print("The message's content was:")
    print(message.content)

    # # testing: works for tupper bots
    # print(message.author.name)
    # print (message.author.name == "Poporopopo")
    # if message.author.name == "Poporopopo":
    #     return

    # message_context = await bot.get_context(message)
    # message_author = message_context.author
    # message_author_name = message_author.name
    # # message_author_nickname = message_author.nick
    #
    # # context is immutable
    # # try:
    # #      message_author.bot = False
    # # except Exception as error:
    # #     print (error)
    #
    # message_author_isBot = message_author.bot
    # print (message_context)
    # print (message_author)
    # print (message_author_name)
    # # print (message_author_nickname)
    # print (message_author_isBot)
    # print()

    # #ignores bots
    await bot.process_commands(message)
    print ()

# commands section


# tracks sessions based on channels
sessions = {}

# cogs
bot.add_cog(session_cog(bot, sessions))

# run section; must be at end
bot.run(bot_token)
