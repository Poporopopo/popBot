import discord
from asyncio import TimeoutError
from utl.classes import session_manager
from utl.classes.session import Cast_Error, Pause_Error
from discord.ext import commands

class session_cog(commands.Cog):
    def __init__(self, bot, manager):
        self.bot = bot
        self.session_manager = manager

    # marks the channel as an open session
    @commands.command()
    async def open(self, ctx):
        # adds room to session if not open
        try:
            self.session_manager.open_session(ctx.channel.id)
        except session_manager.Session_Error:
            await ctx.send(f'Session is already open in {ctx.channel}.')
        else:
            await ctx.send(f'Session has been opened in {ctx.channel}.')
        print ("Sessions:",
            self.session_manager
            )

    # unmarks channel as open session
    @commands.command()
    async def close(self, ctx):
        # quits if session is recording
        try:
            self.session_manager.close_session(ctx.channel.id)
        except session_manager.Session_Error:
            await ctx.send(f'Session is not open in {ctx.channel}.')
        else:
            await ctx.send(f'Session has been closed in {ctx.channel}.')
        print ("Sessions:",
            self.session_manager)

    # method for repeated check for open sessions
    async def check_is_open(self, ctx):
        output = self.session_manager.is_session_open(ctx.channel.id)
        if not output:
            await ctx.send(
                f'Session is not open in {ctx.channel}.'
            )
        return output

    
