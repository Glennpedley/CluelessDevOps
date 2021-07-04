import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
to_whatsapp_no = os.environ['to_whatsapp_no']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='This is Jimmy Virgin Slayer mission done',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+to_whatsapp_no
                          )

print("Message ID:",message.sid)
