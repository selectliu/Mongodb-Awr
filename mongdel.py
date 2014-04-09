#!/usr/bin/env python
import pymongo
import os
import operator
from  datetime  import  *  
import  time  

if __name__ == '__main__':
    connection = pymongo.Connection('xx.xx.xxx.xxx',xxx)
    dbadmin = connection.admin 
    dbadmin.authenticate('mongodb','mongodb123')
    db=connection.local
    d1= datetime.now()
    delday =  d1 - timedelta(days=10)  
    print delday
    print d1
    db.dbmonitor.remove({"time":{'$lt':delday}})
    db.serverstatus.remove({"sertime":{'$lt':delday}})
    db.logout()
