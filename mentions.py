from dhooks import Webhook

webhook_url = 'YOUR_WEBHOOK_URL'

hook = Webhook(webhook_url)

user_id = 123456789012345678
role_id = 987654321098765432

message = f'Hello <@{user_id}> and <@&{role_id}>!'
hook.send(message)
