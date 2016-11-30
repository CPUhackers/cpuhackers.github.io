import psutil
import subprocess
import os
from subprocess import Popen, PIPE

def get_current_loads():
	return psutil.cpu_percent(interval=2, percpu=True)

def get_core_count():
	return psutil.cpu_count(logical=False)

def get_core_count_logical():
	return psutil.cpu_count()

def get_core_freqeuncies(core_number=0):
	frequency_file = open("/sys/devices/system/cpu/cpu%s/cpufreq/scaling_available_frequencies" % str(core_number), "r")
	lines = frequency_file.read().split(' ')
	return lines

def max_load():
	return 100

def min_load() :
	return 0


# return list of temparature
def get_core_temparature():
	temparature_list = []
	output = subprocess.Popen(["./create_core_temp_file.sh"], stdout=subprocess.PIPE).communicate()[0]
	lines = output.split("\n")
	temparature_list.append(lines[0][17:19])
	temparature_list.append(lines[1][17:19])

	return temparature_list

# return list of max temparatures
def get_max_temparatures():
	
	max_temparature_core_1 = 0
	max_temparature_core_2 = 0
	
	for i in range(0, get_core_count_logical(																																								)):
		command = "sudo cpufreq-set -c%s -g performance" % i
		os.system(command)

	for i in range(1, 1000):
		max_temparature_core_1 = max(max_temparature_core_1, get_core_temparature()[0])
		max_temparature_core_2 = max(max_temparature_core_2, get_core_temparature()[1])
	
	max_temparatures = []
	max_temparatures.append(int(max_temparature_core_1))
	max_temparatures.append(int(max_temparature_core_2))
	
	return max_temparatures

def calculate_safe_temperature():
	return max(get_max_temparatures()) - 2


def set_core_frequency(core_no, frequency):
	command = "sudo cpufreq-set -c%s -f %s" % (core_no, frequency)
	os.system(command)

def get_current_frequency(core_no):
	frequency_file = open("/sys/devices/system/cpu/cpu%s/cpufreq/scaling_cur_freq" % str(core_no), "r")
	return frequency_file.read().split("\n")[0]



print calculate_safe_temperature()

