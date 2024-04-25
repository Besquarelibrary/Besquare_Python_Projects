# Import the smtplib module for SMTP functionality
import smtplib
# Import the MIMEText class for creating email body
from email.mime.text import MIMEText
# Import the MIMEMultipart class for creating email message
from email.mime.multipart import MIMEMultipart
import datetime


def email_service(Receiver_Email, Person_name):
    # Sender's email details
    sender_email = 'sangeethareddy2129@gmail.com'
    sender_password = 'app password'

    # Recipient's email details
    recipient_email = Receiver_Email

    # Email content
    subject = 'Builder Tracker Reminder'
    body_1 = f'Dear {Person_name},' \
             '\n' \
             '\n' \
             'Good Morning, This is reminder to start your  "Builder Tracker"  timer and run it for 8 hours without losing any work hours.' \
             '\n' \
             '\n' \
             'Please ignore this email if you have already started the tracker.' \
             '\n' \
             '\n' \
             'Thank you,\n' \
             'BeSquare Technologies' \
             '\n' \
             '\n' \
             'NOTE : This is a system generated email, Please do not reply to this message.'\

    body_2 = f'Dear {Person_name},' \
             '\n' \
             '\n' \
             'Good Evening, This is reminder to stop your  "Builder Tracker"  timer after completing 8 working hours.' \
             '\n' \
             '\n' \
             'Please ignore this email if you have already stopped the tracker.' \
             '\n' \
             '\n' \
             'Thank you,\n' \
             'BeSquare Technologies' \
             '\n' \
             '\n' \
             'NOTE : This is a system generated email, Please do not reply to this message.' \

    # Create the email message
    message = MIMEMultipart()
    # Set the 'From' header of the email message
    message['From'] = sender_email
    # Set the 'To' header of the email message
    message['To'] = recipient_email
    # Set the 'Subject' header of the email message
    message['Subject'] = subject
    # Flag to keep track if a message has been attached
    message_attached = False
    while not message_attached:
        time_now = datetime.datetime.now().strftime("%I:%M%p")

        if time_now == "09:55AM":
            # Create MIMEText attachment with body_1
            message.attach(MIMEText(body_1, 'plain'))
            # Set the flag to exit the loop
            message_attached = True
        elif time_now == "19:30":
            # Create MIMEText attachment with body_2
            message.attach(MIMEText(body_2, 'plain'))
            # Set the flag to exit the loop
            message_attached = True

    try:
        # Connect to Gmail's SMTP server using SSL
        with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
            # Login to the sender's Gmail account
            smtp.login(sender_email, sender_password)

            # Send the email
            smtp.send_message(message)

        # print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error: unable to send email.")
        print(str(e))

