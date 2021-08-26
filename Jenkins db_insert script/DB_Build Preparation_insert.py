#!/usr/bin/python

import MySQLdb
import re
import os
import datetime
import os, sys
import urllib2
import urllib
import paramiko

db_stage="build_preparation"

jenkins_ip="135.249.27.140"
url=os.environ['JOB_URL']


url="%sapi/python"%os.environ['BUILD_URL']
print url
stage_name_check= eval(urllib.urlopen(url).read())


jname=os.environ['PIPELINE_NAME']
jname=jname.split(":")
jname=jname[0]
print jname
stage_name=os.environ['STAGE_NAME']
print stage_name

ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect("10.182.198.209",username="root",password="T&Dfndpc#123")  
channel = ssh_client.invoke_shell()


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