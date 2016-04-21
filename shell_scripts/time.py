import datetime
import os

os.system("sudo cpufreq-set -c0 -g ondemand")
os.system("sudo cpufreq-set -c1 -g ondemand")
os.system("sudo cpufreq-set -c2 -g ondemand")
os.system("sudo cpufreq-set -c3 -g ondemand")

a = datetime.datetime.now()

os.system("./../lulesh2.0 -p")

b = datetime.datetime.now()
print(b-a)