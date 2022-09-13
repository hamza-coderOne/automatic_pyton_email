import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = "email" 
EMAIL_PASSWORD = "psd"

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = "MAIN TITLE"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'RECEIVER'

msg.set_content('This is a plain text email')

## body text 
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        <ul>
           <li>Hello world</li>
           <li>Hello world</li>
           <li>Hello world</li>
        </ul>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
