import smtplib
import ssl
from email.message import EmailMessage


def emailing(sender, psd ,  receiver, sub, boddy):
    email_sender = sender
    email_password = psd
    email_receiver = receiver

    subject = sub
    body = boddy

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())



receivers = ["receiver1", "receiver2", ".."]


  

for email in receivers:
      emailing("your eamil", "psd",email, "the email")

   
