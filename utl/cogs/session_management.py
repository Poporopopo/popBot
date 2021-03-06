import discord
from asyncio import TimeoutError
from utl.classes import session_manager
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

    # takes two channel ids and creates a section between them, inclusive
    @commands.command()
    async def section(self, ctx, *args):
        if not await self.check_is_open(ctx):
            return
        if len(args) == 2:
            try:
                start_message = await ctx.fetch_message(int(args[0]))
                end_message = await ctx.fetch_message(int(args[1]))
                self.session_manager.session_create_section(ctx.channel.id, start_message, end_message)
            except discord.HTTPException as error:
                print (error)
        else:
            await ctx.send(
                "Provide the message ID for the first message and the last message."
            )
        print ("Sessions:",
            self.session_manager)

    async def bot_catcher(self, ctx, message, keyword):
        await ctx.send(
            message
        )
        # waits for join message from a tupper bot
        def is_bot(message):
            return message.author.bot and message.content == keyword
        try:
            bot_message = await self.bot.wait_for('message', check=is_bot, timeout=30.0)
        except TimeoutError as error:
            raise error
        else:
            return bot_message

    # adds all users mentioned to the cast of the current session
    @commands.command()
    async def join(self, ctx):
        if not await self.check_is_open(ctx):
            return
        mentions =  ctx.message.mentions
        if len(mentions) < 1:
            await ctx.send("Mention users to add")
            return
        else:
            print (mentions)
            display_names = []
            # for name in mentions:
            #     display_name.append(name.display_name)
            print (display_names)
        print ("Sessions:",
            self.session_manager)


    @commands.command()
    async def joinbot(self, ctx, *args):
        # TODO: bot joining system
        # pushes a message with instructions
        # waits a set amount of time or until a close command is issued
        # fetches messages from this send message to the close command
        # searches messages for a bot display_name and adds that to cast
        return


    # adds character to current cast
    async def old_join(self, ctx, *args):
        # quits if no session is opened or if is recording
        if (not await self.check_is_open(ctx) or not self.check_is_paused(ctx.channel.id)):
            return
        if len(args) > 0 and args[0] == 'bot':
            # instructions to add a tupper
            bot_join_instructions = (
                'Now waiting for Tupper. '
                'Send \'join\' from your Tupper in the next 30 seconds '
                'to add it to cast.'
            )
            # waits for message from bot
            try:
                bot_message = await self.bot_catcher(ctx, bot_join_instructions, 'join')
            except TimeoutError:
                # sends message when no bot is found
                await ctx.send(
                    f'Tupperbot not found in {ctx.channel}.'
                )
            else:
                # otherwise tries to add
                await self.join_handling(ctx, bot_message.author.display_name)
        else:
            await self.join_handling(ctx, ctx.author.display_name)
        print ("Sessions:",
            self.session_manager)

    async def join_handling(self, ctx, name):
        try:
            self.session_manager.add_member(ctx.channel.id, name)
        except Cast_Error:
             await ctx.send(
                f'{name} '
                f'is already in the session in {ctx.channel}.'
            )
        else:
            await ctx.send(
                f'{name} '
                f'has been added to the session in {ctx.channel}.'
            )

    @commands.command()
    async def leave(self, ctx, *args):
        # quits if no session is opened
        if (not await self.check_is_open(ctx) or not self.check_is_paused(ctx.channel.id)):
            return
        if len(args) > 0 and args[0] == 'bot':
            # instructions to remove a tupper
            bot_leave_instructions = (
                'Now waiting for Tupper. '
                'Send \'leave\' from your Tupper in the next 30 seconds '
                'to leave to cast.'
            )
            # waits for join message from a tupper bot
            try:
                bot_message = await self.bot_catcher(ctx, bot_leave_instructions, 'leave')
            except asyncio.TimeoutError:
                # sends message when no bot is found
                await ctx.send(
                    f'Tupperbot not found in {ctx.channel}.'
                )
            else:
                # otherwise tries to remove
                await self.leave_handling(ctx, bot_message.author.display_name)
        # remove message sender from cast of session
        else:
            await self.leave_handling(ctx, ctx.author.display_name)
        print ("Sessions:",
            self.session_manager)

    async def leave_handling(self, ctx, name):
        try:
            self.session_manager.remove_member(ctx.channel.id, name)
        except Cast_Error:
             await ctx.send(
                f'{name} '
                f'is not in the session in {ctx.channel}.'
            )
        else:
            await ctx.send(
                f'{name} '
                f'has been remove from the session in {ctx.channel}.'
            )

    @commands.command()
    async def start(self, ctx):
        # quits if channel isn't open or is recording
        if (not await self.check_is_open(ctx) or not self.check_is_paused(ctx.channel.id)):
            return
        # checks if the command is issued by a member of the cast
        if not self.session_manager.is_name_in_session(ctx.channel.id, ctx.author.display_name):
            await ctx.send(
                f'{ctx.author.display_name} '
                f'is not part of session in {ctx.channel}.'
            )
        # starts section
        else:
            try:
                self.session_manager.start_in_session(ctx.channel.id, ctx.message.created_at)
            except Pause_Error as error:
                await ctx.send(
                    f'Already recording session in {ctx.channel}.'
                )
            else:
                await ctx.send(
                    f'Now recording session in {ctx.channel}.'
                )
        print ("Sessions:",
            self.session_manager)

    @commands.command()
    async def stop(self, ctx):
        # quits if channel isn't open
        if not await self.check_is_open(ctx):
            return
        # checks if the command is issued by a member of the cast
        if not self.session_manager.is_name_in_session(ctx.channel.id, ctx.author.display_name):
            await ctx.send(
                f'{ctx.author.display_name} '
                f'is not part of session in {ctx.channel}.'
            )
        # closes section
        else:
            try:
                self.session_manager.close_in_session(ctx.channel.id, ctx.message.created_at)
            except Pause_Error as error:
                await ctx.send(
                    f'Session in {ctx.channel} is not being recorded.'
                )
            else:
                await ctx.send(
                    f'Session in {ctx.channel} no longer being recorded.'
                )
        print ("Sessions:",
            self.session_manager)
