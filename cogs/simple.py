import discord
from discord.ext import commands


class Simple(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member: object = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.mention}'.format(member))
        else:
            await ctx.send('Hello {0.mention}... This feels familiar.'.format(member))
        self._last_member = member


def setup(bot):
    bot.add_cog(Simple(bot))
