from dhooks import Webhook

webhook_url = 'YOUR_WEBHOOK_URL'

hook = Webhook(webhook_url)

hook.send('Hello!')
