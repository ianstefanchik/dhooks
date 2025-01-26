from dhooks import Webhook

webhook_url = 'YOUR_WEBHOOK_URL'

hook = Webhook(webhook_url)

with open('example.txt', 'rb') as file:
    hook.send(file=file)
