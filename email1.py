import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#email credentials
sender_email = "kristinakattel45@gmail.com"
receiver_email = "ruman.metahorizon@gmail.com"
password = "dnyd kgsn pxzq dkcw"   #use password, NOT your gmail password app testing

#create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

#email body
body = "Hello, this is a test email sent from python."
message.attach(MIMEText(body, "plain"))
#send the email
try:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")