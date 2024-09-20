import json
import openai
from discord.ext import commands

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Set up OpenAI API
openai.api_key = config['openai_api_key']

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # Generate a response using OpenAI's API
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{message.author.name}: {message.content}\nBot:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Send the generated response
        await message.channel.send(response.choices[0].text.strip())

def setup(bot):
    bot.add_cog(Chat(bot))
