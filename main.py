import discord
from discord.ext import commands
import config
import time
import bottoken
intents = discord.Intents.default()  # All but the two privileged ones
intents.members = True  # Subscribe to the Members intent
bot = commands.Bot(command_prefix = config.invoke_char, help_command=None, intents=intents)



@bot.event
async def on_ready(): #Ran when the bot is started
    global startTime
    startTime = time.time()
    print("bot online")



@bot.command()
@commands.has_guild_permissions(move_members=True)
async def bully(ctx, person:discord.Member=None, *, amount=None):
    memids = []
    channel = bot.get_channel(config.standard_channel_id)
    afk_channel = bot.get_channel(config.afk_channel_id)
    member = person
    embedvar = discord.Embed(title=f"✅ bully succesfull", description=f"{ctx.message.author} has bullied you for deserving it. You will be moved {amount} times", color=int(float(100)))
    await member.send(embed=embedvar)
    embedvar_chat = discord.Embed(title=f"✅ bully successful", description=f"{ctx.message.author} has bullied {member} {amount} times", color=int(float(100)))
    await ctx.channel.send(embed=embedvar_chat)
    print(person)
    if amount == 0 or amount == None:
        amount = 1
    else:
        pass
    bully_times = 1
    while bully_times < int(amount) or bully_times == int(amount):
        await person.move_to(afk_channel)
        bully_times = bully_times+1

        def check(person, before, after):
            print("test")
            return person.id == member.id and after.channel == channel

        await bot.wait_for("voice_state_update", check=check)





bot.run(bottoken.Secret_token)













