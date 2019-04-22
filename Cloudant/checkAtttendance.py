from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import smtplib

serviceUsername = ""
servicePassword = ""
serviceURL = ""

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

smtp_server = "smtp.gmail.com"
port = 465  # For SSL
sender_email = "meky1021997@gmail.com" 


#gmail pass for sender email
password = "OMAR$1021997"  #must be string



databaseName = "class"
database = client[databaseName]
if database.exists():
    print ("'{0}' successfully connected.\n".format(databaseName))


#server.starttls()

##check attendance
for document in database:
    if document['attendance']<5:
        print(document['name'])
        print(document['email'])

        ##send messages here
        receiver_email = document['email']
        
        message = """Subject: Hi {0}


        This message is sent from Python.
        your attendace is {1}""".format(document['name'],document['attendance'])
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email , message)
        print ('successfully sent the mail')
        
server.close()
        
