import nextcord
from nextcord.ext import commands

GUILD_IDS = [863187370119659560]
BOT_TOKEN = "OTgzNTY2Nzg2MjQwODQzODI3.GTGdx2.N0wvxdueME8fG7uDmrLDktPjSafCGerOh0FgHM"

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(name="ping",description="Replys Pong!", guild_ids=GUILD_IDS)
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!")

@bot.slash_command(name="socials",description="Gives link to socials", guild_ids=GUILD_IDS)
async def socials(interaction: nextcord.Interaction):
    await interaction.send("https://linktr.ee/apexgamingesports")

bot.run(BOT_TOKEN)