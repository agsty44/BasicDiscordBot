import discord

# declare intents
intents = discord.Intents.default()
intents.message_content = True

# initiate client
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.lower() == "!help":
        await message.channel.send\
            ("""Commands:
             !help - opens the help menu.
                                   """)
        
f = open("token.txt")
token = f.read()

client.run(token)