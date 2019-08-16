import json

from twilio.rest import Client

# load the stories that were scraped
with open('stories.json') as f:
    stories = json.load(f)

# load twilio details
with open('account.json', 'r') as f:
    account = json.load(f)

# send the alert
def sendAlert(number, message):
    client = Client(account['accountSID'], account['authToken'])
    message = client.messages.create(
        to=number,
        from_="+19389999671",
        body=message)

# this is an awful way to do this but I want to go home I will clean it up at a later date
sent = ''

# concatenate every 5 paragraphs and send them
for i, sentence in enumerate(stories):
    sent = sent + sentence
    if i % 5 == 0:
        try:
            sendAlert('+18032922566', sent)
        except:
            pass

        # resets the sentence for the next text
        sent = ''
