from discord import Color, Embed
import nextcord
from nextcord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()

GUILD_IDS = [863187370119659560, 574389293318012928]
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @bot.event
# async def on_member_join(member):

#     welcome_messages = ["Welcome to the server! <:apexMagic:886088735505149952>",
#     "Howdy gamer! <:khuckerEZ:881365671169101854>",
#     "Wait do I know you? <:brickWait:939759637719306271>",
#     "Hey got any trades? <:apexReader:906696005741838346>"]

#     embed = Embed(title= f"Welcome {member.display_name} to the server!",description=random.choice(welcome_messages), color= Color.blue())
#     embed.set_thumbnail(member.display_avatar)
#     await member.guild.system_channel.send(embed=embed)

# @bot.slash_command(name="socials",description="Gives link to socials", guild_ids=GUILD_IDS)
# async def socials(interaction: nextcord.Interaction):

#     embed = Embed(title='Apex Gaming | Linktree', description= "Check out all of our social media links here!",color = Color.blue(), url = "https://linktr.ee/apexgamingesports")
#     embed.set_thumbnail(url = "https://d1fdloi71mui9q.cloudfront.net/IwzPyzSnTLS8fdpNcS9W_IIKg6H3OYxV5YYVc")    
#     await interaction.send(embed=embed)

bot.run(BOT_TOKEN)