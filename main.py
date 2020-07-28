import discord

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

    #experimental alt key
    if message.content.startswith('popbot'):
        await message.channel.send('pop hello')

bot_token = ""
client.run(bot_token)
