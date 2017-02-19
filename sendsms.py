# Imports
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC9a667398c01a7f19c0ced954b4367b6d"
auth_token  = "74631dded75052e1acb457e411df8081"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Did you unplug the iron?",
    to="+12487362620",    # Replace with your phone number
    from_="+12482302248") # Replace with your Twilio number
print message.sid