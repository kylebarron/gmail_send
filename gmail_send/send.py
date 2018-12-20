import httplib2
import oauth2client
import base64

from email.mime.text import MIMEText
from apiclient import discovery
from oauth2client import client, tools
from pathlib import Path


def send(
        to_addr,
        from_addr,
        subject,
        msg,
        text_format='plain',
        client_secret_path='~/.config/gmail_send/client_secret.json',
        credential_path='~/.credentials/gmail_send.json'):
    """Send email through gmail

    Args:
        to_addr (str): address to send email to
        from_addr (str): address that is sending the email
        subject (str): subject of email
        msg (str): email body text
        text_format (str): either 'plain' for plain text or 'html' for
            HTML-formatted text
        client_secret_path (str): path to client_secret.json
        credential_path (str): path to credentials object

    Returns:
        (bool): True if email was successfully sent; False otherwise
    """

    # API info
    # --------

    client_secret_path = Path(client_secret_path).expanduser()
    credential_path = Path(credential_path).expanduser()
    scopes = ['https://www.googleapis.com/auth/gmail.send']

    # Create gmail messages object
    # ----------------------------

    credentials = get_credentials(client_secret_path, scopes, credential_path)
    http = credentials.authorize(httplib2.Http())
    messages = discovery.build('gmail', 'v1', http=http).users().messages()

    message_object = create_message(
        sender=from_addr,
        to=to_addr,
        subject=subject,
        message_text=msg,
        text_format=text_format)

    try:
        messages.send(userId='me', body=message_object).execute()
        return True
    except Exception as e:
        print(e)
        return False


def get_credentials(client_secret_path, scopes, credential_path, flags=None):
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_path, scopes)
        flow.user_agent = 'gmail_send'
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + str(credential_path))

    return credentials


def create_message(sender, to, subject, message_text, text_format='plain'):
    """Create a message for an email.

    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

    Returns:
        An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text, text_format)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def authenticate_cli():

    client_secret_path = '~/.config/gmail_send/client_secret.json'
    credential_path = '~/.credentials/gmail_send.json'
    client_secret_path = Path(client_secret_path).expanduser()
    credential_path = Path(credential_path).expanduser()
    scopes = ['https://www.googleapis.com/auth/gmail.send']

    get_credentials(client_secret_path, scopes, credential_path)
