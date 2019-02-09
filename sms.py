from twilio.rest import Client
import sys
def main(dict):

    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC967c509f7b778e743a8fae5c620d1446'
    auth_token = '48824bc653c6fb9c56218e9e40e9d430'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_='+16078826488',
                         to='+16072798270'
                     )

    print(message.sid)
main({})
