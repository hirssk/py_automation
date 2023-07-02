from slack_sdk import WebClient
from account import slack_bot 

client = WebClient(slack_bot.token)

msg = "slack app test message."
response = client.chat_postMessage(channel=slack_bot.send_channel, text=msg)