from twilio.rest import Client
import sys
def main(dict):

    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_='+16078826488',
                         to='+16072798270'
                     )

    print(message.sid)
main({})
