# Project: Telegram Bot for Sending a Message to a Channel

This project is a simple implementation of a Telegram bot that sends a message to a specific channel with an attached "Subscribe" button

## Installation and Setup

1. **Clone the repository**

   ```sh
   git clone <URL of your repository>
   cd <project folder name>
   ```

2. **Create a virtual environment and activate it**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # for Linux/macOS
   venv\Scripts\activate  # for Windows
   ```

3. **Install dependencies**

   ```sh
   pip install python-telegram-bot
   ```

## Bot Setup

1. **Get the token for your Telegram bot**

   - Go to Telegram and find the bot `@BotFather`.
   - Use the command `/newbot` to create a new bot and get the token.

2. **Replace the token in the code**

   - Find the line in the code and replace `'YOUR_BOT_TOKEN'` with your bot's token:
     ```python
     bot_token = 'YOUR_TOKEN'
     ```

## Usage

1. **Edit the parameters**

   - Make sure that `chat_id` contains the correct username of your channel (e.g., `'@InfoPulseru'`).

2. **Run the script**

   ```sh
   python bot.py
   ```

   The script will send a message to the specified channel with the "Subscribe" button.

## Notes

- Make sure your bot has permission to send messages to the channel. To do this, add it as an administrator of the channel.
- This example uses the `python-telegram-bot` library to interact with the Telegram API.

## Additional Information

- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

