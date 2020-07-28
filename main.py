import discord, pathlib

file_parent_location = str(pathlib.Path(__file__).parent)
client = discord.Client()

#  callback: happens when an event happens
@client.event
async def on_ready():
    # prints in terminal that bot is online
    print('We have logged in as {0.user}'.format(client))

# reads messages
@client.event
async def on_message(message):
    # exits when message is from this bot
    # otherwise (including other bots) will respond
    if message.author == client.user:
        return

    # if the message is from a user and as the key, will respond with Hello
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot_token = ""
with open(file_parent_location + "/data/bot_token.txt", "r") as tokenfile:
    bot_token = tokenfile.readline()
client.run(bot_token)
