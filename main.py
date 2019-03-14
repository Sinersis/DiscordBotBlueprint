import discord
from discord.ext import commands

import logging
import traceback

from os import listdir
from os.path import isfile, join

bot = commands.Bot(command_prefix='$', description='This simple Blueprint')


@bot.event
async def on_ready():
    print('This bot ready to works')
    await load_cogs()


async def load_cogs():
    for extension in [file.replace('.py', '') for file in listdir('cogs') if isfile(join('cogs', file))]:
        try:
            if not '__init__' in extension:
                print('Loading {} ...'.format('cogs.' + extension))
                bot.load_extension('cogs.' + extension)
        except Exception as e:
            print('Failed to load cog {}'.format(extension))
            traceback.print_exc()


def main():
    logging.basicConfig(level=logging.INFO)
    bot.run('NTU1NTQ0NDgwOTUwNzc5OTA1.D2syEQ.DklB5IevnLTznr0HpjPctYPx8UI')


if __name__ == '__main__':
    main()
