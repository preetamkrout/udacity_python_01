from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = 'AC3688738d8b44b1d65c4818ba79cf5b4c'
AUTH_TOKEN = '29774df212b2739ee1705186df9d42eb'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to = '+919778444465',
    from_ = '+16284444465',
    body = 'Hey There. this is preetam'
)

print("Request has been sent")
