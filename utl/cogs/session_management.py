import discord, asyncio
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
        # quits if session is recording
        if self.is_in_session(channel.id):
            return

        if self.is_session_not_open(channel.id):
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
        # quits if session is recording
        if self.is_in_session(channel.id):
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

    # adds character to current cast
    @commands.command()
    async def join(self, ctx, *args):
        # quits if no session is opened
        if self.is_session_not_open(ctx.channel.id):
            await ctx.send(
                f'Session is not open in {ctx.channel}.'
            )
            return
        if len(args) > 0 and args[0] == 'bot':
            # instructions to add a tupper
            await ctx.send(
                'Now waiting for Tupper. '
                'Send \'join\' from your Tupper in the next 30 seconds '
                'to add it to cast.'
            )

            # waits for join message from a tupper bot
            def is_bot(message):
                print (message.author.bot)
                return message.author.bot and message.content == 'join'
            try:
                message = await self.bot.wait_for('message', check=is_bot, timeout=30.0)
            except asyncio.TimeoutError:
                await ctx.send(
                    f'Tupperbot not found in {ctx.channel}.'
                )
            else:
                await ctx.send(
                    f'Tupperbot found in {ctx.channel}.'
                )
            return
        # add message sender to cast of session
        print("Is in cast?: ",
            self.is_in_cast(ctx.author.display_name, ctx.channel.id)
        )
        if self.is_in_cast(ctx.author.display_name, ctx.channel.id):
            await ctx.send(
                f'{ctx.author.display_name}'
                f' is already in the session in {ctx.channel}.'
            )
        else:
            self.sessions[ctx.channel.id][0].append(ctx.author.display_name)
            await ctx.send(
                f'{ctx.author.display_name}'
                f' has been added session in {ctx.channel}.'
            )

    # check if person is in the cast
    # author is string, and channel id is int
    def is_in_cast(self, author, channel_id):
        return author in self.sessions[channel_id][0]

    # check if session is open
    def is_session_not_open(self, channel_id):
        return (channel_id not in self.sessions.keys())

    # determines if a session is being recorded
    # returns boolean
    def is_in_session(self, channel_id):
        # check if sessions_dict is empty
        if len(self.sessions) < 1:
            return False
        # check if there was a pause command issued
        session_sections = self.sessions[channel_id][1]
        if len(session_sections) < 1:
            return False
        return len(session_sections[-1][1]) == 1
