import discord
import requests
import json

DISCORD_BOT_TOKEN = "PASTE_YOUR_DISCORD_TOKEN_HERE"
OPENROUTER_API_KEY = "PASTE_YOUR_OPENROUTER_API_KEY_HERE"

PERSONA_PROMPT = """
You are a dominant, seductive lesbian mommy. You speak slowly, affectionately, and command attention with every word. You love controlling, teasing, praising, and degrading your girl with obsession and intensity. You always stay in control.
"""

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

API_URL = "https://openrouter.ai/api/v1/chat/completions"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": PERSONA_PROMPT},
            {"role": "user", "content": message.content}
        ]
    }

    try:
        res = requests.post(API_URL, headers=HEADERS, json=payload)
        reply = res.json()['choices'][0]['message']['content']
        await message.channel.send(reply)
    except Exception as e:
        await message.channel.send("MommyBot broke. Try again later.")
        print("Error:", e)

client.run(DISCORD_BOT_TOKEN)
