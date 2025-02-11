# Discord Bot with Hugging Face Integration (DeepSeek-R1-Distill-Qwen-32B)

This project is a Discord bot that uses the Hugging Face API to generate AI responses to user messages.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd discord-bot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Discord token and Hugging Face API key:
    ```properties
    DISCORD_TOKEN="your_discord_token_here"
    HUGGINGFACE_API_KEY="your_huggingface_api_key_here"
    ```

## Usage

1. Run the bot:
    ```sh
    python bot.py
    ```

2. The bot will log in to Discord and start listening for messages. When a user sends a message, the bot will generate a response using the Hugging Face API and send it back to the channel.

## Files

- `bot.py`: The main script that sets up and runs the Discord bot.
- `.env`: Environment variables file containing the Discord token and Hugging Face API key.

## Requirements

- Python 3.7+
- `discord.py`
- `python-dotenv`
- `huggingface_hub`


