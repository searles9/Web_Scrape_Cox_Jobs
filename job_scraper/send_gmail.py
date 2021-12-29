# Send Gmail Email
import smtplib
from email.message import EmailMessage
  
def send_gmail_email(sender_email,sender_app_password,recipient_email,subject,message):
    print("***Sending email with jobs")
    # Make email object
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    # Send email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_app_password)
    s.send_message(msg)
    s.quit()
    print("***The email was successfully sent!")