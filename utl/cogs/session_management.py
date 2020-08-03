import discord
from discord.ext import commands

class session_cog(commands.Cog):
    def __init__(self, bot, channel_array):
        self.bot = bot
        self.sessions = channel_array

    # marks the channel as an open session
    @commands.command()
    async def open(self, ctx):
        # shows the channel marked
        channel = ctx.channel
        all_sessions = self.sessions.keys()
        if (channel.id not in all_sessions):
            self.sessions[channel.id] = [[],[]]
            await ctx.send(f'Session has been opened in {channel}.')
        else:
            await ctx.send(f'Session is already open in {channel}.')
        print (self.sessions)
        print()

    # unmarks channel as open session
    @commands.command()
    async def close(self, ctx):
        channel = ctx.channel
        try:
            # pauses session and checks for title
            # records information from session

            # removes from sessions list
            del self.sessions[channel.id]
            await ctx.send(f'Session has been closed in {channel}.')
        except KeyError:
            await ctx.send(f'Session is already closed in {channel}.')
        print (self.sessions)
        print ()
