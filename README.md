<h1>Discord OpenAI Bot</h1>

This Discord bot uses OpenAI's API to generate human-like responses in chat conversations.

<h2>Features</h2>

- Responds to messages in a human-like manner
- Uses OpenAI's GPT model for generating responses
- Easy to set up and customize
- reset the bots memory with the discord command !reset

<h2>Discord Bot Setup</h2>

Before installing and running the bot, you need to create a Discord application and bot user:

1. Go to the Discord Developer Portal (https://discord.com/developers/applications).
2. Click on "New Application" and give your application a name.
3. Go to the "Bot" tab in the left sidebar and click "Add Bot".
4. Customize your bot's name and avatar as desired.
5. Under the "Token" section, click "Copy" to copy your bot token. You'll need this for the config.json file.
6. In the "Privileged Gateway Intents" section, enable "Message Content Intent".
7. Go to the "OAuth2" tab in the left sidebar, then select "URL Generator".
8. In the "Scopes" section, select "bot".
9. In the "Bot Permissions" section, select the permissions your bot needs (at minimum: "Read Messages/View Channels", "Send Messages", and "Read Message History").
10. Copy the generated URL at the bottom of the page.
11. Open this URL in a new tab and select the server you want to add the bot to. You must have the "Manage Server" permission to add bots to a server.

Now your Discord bot is set up and added to your server(s).

<h2>Installation</h2>

<h3>Local Installation</h3>

1. Clone this repository:

```
git clone https://github.com/Fruchtii/Discord-Open-AI-bot-fake-user.git
```

2. Navigate to the project directory:

```
cd Discord-Open-AI-bot-fake-user
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Create a config.json file with your Discord bot token and OpenAI API key (see Configuration section)

5. Run the bot:

```
python bot.py
```

<h2>Configuration</h2>

Create a config.json file in the root directory with the following structure:

```
{
  "discord_token": "YOUR_DISCORD_BOT_TOKEN",
  "openai_api_key": "YOUR_OPENAI_API_KEY"
}
```

Replace YOUR_DISCORD_BOT_TOKEN with the token you copied in step 5 of the Discord Bot Setup.
Replace YOUR_OPENAI_API_KEY with your OpenAI API key. If you don't have one, sign up at OpenAI (https://beta.openai.com/signup/) and create an API key.

<h2>Usage</h2>

The bot will respond to messages in channels it has access to. It uses OpenAI's API to generate human-like responses based on the conversation context.

<h2>Deployment on DigitalOcean</h2>

To deploy this bot on DigitalOcean, you can either use SSH or the DigitalOcean console on the website:

1. Create a DigitalOcean account if you don't have one.

2. Create a new Droplet:
   - Choose an image: Ubuntu 20.04 (LTS) x64
   - Choose a plan: Basic (cheapest option should be sufficient)
   - Choose a datacenter region close to your target audience
   - Add your SSH key or create a new one

3. Once your Droplet is created, you can either use SSH or the DigitalOcean console:
   - To use SSH:

```
ssh root@your_droplet_ip
```

   - To use the DigitalOcean console:
     - Go to your Droplet's page on DigitalOcean
     - Click on "Access" in the left sidebar
     - Click on "Launch Droplet Console" to open a web-based console

4. In the terminal or console, update the system and install required packages:

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

5. Clone the repository:

```
git clone https://github.com/Fruchtii/Discord-Open-AI-bot-fake-user.git
cd Discord-Open-AI-bot-fake-user
```

6. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate
```

7. Install the required packages:

```
pip install -r requirements.txt
```

8. Create the config.json file and add your Discord token and OpenAI API key:

```
nano config.json
```

   Paste your configuration and save the file (Ctrl+X, then Y, then Enter).

9. Install screen to run the bot in the background:

```
sudo apt install screen -y
```

10. Start a new screen session and run the bot:

```
screen -S discord-bot
python bot.py
```

11. Detach from the screen session by pressing Ctrl+A, then D.

Your bot should now be running on the DigitalOcean Droplet. To reattach to the screen session later, use:

```
screen -r discord-bot
```

To keep your bot running after you close the console, make sure to detach from the screen session instead of closing it.

Note: When using the DigitalOcean console, you may experience occasional disconnects. If this happens, simply reconnect and reattach to the screen session to check on your bot.

<h2>Contributing</h2>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

<h2>License</h2>

MIT (https://choosealicense.com/licenses/mit/)
