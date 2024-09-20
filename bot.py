import json
import discord
from discord.ext import commands

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
bot.load_extension('cogs.chat')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Run the bot
bot.run(config['discord_token'])
