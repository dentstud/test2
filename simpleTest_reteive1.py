

import pymongo
from time import sleep

myclient = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds135592.mlab.com:35592/data_db")   #mongodb://localhost:27017/
mydb = myclient["data_db"]  #  file
mycol = mydb["data"]  # collection - table 



order = False 
while order == False:
    for x in mycol.find().sort('_id', -1).limit(1):   #.skip(1):
        c = x['k']['c']
        o = x['k']['o']
        eventTime = x['E']
        change = round(((float(c)-float(o)) / float(o)*100),2)
    if change <= 0:
        print (change, eventTime)
        
#    print ("Open: "+o+" -- Close:  "+c)
#    print(change)
    sleep(1)
#if float(y) > 1:
#    print('yes')
#else:
#    print ('no')
    


