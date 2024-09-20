import json
import discord
from discord.ext import commands
from openai import OpenAI

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Set up OpenAI client
client = OpenAI(api_key=config['openai_api_key'])

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Generate a response using OpenAI's API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{message.author.name}: {message.content}"}
        ]
    )

    # Send the generated response
    await message.channel.send(response.choices[0].message.content.strip())

# Run the bot
bot.run(config['discord_token'])
