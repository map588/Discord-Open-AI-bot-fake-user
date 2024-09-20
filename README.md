# Discord OpenAI Bot

This Discord bot uses OpenAI's API to generate human-like responses in chat conversations.

## Features

- Responds to messages in a human-like manner
- Uses OpenAI's GPT model for generating responses
- Easy to set up and customize

## Installation

1. Clone this repository
2. Install the required packages: `pip install -r requirements.txt`
3. Create a `config.json` file with your Discord bot token and OpenAI API key
4. Run the bot: `python bot.py`

## Configuration

Create a `config.json` file in the root directory with the following structure:

```json
{
  "discord_token": "YOUR_DISCORD_BOT_TOKEN",
  "openai_api_key": "YOUR_OPENAI_API_KEY"
}
