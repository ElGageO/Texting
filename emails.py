from lib2to3.refactor import MultiprocessingUnsupported
import win32com.client
from twilio.rest import Client

outlook = win32com.client.Dispatch('Outlook.Application')
outlookNS = outlook.GetNameSpace('MAPI')

myFolder = outlookNS.Folders['Gage_Reynolds1@baylor.edu'].Folders['Inbox']
messages = myFolder.Items

messagecount = 0
for message in messages:
    messagecount += 1
    if message.Unread:
        print(message.sender)
        print(message.subject)

        if 'absence' in message.subject:
            print('Found message with absence')

            msg = outlook.CreateItem(0)
            msg.Importance = 1
            msg.subject = 'Got your ' + message.subject + 'email'
            msg.HTMLBody = 'Hi ' + str(message.sender) + ',\n Sorry you are not well'

            msg.To = message.sender.GetExchangeUser().PrimarySmtpAddress
            msg.ReadReceiptRequested = True

            msg.Send()

accountSID = ''
authToken = ''
client = Client(accountSID, authToken)
TwilioNumber = '+19377773923'
myCellPhone = ''

textMessage = client.messages.create(to = myCellPhone, from_ = TwilioNumber, body = ('You have ' + str(messagecount) + ' email(s) in your inbox'))
