import os
import requests
import time
import subprocess

## get load
command = "mpstat -P %s " % "ALL"
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell = True,stderr=subprocess.PIPE)
out, error = p.communicate()
print out  

##get freq
#core 0

#command = "cat /proc/cpuinfo | grep  %s " % "cpu MHz"
command = "cat /proc/cpuinfo "

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell = True,stderr=subprocess.PIPE)
out, error = p.communicate()
print "freq of cores are : " + out 
