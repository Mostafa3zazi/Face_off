import smtplib

smtp_server = "smtp.gmail.com"
port = 465  # For SSL
sender_email = "mostafa.3zazi@gmail.com" 
receiver_email = "mostafa.3zazi2@gmail.com"
message = """\
Subject: enter the subject here

write your message."""

#gmail pass for sender email
password = "enter your password here"   

server = smtplib.SMTP_SSL(smtp_server, port)
server.ehlo()
#server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email , message)
server.close()
print ('successfully sent the mail')
print ("failed to send mail")
