from twilio.rest import Client

accountSID = ''
authToken = ''
client = Client(accountSID, authToken)
TwilioNumber = '+19377773923'
myCellPhone = '+'

# Sending a text
textMessage = client.messages.create(to = myCellPhone, from_ = TwilioNumber, body = 'Nice cock')
print(textMessage.status)

# Making a call
#call = client.calls.create(url = 'http://demo.twilio.com/docs/voice.xml', to = myCellPhone, from_ = TwilioNumber)
