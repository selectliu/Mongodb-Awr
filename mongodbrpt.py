#!/usr/bin/env python
import pymongo
import os
import operator
from  datetime  import  *  
import  time 
import getopt  
import sys  


#configure database
if __name__ == '__main__':
     connection = pymongo.Connection('xx.xx.xx.xx',xxxx)
     dbadmin = connection.admin
   #  dbadmin.authenticate('mongodb','mongodb123')
     db=connection.local
     be=db.serverstatus.find().sort("sertime",pymongo.ASCENDING).limit(1)
     en=db.serverstatus.find().sort("sertime",pymongo.DESCENDING).limit(1)
     for dict in be:
          begtime=dict['sertime']
     for dict in en:
         endtime=dict['sertime']

#get parameter
opts, args = getopt.getopt(sys.argv[1:], 'hs:u:f:',   
      [  
        'since=',   
        'until=',
        'file=',
        'help'  
        ]  
      )  

if ( len( sys.argv ) == 1 ):
    print 'mongodbrpt.py -h or --help for detail'
    sys.exit(1)
elif(len( sys.argv ) <> 4 ): 
	 for option, value in opts: 
	     if  option in ["-h","--help"]:                                                                                           
	          print  "===================================================\n"                                                       
	          print  "|       Welcome to use the mongdbrpt tool !   \n"                                                             
	          print '''
	           Please modify you Connection configuration like this 
   	               connection = pymongo.Connection('10.1.69.157',17017)
                       dbadmin.authenticate('mongodb','mongodb123')
	          Usage :                                                                                                     
	          Command line options :                                                                                               	                                                                                                                               
	             -h,--help        Print Help Info.                                                                                                                                                                                                -s,--since       the report start time.                                  
	             -u,--until=      the report end time.
                     -f,--file=       the report file path.\n
	             '''                                
	          print '''Sample :                                                                                                    
	           shell>mongodbrpt.py --since="2014-03-31 18:01:50" --until="2014-03-31 18:01:52" --f=/home/mongodb/myawr.html'''          
	          print  "===================================================\n"                                                       
	          print  "Pls  enter the following periods: \n"                                                                        
	          print "The Earliest Start  time: %s" %begtime                                                                                    
	          print "The Latest Start time: %s" %endtime                                                                                    
                  print "If you find some question,you can connect me."
                  print "Mail:select.liu@hotmail.com Or Tele:13905699305 Or QQ:736053407"
                  print "\n"
 	          print  "------------------------------------\n"      
	     else:
	  	      print 'mongdbrpt.py -h or --help for detail'     
	  	      sys.exit(1)                                
	  	    	  	                                                                      	  	         
