# gmail_send

Simple wrapper to send emails through Gmail

## Install

```
$ pip install --upgrade git+https://github.com/kylebarron/gmail_send
```

## Setup

First you have to grab an OAuth2 token from Google. Adapted from the [Gmail API quickstart](https://developers.google.com/gmail/api/quickstart/python):

1. Use [this wizard](https://console.developers.google.com/start/api?id=gmail) to create or select a project in the Google Developers Console and automatically turn on the API. Click **Continue**, then **Go to credentials**.
2. On the **Add credentials to your project** page, click the **Cancel** button.
3. At the top of the page, select the **OAuth consent screen** tab. Select an **Email address**, enter a **Product name** if not already set, and click the **Save** button.
4. Select the **Credentials** tab, click the **Create credentials** button and select **OAuth client ID**.
5. Select the application type **Other**, enter the name "Gmail API Quickstart", and click the **Create** button.
6. Click **OK** to dismiss the resulting dialog.
7. Click the `file_download` (Download JSON) button to the right of the client ID.

This package expects the `client_secret.json` file to be placed at

```
~/.config/gmail_send/client_secret.json
```

To finish the authentication, from the command line run the following

```
gmail_send_auth
```

Your web browser should open to the Gmail authentication page.

## Usage

```python
from gmail_send import send

send(
    to_addr='to@example.com',
    from_addr='from@gmail.com',
    subject='subject',
    msg='message',
    text_format='plain')
```

### Full API

```
Args:
    to_addr (str): address to send email to
    from_addr (str): address that is sending the email
    subject (str): subject of email
    msg (str): email body text
    text_format (str): either 'plain' for plain text or 'html' for
        HTML-formatted text

Returns:
    (bool): True if email was successfully sent; False otherwise
```

## Requirements

Python 3.6; Python 3.5 may work


