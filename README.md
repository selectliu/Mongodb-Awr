Mongodb-Awr
===========
如发现问题可以联系：Mail:select.liu@hotmail.com Or Tele:13905699305 Or QQ:736053407

Monogdb Awr是用python语言开发的。
主要记录了内存，lock，record stats，opcounter profile，bad sql等几大块信息，在mongodb2.4.5和mongodb2.4.9已经做过测试。
此工具对Mongodb的影响并不大，主要是在local中记录一些历史信息，Mongodb Awr也可以做成一款集中式的工具，这里我没有去做，都是保存在Mongodb自己的local database中。在安装配置时也不需要特别设置Mongodb，如果要记录Mongodb的bad sql需要开启profile。
[root@bj3mem003 monitor]# mongo -port 17017
MongoDB shell version: 2.4.5
connecting to: 127.0.0.1:17017/test
>
> db.setProfilingLevel(1,500)
{ "was" : 0, "slowms" : 500, "ok" : 1 }
> db.getProfilingStatus()
{ "was" : 1, "slowms" : 500 }

介绍一下Mongodb Awr的部署和安装。

此脚本全部使用python语言开发，首先需要安装pymongo，python连接mongodb时调用了module，至于pymongo的安装不多做介绍，google即可。

Mongodb Awr主要为三个脚本。

[root@bj3mem003 monitor]# ls -ltrh

total 516K

-rwxr--r-- 1 root root 2.1K Apr  8 16:54 mongodbserverstatus.py

-rwxr--r-- 1 root root  551 Apr  8 16:57 mongdel.py

-rwxr--r-- 1 root root  22K Apr  9 09:27 mongodbrpt.py

这三个脚本都依赖于pymongo Connection需要结合自己的环境修改连接到mongodb的配置。只需将每个脚本中connect部分修改为自己实际的信息即可。

if __name__ == '__main__':
connection = pymongo.Connection('10.1.64.23',17017) --连接信息
dbadmin = connection.admin
dbadmin.authenticate('mongodb','mongodb123') --认证的密码，没有可以不设置

第一个脚本mongodbserverstatus.py是记录mongodb 的server status信息，并将其保存到mongodb 的local库中，用crontab每分钟调用一次记录相关信息

[root@bj3mem003 monitor]# crontab -l。

*/1 * * * * su - mongodb -c "/home/mongodb/monitor/mongodbserverstatus.py  >> /home/mongodb/monitor/mongodbserver.log"
0 1 * * * su - mongodb -c "/home/mongodb/monitor/mongdel.py  >> /home/mongodb/monitor/mongdel.log"

[root@bj3mem003 monitor]# mongo -port 17017

MongoDB shell version: 2.4.5

connecting to: 127.0.0.1:17017/test

>

> use local

switched to db local

> show tables

serverstatus

startup_log

system.indexes

system.profile

> db.serverstatus.findOne()

{

     "_id" : ObjectId("5343b9604ead2d6541000000"),

     "mem" : {

         "resident" : 4701,

         "supported" : true,

         "virtual" : 18737,

         "mappedWithJournal" : 18394,

         "mapped" : 9197,

         "bits" : 64

     },

     "opcounter" : {

         "getmore" : 0,

         "insert" : 1136236,

         "update" : 833078557,

         "command" : 67112,

         "query" : 835074131,

         "delete" : 1078569

     },

     "indexCounters" : {

         "missRatio" : 0,

         "resets" : 0,

         "hits" : 460589161,

         "misses" : 0,

         "accesses" : 460589169

     },

     "recordStats" : {

         "admin" : {

              "pageFaultExceptionsThrown" : 0,

              "accessesNotInMemory" : 0

         },

         "pageFaultExceptionsThrown" : 0,

         "uudb" : {

              "pageFaultExceptionsThrown" : 0,

              "accessesNotInMemory" : 0

         },

         "uucun_baiduproxy" : {

              "pageFaultExceptionsThrown" : 0,

              "accessesNotInMemory" : 0

         },

         "test" : {

              "pageFaultExceptionsThrown" : 0,

              "accessesNotInMemory" : 0

         },

         "local" : {

              "pageFaultExceptionsThrown" : 0,

              "accessesNotInMemory" : 0

         },

         "accessesNotInMemory" : 0

     },

     "connections" : {

         "current" : 51,

         "available" : 768,

         "totalCreated" : 78007

     },

     "locks" : {

         "admin" : {

              "timeAcquiringMicros" : {

                   "r" : 479915,

                   "w" : 0

              },

              "timeLockedMicros" : {

                   "r" : 23454820,

                   "w" : 0

              }

         },

         "uudb" : {

              "timeAcquiringMicros" : {

                   "r" : NumberLong("6718581544412"),

                   "w" : NumberLong("4862305557749")

              },

              "timeLockedMicros" : {

                   "r" : NumberLong("3497936412371"),

                   "w" : NumberLong("2530517353265")

              }

         },

         "uucun_baiduproxy" : {

              "timeAcquiringMicros" : {

                   "r" : NumberLong("25032187428"),

                   "w" : 88974095

              },

              "timeLockedMicros" : {

                   "r" : NumberLong("72133781064"),

                   "w" : 848716611

              }

         },

         "test" : {

              "timeAcquiringMicros" : {

                   "r" : 1061945,

                   "w" : 0

              },

              "timeLockedMicros" : {

                   "r" : 13773452,

                   "w" : 0

              }

         },

         "local" : {

              "timeAcquiringMicros" : {

                   "r" : 2919743,

                   "w" : 0

              },

              "timeLockedMicros" : {

                   "r" : 41814185,

                   "w" : 0

              }

         }

     },

     "sertime" : ISODate("2014-04-08T16:54:01Z")

}

