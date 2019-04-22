from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

serviceUsername = ""
servicePassword = ""
serviceURL = ""

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
print ("Successfully connected to Cloudant")


databaseName = "gfdfgthwtg"
x = client.create_database(databaseName)
##x = client[databaseName]
if x.exists():
    print ("'{0}' successfully created.\n".format(databaseName))
