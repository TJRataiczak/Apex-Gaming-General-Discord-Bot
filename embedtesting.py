from discord_webhook import DiscordWebhook, DiscordEmbed


webhook = DiscordWebhook(url = "https://discordapp.com/api/webhooks/988274101112160288/OhZLBf1L5DSQU-vPDa7_vpWr-kVlrbTPaZODOKazoR6TIWBOxsiYXq5q7lSsXTiSAsQJ")

embed = DiscordEmbed(title='Apex Gaming | Linktree', description= "Check out all of our social media links here!", color='03b2f8', url = "https://linktr.ee/apexgamingesports")
embed.set_thumbnail(url = "https://d1fdloi71mui9q.cloudfront.net/IwzPyzSnTLS8fdpNcS9W_IIKg6H3OYxV5YYVc")

webhook.add_embed(embed)

response = webhook.execute()