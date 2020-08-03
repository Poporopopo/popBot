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
        # quits if session is moving
        if (self.in_session(channel.id, self.sessions)):
            return
        all_sessions = self.sessions.keys()
        if (channel.id not in all_sessions):
            self.sessions[channel.id] = [[],[]]
            await ctx.send(f'Session has been opened in {channel}.')
        else:
            await ctx.send(f'Session is already open in {channel}.')
        print ("Sessions:",
            self.sessions)

    # unmarks channel as open session
    @commands.command()
    async def close(self, ctx):
        channel = ctx.channel
        # quits if session is moving
        if (self.in_session(channel.id, self.sessions)):
            return
        try:
            # pauses session and checks for title
            # records information from session

            # removes from sessions list
            del self.sessions[channel.id]
            await ctx.send(f'Session has been closed in {channel}.')
        except KeyError:
            await ctx.send(f'Session is already closed in {channel}.')
        print ("Sessions:",
            self.sessions)

    # determines if a session is being recorded
    # returns boolean
    def in_session(self, channel_id, sessions_dict):
        # check if sessions_dict is empty
        if len(sessions_dict) < 1:
            return False
        # check if there was a pause command issued
        session_sections = sessions_dict[channel_id][1]
        if len(session_sections) < 1:
            return False
        return len(session_sections[-1][1]) == 1
