import discord
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Initialize Hugging Face Client
client_hf = InferenceClient(api_key=HUGGINGFACE_API_KEY)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Function to get AI response
def generate_response(prompt):
    messages = [{"role": "user", "content": prompt}]
    
    response = client_hf.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        messages=messages,
        temperature=0.5,
        max_tokens=2048,
        top_p=0.7,
        stream=False  # Ensure stream=False for easier handling
    )

    # Ensure response is a dictionary, not a raw string
    if isinstance(response, str):  # If response is a string, return it directly
        return response

    # Extract the text safely
    if hasattr(response, "choices") and response.choices:
        return response.choices[0].message.content

    return "I have no words for that."

# Event handlers
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_input = message.content
    async with message.channel.typing():
        response = generate_response(user_input)

    await message.channel.send(response)

# Run the bot
client.run(DISCORD_TOKEN)
