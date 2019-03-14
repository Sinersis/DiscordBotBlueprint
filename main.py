import discord
from discord.ext import commands

import logging
import traceback
import configparser

from os import listdir
from os.path import isfile, join

bot = commands.Bot(command_prefix='$', description='This simple Blueprint')
config = configparser.ConfigParser()
config.read('config.ini')


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
    bot.run(config['DEFAULT']['TOKEN'])


if __name__ == '__main__':
    main()
