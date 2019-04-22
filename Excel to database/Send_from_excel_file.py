# Reading an excel file using Python 
import xlrd 
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import json
import ast

columnN=4
rowN=5

# Give the location of the file 
loc = ("test.xlsx")
# To open Workbook 
wb = xlrd.open_workbook(loc)    
sheet = wb.sheet_by_index(0)

serviceUsername = ""
servicePassword = ""
serviceURL = ""
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = "class"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print ("'{0}' successfully created.\n".format(databaseName))

document={}
for y in range(1,rowN):
    document["_"+sheet.cell_value(0, 0)]= str(int(sheet.cell_value(y, 0)))
    for x in range(1,columnN):
        document[sheet.cell_value(0, x)]= sheet.cell_value(y, x)
    newDocument = myDatabaseDemo.create_document(document)
    if newDocument.exists:
        print ("Document '{0}' successfully created.".format(y))
