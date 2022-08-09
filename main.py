import datetime
from discord import Color, Embed
import nextcord
from nextcord.ext import commands

GUILD_IDS = [863187370119659560, 574389293318012928]
BOT_TOKEN = "OTgzNTY2Nzg2MjQwODQzODI3.GTGdx2.N0wvxdueME8fG7uDmrLDktPjSafCGerOh0FgHM"


intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(name="testing",description="Testing Purpose", guild_ids=GUILD_IDS)
async def testing(interaction: nextcord.Interaction):

    embed = Embed(title= f"Welcome {interaction.user.display_name}!", color= Color.blue(), timestamp=datetime.datetime.now())
    embed.set_thumbnail(interaction.user.display_avatar)
    await interaction.send(embed=embed)

@bot.slash_command(name="socials",description="Gives link to socials", guild_ids=GUILD_IDS)
async def socials(interaction: nextcord.Interaction):

    embed = Embed(title='Apex Gaming | Linktree', description= "Check out all of our social media links here!",color = Color.blue(), url = "https://linktr.ee/apexgamingesports", timestamp=datetime.datetime.now())
    embed.set_thumbnail(url = "https://d1fdloi71mui9q.cloudfront.net/IwzPyzSnTLS8fdpNcS9W_IIKg6H3OYxV5YYVc")
    
    await interaction.send(embed=embed)

bot.run(BOT_TOKEN)