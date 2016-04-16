import os
import requests
import time

for i in range(0,10):
	os.system("ls")

if not os.path.exists("sam"):
	os.system("mkdir sam")
else:
	print "path is already there"
	#os.system("vi sam.c")
	#os.system("mkdir sam")
	os.system("pwd")	

os.system("sudo cpufreq-set -c0 -g userspace")
os.system("sudo cpufreq-set -c1 -g userspace")
os.system("sudo cpufreq-set -c2 -g userspace")
os.system("sudo cpufreq-set -c3 -g userspace")

x = (input("Enter Low freq: "))
y = (input("Enter Mid freq: "))
z = (input("Enter High freq: "))


while 1:
	os.system("sudo cpufreq-set -c0 -f " + str(x) + "GHz")
	os.system("sudo cpufreq-set -c1 -f " + str(x) + "GHz")
	os.system("sudo cpufreq-set -c2 -f " + str(x) + "GHz")
	os.system("sudo cpufreq-set -c3 -f " + str(x) + "GHz")

	os.system("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
	time.sleep(5)
	os.system("sudo cpufreq-set -c0 -f " + str(y) + "GHz")
	os.system("sudo cpufreq-set -c1 -f " + str(y) + "GHz")
	os.system("sudo cpufreq-set -c2 -f " + str(y) + "GHz")
	os.system("sudo cpufreq-set -c3 -f " + str(y) + "GHz")

	os.system("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
	time.sleep(5)
	os.system("sudo cpufreq-set -c0 -f " + str(z) + "GHz")
	os.system("sudo cpufreq-set -c1 -f " + str(z) + "GHz")
	os.system("sudo cpufreq-set -c2 -f " + str(z) + "GHz")
	os.system("sudo cpufreq-set -c3 -f " + str(z) + "GHz")

	os.system("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
	time.sleep(5)
	

os.system("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")