# Friend Tech Auto Chat

This bot acts as a bridge between Discord and Friend Tech. When a message is sent in a specified Discord channel, the bot captures the content of the message and sends it to a list of Friend Tech rooms decided by the user via WebSockets.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Discord Bot Setup](#discord-bot-setup)
- [Installation](#installation)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Usage](#usage)

## Prerequisites

1. **Python**: This project requires Python 3.11.5 or newer. If you haven't already installed Python, download and install it from [python.org](https://www.python.org/downloads/).

## Discord Bot Setup

1. **Create a New Application**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on the "New Application" button. Name your application and click "Create".
   
2. **Set up a Bot**:
   - On the left side panel, click on "Bot".
   - Click "Add Bot" and confirm.
   
3. **Get Your Bot Token**:
   - Under the "TOKEN" section, click "Copy" to copy your bot token. This will be used in the `config.py` file.

4. **Invite the Bot to Your Server**:
   - On the left side panel, click on "OAuth2".
   - Under "OAuth2 URL Generator", select "bot" in the scopes section.
   - Choose the desired permissions for your bot (It needs AT LEAST to be able to read messages and chat history).
   - Copy the generated URL and open it in your browser to invite the bot to your server.

## Installation

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

## Configuration

1. **Tokens & IDs**:
   - Open the config.py file in a text editor.
   - Replace PASTE_YOUR_DISCORD_BOT_TOKEN_HERE with the token you copied from the Discord Developer Portal.
   - Replace PASTE_YOUR_FRIEND_TECH_AUTHORIZATION_TOKEN_HERE with your Friend Tech authorization token.
   - Set the TARGET_CHANNEL_ID with the ID of the Discord channel you want the bot to listen to.
     > Tip: In Discord, enable Developer Mode in Settings to easily copy IDs by right-clicking on channels, users, etc.
  
2. **Chat Rooms**:
   - Open the `chat_room_ids.py` file in a text editor.
   - The file contains a list of placeholders for chat room IDs, identified by the wallet address of the room owner. Replace these placeholders with the actual addresses of the owners of he rooms where you want the bot to forward messages.

## How It Works
1. **Initialization**: When the bot starts, it connects to Discord using the provided token.
2. **Listening**: The bot continuously listens to messages sent in the specified Discord channel.
3. **Processing**: Upon receiving a message in the target channel, the bot establishes a WebSocket connection to the external API.
4. **Message Forwarding**: The bot forwards the received Discord message content to the external API.
5. **Disconnection**: After sending the message, the bot gracefully closes the WebSocket connection to the external API.

## Usage

1. **Run the bot**:
   ```bash
   python autod.py

   Your bot should now be running and listening to messages in the specified Discord channel.

Disclaimer: Please interact with the software at your own risk, I am not responsible for any loss or any downside caused by it. I cannot guarantee any results from it. The software is not an offering from me. I share no responsibility for the usage and outcome of this now open-sourced software.


