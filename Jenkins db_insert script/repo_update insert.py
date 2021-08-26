#!/usr/bin/python

#The same script is copied to download,activation etc scripts.
# the variable "db_stage" slone to be modified for each script.

import MySQLdb
import re
import os
import datetime
import os, sys
import urllib2
import urllib
import paramiko

#db_stage variable is so important.This variable is used to trigger script present in 10.182.198.209
db_stage="build_repo"

jenkins_ip="135.249.27.140"
url=os.environ['JOB_URL']

#info about the job is fetched from below url
url="%sapi/python"%os.environ['BUILD_URL']
print url
stage_name_check= eval(urllib.urlopen(url).read())

#This below split is done to fetch moswa/snmp,copper/fiber,APME/ROBOT info from single parameter "PIPELINE_NAME"
jname=os.environ['PIPELINE_NAME']
jname=jname.split(":")

#The configurations moswa/snmp,copper/fiber,APME/ROBOT info from single parameter "PIPELINE_NAME" is not done yet.
#So below assignment is done to fetch the plaform name alone from PIPELINE_NAME
jname=jname[0]


print jname
stage_name=os.environ['STAGE_NAME']
print stage_name

ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("10.182.198.209",username="root",password="T&Dfndpc#123")  
channel = ssh_client.invoke_shell()

#4 arguements are passed to below python script.
cmd1="cd jenkins_datbase_scripts;python %s.py %s %s %s"%(db_stage,jname,stage_name,db_stage)
channel = ssh_client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

stdin.write(cmd1+"\n")
stdin.write('exit\n')
result= stdout.read()


print result

stdout.close()
stdin.close()
ssh_client.close()

Note:
Same script for DB preparation,download,activate,commit.
Db_stage name will be different for all insertion.