import datetime
import discord
from discord.ext import commands

# declare intents
intents = discord.Intents.default()
intents.message_content = True

# initiate client and commands
bot = commands.Bot(command_prefix = "!", intents=intents)

# lets set up some important texts
# this is the help screen
f = open("help.txt")
helpText = f.read()
f.close()

logbook = open("logs.txt", "a")

# using the command api
# the arguments in the command are:
# "ctx" is the current channel
# "member : discord.Member" is the member specified in the second argument

# ban
@bot.command()
async def ban(ctx, member : discord.Member, reason): #get the member as the second argument
    await member.ban(reason = reason)
    banMessage = "@" + str(member) + " was banned with reason: " + reason
    await ctx.send(banMessage)
    logbook.write("Time: " + str(datetime.time) + " User: " + str(member) + " Action: Ban")

# timeout
@bot.command()
async def timeout(ctx, member : discord.Member, timeInHours):
    await member.timeout(datetime.timedelta(hours=int(timeInHours)))
    timeoutMessage = "@" + str(member) + " was timed out for: " + str(timeInHours) + " hours"

@bot.command()
async def kick(ctx, member : discord.Member):
    await member.kick()
    kickMessage = "@" + str(member) + " was kicked"
    await ctx.send(kickMessage)

@bot.command()
async def warn(ctx, member : discord.Member, reason):
    warnMessage = "@" + str(member) + " has been warned for: " + reason
    await ctx.send(warnMessage)

# run the bot below here, dont modify

f = open("token.txt")
token = f.read()
f.close()

bot.run(token)
