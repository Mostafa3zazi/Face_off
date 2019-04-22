from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

serviceUsername = "6fd37c9b-4719-4fe6-9494-509a4f4e2130-bluemix"
servicePassword = "349ecad031b57c58c0bd4b3991abd44b41d78a49632fb6456a038dcfd83951fc"
serviceURL = "https://6fd37c9b-4719-4fe6-9494-509a4f4e2130-bluemix:349ecad031b57c58c0bd4b3991abd44b41d78a49632fb6456a038dcfd83951fc@6fd37c9b-4719-4fe6-9494-509a4f4e2130-bluemix.cloudant.com"


client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
print ("Successfully connected to Cloudant")
