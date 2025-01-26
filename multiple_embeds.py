from dhooks import Webhook, Embed

webhook_url = 'YOUR_WEBHOOK_URL'

hook = Webhook(webhook_url)

embed1 = Embed(title='Embed 1', description='This is the first embed.', color=0x1ABC9C)
embed2 = Embed(title='Embed 2', description='This is the second embed.', color=0x9B59B6)

hook.send(embeds=[embed1, embed2])
