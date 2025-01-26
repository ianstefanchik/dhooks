from dhooks import Webhook, Embed

webhook_url = 'YOUR_WEBHOOK_URL'

hook = Webhook(webhook_url)

embed = Embed(
    title='Author Example',
    description='This embed showcases the author field.',
    color=0xFF5733
)
embed.set_author(
    name='Author Name',
    url='https://example.com',
    icon_url='https://example.com/author-icon.png'
)

hook.send(embed=embed)