可以看到mongodbserverstatus.py 脚本会在local中产生一个serverstatus collection 用于保存历史信息。

第二个脚本mongdel.py 是用于删除历史信息，用于保存几天的历史信息，默认是保存10天的信息。可以手工执行该脚本，也可以使用crontab命令，自动执行。

第三个脚本 mongodbrpt.py脚本就是用于产生awr报告的脚本，目前做的功能比较简单，不接受太多的参数

[root@bj3mem003 monitor]# ./mongodbrpt.py
mongodbrpt.py -h or --help for detail
[root@bj3mem003 monitor]# ./mongodbrpt.py -h

===================================================

|       Welcome to use the mongdbrpt tool !

Please modify you Connection configuration like this
connection = pymongo.Connection('10.1.69.157',17017)
dbadmin.authenticate('mongodb','mongodb123')
Usage :
Command line options :
-h,--help        Print Help Info.                                                                                                                                                                                                -s,--since       the report start time.
-u,--until=      the report end time.
-f,--file=       the report file path.

Sample :
shell>mongodbrpt.py --since="2014-03-31 18:01:50" --until="2014-03-31 18:01:52" --f=/home/mongodb/myawr.html
===================================================

Pls  enter the following periods:

The Earliest Start  time: 2014-04-08 16:54:01
The Latest Start time: 2014-04-09 11:05:01
If you find some question,you can connect me.
Mail:select.liu@hotmail.com Or Tele:13905699305 Or QQ:736053407

------------------------------------

在使用mongodbrpt.py -h 查看help信息时，提示了，产生awr报告时可以输入的时间段。

[root@bj3mem003 monitor]# ./mongodbrpt.py --since='2014-04-09 09:00:01' --until="2014-04-09 09:15:01" --f=/root/mong.html
[root@bj3mem003 monitor]# ls -ltrh /root/mong.html
-rw-r--r-- 1 root root 8.5K Apr  9 10:23 /root/mong.html

 
Mongodb WorkLoad Report

 
Host Name	Port	Version	Pid	Starttime
xxxxx	17017	2.4.5	5629	Fri Aug 9 11:49:01.211
 	Begin Time	Connect
Begin Time:	2014-04-09 09:00:01	51
End Time:	2014-04-09 09:15:01	50
Report Summary

Memory Sizes

 
 	Begin Time	End Time
Res(M):	4692	4690
Mapped(M):	9277	9277
Vsize(M):	18897	18897

Index Hit(%)

 
Index Hit	100.00

Opcounter Profile

 
 	Sum	Per Second
getmore	0.0	0.00
command	367.0	0.38
insert	8043.0	8.38
update	2818775.0	2936.22
query	2828608.0	2946.47
delete	7910.0	8.24

RecordStats Profile

 
dbname	accessesNotInMemory	pageFaultExceptionsThrown
local	0	0
gggg	0	0
admin	0	0
xxxxx	0	0
test	0	0

LockStats Profile

 
dbname	Read Wait(ms)	Per Second	Write Wait(ms)	Per Second	Read Lock(ms)	Per Second	Write Lock(ms)	Per Second
local	0	0.00	0	0.00	1	0.00	4	0.00
xxxg	1634161	1702.00	1173462	1222.00	827958	862.00	572885	596.00
admin	0	0.00	0	0.00	2	0.00	0	0.00
gggxx	9	0.00	1	0.00	326	0.00	43	0.00
test	0	0.00	0	0.00	0	0.00	0	0.00

Parammeter

 
Parameter Name	value
logpath	/var/log/mongodb/mongodb.log
logappend	true
config	/opt/mongodb/etc/mongodb.conf
dbpath	/app/mongodb/data
port	17017
SQL Statistics
Elapsed Time (ms)	db name	op	ns	numYield	scanAndOrder	nreturned	nscanned	ts	client	SQL Text

End of Report