else:
    for option, value in opts:  
        if  option in ["-h","--help"]:  
                  print  "===================================================\n"                                                       
	          print  "|       Welcome to use the mongdbrpt tool !   \n"                                                             
	          print '''
	          Please modify you Connection configuration like this 
	               connection = pymongo.Connection('10.1.69.157',17017)
                 dbadmin.authenticate('mongodb','mongodb123')
	          Usage :                                                                                                     
	          Command line options :                                                                                               	                                                                                                                               
	             -h,--help        Print Help Info.                                                                                                                                                                                                -s,--since       the report start time.                                  
	             -u,--until=      the report end time.
                     -f,--file=       the report file path.\n
	             '''                                
	          print '''Sample :                                                                                                    
	          shell>mongdbrpt.py --since="2014-03-31 18:01:50" --until="2014-03-31 18:01:52" --f=/home/mongodb/myawr.html'''          
	          print  "===================================================\n"                                                       
	          print  "Pls  enter the following periods: \n"                                                                        
	          print "The Earliest Start  time: %s" %begtime                                                                                    
	          print "The Latest Start time: %s" %endtime                                                                                    
	          print  "\n"                                                                                                          
	          print  "------------------------------------\n"      
        elif option in ['--since', '-s']:            
            a=datetime(*(time.strptime(value,'%Y-%m-%d %H:%M:%S')[0:6]))  
            a1=datetime(*(time.strptime(value[0:17]+'01','%Y-%m-%d %H:%M:%S')[0:6]))
        elif option in ['--until', '-u']:  
            b=datetime(*(time.strptime(value,'%Y-%m-%d %H:%M:%S')[0:6])) 
            b1=datetime(*(time.strptime(value[0:17]+'01','%Y-%m-%d %H:%M:%S')[0:6]))+ timedelta(minutes=1)
        elif option in ['--file', '-f']:  
            filename=value               	   
    if a>b:
       print 'the start time is too early' 
    elif a<begtime:
       print 'the start time must grater than:%s' %begtime
       print 'mongodbrpt.py -h or --help for detail' 
    elif b>endtime:
       print 'the until time must less than:%s'%endtime
       print 'mongodbrpt.py -h or --help for detail'
    else:
       fp=open(filename,'w')
       
       
       myawrrpt_head='''<html><HEAD><TITLE>Mongodb WorkLoad Report</TITLE><style type="text/css">body.awr {font:bold 10pt Arial,Helvetica,Geneva,sans-serif;color:black; background:White;}
       pre.awr  {font:8pt Courier;color:black; background:White;}h1.awr   {font:bold 20pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;border-bottom:1px solid #cccc99;margin-top:0pt; margin-bottom:0pt;padding:0px 0px 0px 0px;}
       h2.awr   {font:bold 18pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}
       h3.awr {font:bold 16pt Arial,Helvetica,Geneva,sans-serif;color:#336699;background-color:White;margin-top:4pt; margin-bottom:0pt;}li.awr {font: 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;}
       th.awrnobg {font:bold 8pt Arial,Helvetica,Geneva,sans-serif; color:black; background:White;padding-left:4px; padding-right:4px;padding-bottom:2px}th.awrbg {font:bold 8pt Arial,Helvetica,Geneva,sans-serif; color:White; background:#0066CC;padding-left:4px; padding-right:4px;padding-bottom:2px}
       td.awrnc {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:White;vertical-align:top;}
       td.awrc    {font:8pt Arial,Helvetica,Geneva,sans-serif;color:black;background:#FFFFCC; vertical-align:top;}a.awr {font:bold 8pt Arial,Helvetica,sans-serif;color:#663300; vertical-align:top;margin-top:0pt; margin-bottom:0pt;}
       </style></HEAD><BODY class='awr'>
       <H1 class='awr'>
       Mongodb WorkLoad Report
       
       </H1>
       '''
       
       myawrrpt_foot='<p /> End of Report </body></html>';
       fp.write(myawrrpt_head)
       
       #get the recently startup information
       if __name__ == '__main__':
           startup_log= db.startup_log.find().sort("startTime",pymongo.DESCENDING).limit(1)
           for dict in startup_log:
               host_name= dict['hostname']
               startime= dict['startTimeLocal']
               pid=str(dict['pid'])
               version=dict['buildinfo']['version']
               portn=str(dict['cmdLine']['port'])
               param=dict['cmdLine']
       
       html_line='''
       <p />
       <table border=\"1\"  width=\"600\">
       <tr><th class='awrbg'>Host Name</th><th class='awrbg'>Port</th><th class='awrbg'>Version</th><th class='awrbg'>Pid</th><th class='awrbg'>Starttime</th></tr>
       <tr><TD class='awrnc'>'''+host_name+'''</td><TD ALIGN='right' class='awrnc'>'''+portn+'''</td><td align='right' class='awrnc'>'''+version+'''</td><TD ALIGN='right' class='awrnc'>'''+pid+'''</td><TD ALIGN='right' class='awrnc'> '''+startime+'''</td></tr>
       </table><p />'''
       
       fp.write(html_line)
       
       if __name__ == '__main__':          
           db=connection.local
           sin= db.serverstatus.find({"sertime":a1}).limit(1)       
           for dict in sin:
               sinconn=dict['connections']['current']
               since=a
               sinres=dict['mem']['resident']
               sinmap=dict['mem']['mapped']
               sinvsize=dict['mem']['virtual']
           end=db.serverstatus.find({"sertime":b1}).limit(1)
           for dict in end:
               endconn=dict['connections']['current']
               until=b
               endres=dict['mem']['resident']
               endmap=dict['mem']['mapped']
               endvsize=dict['mem']['virtual']
       html_line='''<TABLE BORDER=1 WIDTH=400>
       <tr><th class='awrnobg'></th><th class='awrbg'>Begin Time</th><th class='awrbg'>Connect</th></tr>
       <tr><TD class='awrnc'>Begin Time:</td><TD ALIGN='center' class='awrnc'>'''+str(since)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(sinconn)+'''</tr>
       <tr><TD class='awrc'>End Time:</td><TD ALIGN='center' class='awrc'>'''+str(until)+'''</td><TD ALIGN='right' class='awrc'>'''+str(endconn)+'''</tr>
       </table>'''
       
       
       fp.write(html_line)
       
       html_line='''<h3 class='awr'><a class='awr' NAME="99999"></a>Report Summary</h3>
       <p />
       Memory Sizes
       <p />
       <TABLE BORDER=1 WIDTH=400>
       <tr><th class='awrnobg'></th><th class='awrbg'>Begin Time</th><th class='awrbg'>End Time</th></tr>
       <tr><TD class='awrnc'>Res(M):</td><TD ALIGN='right' class='awrnc'>'''+str(sinres)+''' </td><TD ALIGN='right' class='awrnc'>'''+str(endres)+'''</td></tr>
       <tr><TD class='awrc'>Mapped(M):</td><TD ALIGN='right' class='awrc'>'''+str(sinmap)+'''</td><TD ALIGN='right' class='awrc'>'''+str(endmap)+'''</td></tr>
       <tr><TD class='awrc'>Vsize(M):</td><TD ALIGN='right' class='awrc'>'''+str(sinvsize)+'''</td><TD ALIGN='right' class='awrc'>'''+str(endvsize)+'''</td></tr>
       </table>'''
       fp.write(html_line) 
 

       class RecordStats:                                       
             def __init__(self,dbname,pageFaultExceptionsThrown,accessesNotInMemory,timeLockedMicros,timeAcquiringMicros):     
                 self.dbname = dbname                                 
                 self.pageFaultExceptionsThrown = pageFaultExceptionsThrown                              
                 self.accessesNotInMemory=accessesNotInMemory 
                 self.timeLockedMicros=timeLockedMicros
                 self.timeAcquiringMicros=timeAcquiringMicros                   
       
       r1=[]
       r2=[]

       if __name__ == '__main__':
           databases = connection.database_names()	
           db=connection.local
           sin= db.serverstatus.find({"sertime":a1}).limit(1) 
           for dict in sin:
               sinacess= dict['indexCounters']['accesses']
               sinhit=dict['indexCounters']['hits']
               singet=dict['opcounter']['getmore']   
               sinins=dict['opcounter']['insert']   
               sinupd=dict['opcounter']['update']   
               sincom=dict['opcounter']['command']   
               sinqry=dict['opcounter']['query']    
               sindel=dict['opcounter']['delete']   
               for i in range(len(databases)):
                   r1.append(RecordStats(databases[i],dict['recordStats'][databases[i]]['pageFaultExceptionsThrown'],dict['recordStats'][databases[i]]['accessesNotInMemory'],dict['locks'][databases[i]]['timeLockedMicros'],dict['locks'][databases[i]]['timeAcquiringMicros']))
           end=db.serverstatus.find({"sertime":b1}).limit(1)
           for dict in end:               
               endacess= dict['indexCounters']['accesses']
               endhit=dict['indexCounters']['hits'] 
               edndget=dict['opcounter']['getmore']  
               endins=dict['opcounter']['insert']   
               endupd=dict['opcounter']['update']   
               endcom=dict['opcounter']['command']  
               endqry=dict['opcounter']['query']    
               enddel=dict['opcounter']['delete']                  
               for i in range(len(databases)):   
                   r2.append(RecordStats(databases[i],dict['recordStats'][databases[i]]['pageFaultExceptionsThrown'],dict['recordStats'][databases[i]]['accessesNotInMemory'],dict['locks'][databases[i]]['timeLockedMicros'],dict['locks'][databases[i]]['timeAcquiringMicros']))
       aces= (float(endacess)-float(sinacess))/(float(endhit)-float(sinhit))*100
       getmore= float(edndget)-float(singet)
       cmd=float(endcom)-float(sincom)
       inser=float(endins)-float(sinins)
       up=float(endupd)-float(sinupd)
       qry=float(endqry)-float(sinqry)
       delet=float(enddel)-float(sindel)
       timedel=b1-a1
      
       pg=getmore/timedel.seconds
       pc= cmd/timedel.seconds
       pi= inser/timedel.seconds   
       pu= up/timedel.seconds   
       pq= qry/timedel.seconds   
       pd= delet/timedel.seconds 
       perget="%.2f" %pg
       percmd="%.2f" %pc
       perinser="%.2f" %pi
       perup="%.2f" %pu
       perqry="%.2f" %pq
       perdel="%.2f" %pd
       idxhit="%.2f" %aces
       
       html_line='''
       <p />
       Index  Hit(%) 
       <p />
       <TABLE BORDER=1 WIDTH=200>
       <tr><TD class='awrnc'>Index Hit</td><TD ALIGN='right' class='awrnc'>'''+str(idxhit)+''' </td></tr> 
       </table>'''
       
       fp.write(html_line) 
       
       html_line='''
        <p />Opcounter Profile<p />
        <TABLE BORDER=1 WIDTH=500>
        <tr><th class='awrnobg'></th><th class='awrbg'>Sum</th><th class='awrbg'>Per Second</th></tr>
        <tr><TD class='awrnc'>getmore</td><TD ALIGN='right' class='awrnc'>'''+str(getmore)+'''</td><TD ALIGN='right' class='awrc'>'''+str(perget)+'''</td></tr>
        <tr><TD class='awrc'>command</td><TD ALIGN='right' class='awrc'>'''+str(cmd)+'''</td><TD ALIGN='right' class='awrc'>''' +str(percmd)+'''</td></tr>
        <tr><TD class='awrc'>insert</td><TD ALIGN='right' class='awrc'>'''+str(inser)+'''</td><TD ALIGN='right' class='awrc'>'''+str(perinser)+'''</td></tr>
        <tr><TD class='awrnc'>update </td><TD ALIGN='right' class='awrnc'>'''+str(up)+'''</td><TD ALIGN='right' class='awrc'>'''+str(perup)+'''</td></tr>
        <tr><TD class='awrnc'>query</td><TD ALIGN='right' class='awrnc'>'''+str(qry)+'''</td><TD ALIGN='right' class='awrc'>'''+str(perqry)+'''</td></tr>
        <tr><TD class='awrc'>delete</td><TD ALIGN='right' class='awrc'>''' +str(delet)+'''</td><TD ALIGN='right' class='awrc'>'''+str(perdel)+'''</td></tr>
        </table>'''
       fp.write(html_line)  
      
       html_line2='''<p />RecordStats Profile<p />
          <TABLE BORDER=1 WIDTH=500>
          <tr><th class='awrbg'>dbname</th><th class='awrbg'>accessesNotInMemory</th><th class='awrbg'>pageFaultExceptionsThrown</th></tr>
''' 
       for i in range(len(r1)):
          html_line2+='''<tr><TD class='awrnc'>'''+r1[i].dbname+'''</td><TD ALIGN='right' class='awrnc'>'''+str(int(r2[i].accessesNotInMemory)-int(r1[i].accessesNotInMemory))+'''</td><TD ALIGN='right' class='awrnc'>'''+str(int(r2[i].pageFaultExceptionsThrown)-int(r1[i].pageFaultExceptionsThrown))+'''</td></tr>
'''  
       html_line2+='''</table>'''
       
       fp.write(html_line2) 
       
       html_line3='''<p />LockStats Profile<p />
          <TABLE BORDER=1 WIDTH=500>
          <tr><th class='awrbg'>dbname</th><th class='awrbg'>Read Wait(ms)</th><th class='awrbg'>Per Second</th><th class='awrbg'>Write Wait(ms)</th><th class='awrbg'>Per Second</th><th class='awrbg'>Read Lock(ms)</th><th class='awrbg'>Per Second</th><th class='awrbg'>Write Lock(ms)</th><th class='awrbg'>Per Second</th></tr>
'''    
       for i in range(len(r1)):
          ar= (long(r2[i].timeAcquiringMicros['r'])-long(r1[i].timeAcquiringMicros['r']))/1000
          aw= (long(r2[i].timeAcquiringMicros['w'])-long(r1[i].timeAcquiringMicros['w']))/1000
          lr= (long(r2[i].timeLockedMicros['r'])-long(r1[i].timeLockedMicros['r']))/1000
          lw= (long(r2[i].timeLockedMicros['w'])-long(r1[i].timeLockedMicros['w']))/1000
          perar=ar/timedel.seconds
          peraw=aw/timedel.seconds
          perlr=lr/timedel.seconds
          perlw=lw/timedel.seconds
          perar="%.2f" %perar
          peraw="%.2f" %peraw
          perlr="%.2f" %perlr
          perlw="%.2f" %perlw
          html_line3+='''<tr><TD class='awrnc'>'''+r1[i].dbname+'''</td><TD ALIGN='right' class='awrnc'>'''+str(ar)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(perar)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(aw)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(peraw)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(lr)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(perlr)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(lw)+'''</td><TD ALIGN='right' class='awrnc'>'''+str(perlw)+'''</td></tr>'''
          
       html_line3+='''</table>'''
             
       fp.write(html_line3)
       
       html_line4='''<p />Parammeter<p />                                                                                                                                                                                                                                                                                                                                                           
                     <table BORDER=1><tr><th class='awrbg'>Parameter Name</th><th class='awrbg'> value</th></tr>'''
       for key in param:
           html_line4+='''<tr><TD class='awrnc'>'''+str(key)+'''</td> <TD class='awrnc'>'''+str(param[key])+'''</td></tr>''' 
       html_line4+='''</table>'''
       fp.write(html_line4)
      
      
       html_line5='''<h2 class='awr'>
       SQL Statistics
       </h2>
       <table BORDER=1>
       <tr><th class='awrbg'>Elapsed  Time (ms)</th><th class='awrbg'>db name</th><th class='awrbg'>op</th><th class='awrbg'>ns</th><th class='awrbg'>numYield</th><th class='awrbg'>scanAndOrder</th><th class='awrbg'>nreturned </th><th class='awrbg'>nscanned</th><th class='awrbg'>ts</th><th class='awrbg'>client</th><th class='awrbg'>SQL Text</th></tr>'''
 
 
       for i in range(len(databases)):
           dn=str(databases[i])
           if dn not in ["admin","local"]:
              dn=str(databases[i])
              db=connection[dn]
              a =  a - timedelta(hours=8)  
              b= b - timedelta(hours=8) 
              sqlcont=db.system.profile.find({"ts":{"$gte":a,"$lt":b},"op":{"$ne":"command"}}).sort("millis",pymongo.DESCENDING).limit(20) 
              for temp in sqlcont:
                 if temp.has_key('nreturned'):
                     nreturned=temp['nreturned']
                 else:
                     nreturned=' '
                 if temp.has_key('nscanned'):
                    nscanned=temp['nscanned']
                 else:
                    nscanned=' '
                 if temp.has_key('scanAndOrder'):
                     scanAndOrder=temp['scanAndOrder']
                 else:
                     scanAndOrder=' '

                 op=temp['op']
                 millis= temp['millis'] 
                 ns = temp['ns']
                 numYield=temp['numYield']
                 ts=temp['ts']
                 client=temp['client']
                 query=str(temp['query'])
                 html_line5+='''<tr><TD ALIGN='right' class='awrc'>'''+str(millis)+'''</td><TD ALIGN='right' class='awrc'>'''+dn+'''</td> <TD ALIGN='right' class='awrc'>'''+op+'''</td>
<TD ALIGN='right' class='awrc'>'''+ns+'''</td> <TD ALIGN='right' class='awrc'>'''+str(numYield)+'''</td>  <TD ALIGN='right' class='awrc'>'''+str(scanAndOrder)+'''</td> <TD ALIGN='right' class='awrc'>'''+str(nreturned)+'''</td>
<TD ALIGN='right' class='awrc'>'''+str(nscanned)+'''</td><TD ALIGN='right' class='awrc'>'''+str(ts)+'''</td><TD ALIGN='right' class='awrc'>'''+client+'''</td><TD ALIGN='right' class='awrc'>'''+query+'''</td></tr>'''

       html_line5+='''</table>'''
       fp.write(html_line5)


       fp.write(myawrrpt_foot)
