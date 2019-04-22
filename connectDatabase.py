from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

serviceUsername = ""
servicePassword = ""
serviceURL = ""


client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
print ("Successfully connected to Cloudant")
