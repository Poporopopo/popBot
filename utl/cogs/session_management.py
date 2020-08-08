import discord
from asyncio import TimeoutError
from utl.classes import session_manager
from utl.classes.session import Cast_Error
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

    # adds character to current cast
    @commands.command()
    async def join(self, ctx, *args):
        # quits if no session is opened
        try:
            to_join = self.session_manager.get_session(ctx.channel.id)
        except session_manager.Session_Error:
            await ctx.send(
                f'Session is not open in {ctx.channel}.'
            )
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

    # @commands.command()
    # async def leave(self, ctx, *args):
    #     # quits if no session is opened
    #     if self.is_session_not_open(ctx.channel.id):
    #         await ctx.send(
    #             f'Session is not open in {ctx.channel}.'
    #         )
    #         return
    #     if len(args) > 0 and args[0] == 'bot':
    #         # instructions to remove a tupper
    #         await ctx.send(
    #             'Now waiting for Tupper. '
    #             'Send \'leave\' from your Tupper in the next 30 seconds '
    #             'to leave to cast.'
    #         )
    #
    #         # waits for join message from a tupper bot
    #         def is_bot(message):
    #             return message.author.bot and message.content == 'leave'
    #         try:
    #             message = await self.bot.wait_for('message', check=is_bot, timeout=30.0)
    #         except asyncio.TimeoutError:
    #             await ctx.send(
    #                 f'Tupperbot not found in {ctx.channel}.'
    #             )
    #         else:
    #             if self.is_in_cast(message.author.display_name, ctx.channel.id):
    #                 # removes from cast array in session
    #                 self.sessions[ctx.channel.id][0].remove(message.author.display_name)
    #                 await ctx.send(
    #                     f'{message.author.display_name} '
    #                     f'has been removed from the session in {ctx.channel}.'
    #                 )
    #             else:
    #                 await ctx.send(
    #                     f'{message.author.display_name} '
    #                     f'was not in the session in {ctx.channel}.'
    #                 )
    #         return
    #     # remove message sender from cast of session
    #     if self.is_in_cast(ctx.author.display_name, ctx.channel.id):
    #         self.sessions[ctx.channel.id][0].remove(ctx.author.display_name)
    #         await ctx.send(
    #             f'{ctx.author.display_name} '
    #             f'has been removed from the session in {ctx.channel}.'
    #         )
    #     else:
    #         self.sessions[ctx.channel.id][0].append(ctx.author.display_name)
    #         await ctx.send(
    #             f'{ctx.author.display_name} '
    #             f'was not in the session in {ctx.channel}.'
    #         )
    #     print (self.sessions)
