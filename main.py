import datetime
from discord import Color, Embed
import nextcord
from nextcord.ext import commands
import random

GUILD_IDS = [863187370119659560, 574389293318012928]
BOT_TOKEN = "OTgzNTY2Nzg2MjQwODQzODI3.GTGdx2.N0wvxdueME8fG7uDmrLDktPjSafCGerOh0FgHM"


intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_join(member):

    welcome_messages = [f"Welcome to the server!<:apexMagic:886088735505149952>\n{member.mention}",
                        f"Howdy gamer!<:khuckerEZ:881365671169101854>\n{member.mention}",
                        f"Wait do I know you?<:brickWait:939759637719306271>\n{member.mention}",
                        f"Hey got any trades?<:apexReader:906696005741838346>\n{member.mention}"]

    embed = Embed(title= "Welcome!", description = random.choice(welcome_messages), color= Color.blue())
    embed.set_thumbnail(member.avatar)
    embed.set_footer()
    await member.guild.system_channel.send(embed=embed)

@bot.slash_command(name="socials",description="Gives link to socials", guild_ids=GUILD_IDS)
async def socials(interaction: nextcord.Interaction):

    embed = Embed(title='Apex Gaming | Linktree', description= "Check out all of our social media links here!",color = Color.blue() , url = "https://linktr.ee/apexgamingesports", timestamp=datetime.datetime.now())
    embed.set_thumbnail(url = "https://d1fdloi71mui9q.cloudfront.net/IwzPyzSnTLS8fdpNcS9W_IIKg6H3OYxV5YYVc")
    
    await interaction.send(embed=embed)
    print(interaction.user.avatar)

bot.run(BOT_TOKEN)