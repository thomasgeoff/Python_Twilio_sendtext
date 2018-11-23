from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc76cda42a62d0699bcc96d0613d3b7d9"
# Your Auth Token from twilio.com/console
auth_token  = "925064d7b8cdd88c88d4619098258a82"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19169533391", 
    from_="+19169533391",
    body="Hello from Python!")

print(message.sid)
