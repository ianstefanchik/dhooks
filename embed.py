from dhooks import Webhook, Embed

webhook_url = 'YOUR_WEBHOOK_URL'

hook = Webhook(webhook_url)

embed = Embed(
    title='Thumbnail and Image Example',
    description='This embed contains both a thumbnail and an image.',
    color=0x7289DA
)
embed.set_thumbnail('https://example.com/thumbnail.png')
embed.set_image('https://example.com/image.png')

hook.send(embed=embed)
