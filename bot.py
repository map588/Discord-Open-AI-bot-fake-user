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

# Dictionary to store conversation history for each channel
conversation_history = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Process commands
    await bot.process_commands(message)

    # If it's a command, don't process it as a regular message
    if message.content.startswith(bot.command_prefix):
        return

    # Initialize conversation history for the channel if it doesn't exist
    if message.channel.id not in conversation_history:
        conversation_history[message.channel.id] = []

    # Add the user's message to the conversation history
    conversation_history[message.channel.id].append({"role": "user", "content": f"{message.author.name}: {message.content}"})

    # Prepare the messages for the API call
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ] + conversation_history[message.channel.id][-10:]  # Include up to the last 10 messages

    # Generate a response using OpenAI's API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Get the assistant's reply
    assistant_reply = response.choices[0].message.content.strip()

    # Add the assistant's reply to the conversation history
    conversation_history[message.channel.id].append({"role": "assistant", "content": assistant_reply})

    # Send the generated response
    await message.channel.send(assistant_reply)

@bot.command(name='reset')
async def reset_memory(ctx):
    """Reset the bot's memory for the current channel."""
    channel_id = ctx.channel.id
    if channel_id in conversation_history:
        conversation_history[channel_id] = []
        await ctx.send("Memory has been reset for this channel.")
    else:
        await ctx.send("There was no conversation history to reset in this channel.")

# Run the bot
bot.run(config['discord_token'])
