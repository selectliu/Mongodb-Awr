#!/usr/bin/env python
import pymongo
import os
import operator
from  datetime  import  *
import  time
import getopt
import sys
import bson

class DbServerMoitor:
       def __init__(self,conn,locks,indexcount,record,opcounter,mem):
          self.conn = conn
          self.locks = locks
          self.indexcount=indexcount
          self.record=record
          self.opcounter=opcounter
          self.mem=mem
serverst = []
dbmons = []
if __name__ == '__main__':
    connection = pymongo.Connection('xxx.xx.xxx.xx',xxxx)
    db=connection.local
    content=db.command(bson.son.SON([('serverStatus',1)]))
    for key in content.keys():
        if key=='connections':
           serverst.append(content[key])
        if key=='locks':
           del content[key]['.']
           serverst.append(content[key])
        if key=='indexCounters':
           serverst.append(content[key])
        if key=='recordStats':
           serverst.append(content[key])
        if key=='opcounters':
           serverst.append(content[key])
        if key=='mem':
           serverst.append(content[key])
    dbmons.append(DbServerMoitor(serverst[0],serverst[1],serverst[4],serverst[2],serverst[5],serverst[3]))
    a=datetime(*(time.strptime(datetime.now().strftime('%Y-%m-%d %H:%M')+":01",'%Y-%m-%d %H:%M:%S')[0:6]))  
    for temp in dbmons:
        db.serverstatus.insert({"connections":temp.conn,"locks":temp.locks,"indexCounters":temp.indexcount,"recordStats":temp.record,"opcounter":temp.opcounter,"mem":temp.mem,"sertime":a})

        
    db.logout()
