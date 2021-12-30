# Send Gmail Email
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib



def send_gmail_email(email_info):

    FILES = email_info["FILES"]
    EMAIL_SUBJECT = email_info["EMAIL_SUBJECT"]
    SENDER_EMAIL = email_info["SENDER_EMAIL"]
    EMAIL_TO = email_info["EMAIL_TO"]
    MESSAGE_BODY = email_info["MESSAGE_BODY"]
    SENDER_APP_PASSWORD = email_info["SENDER_APP_PASSWORD"]

# email_info["EMAIL_TO"]


    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(EMAIL_TO)
    # Add body to email
    msg.attach(body_part)
    # attach the files
    if FILES:
        for file in FILES:
            filename = str(file)
            with open(file,'rb') as file:
                msg.attach(MIMEApplication(file.read(), Name=filename))

    # Create SMTP object
    print("***Sending email with jobs")
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()
    smtp_obj.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
    smtp_obj.sendmail(msg['From'], EMAIL_TO, msg.as_string())
    smtp_obj.quit()
    print("***The email was successfully sent!")
