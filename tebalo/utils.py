import psutil
import subprocess

def get_current_loads():
	return psutil.cpu_percent(interval=2, percpu=True)

def get_core_count():
	return psutil.cpu_count(logical=False)

def get_core_freqeuncies(core_number=0):
	frequency_file = open("/sys/devices/system/cpu/cpu%s/cpufreq/scaling_available_frequencies" % str(core_number), "r")
	lines = frequency_file.read().split(' ')
	return lines

def max_load():
	return 100

def min_load() :
	return 0

def get_core_temparature():
	temparature_list = []
	subprocess.call("./create_core_temp_file.sh", shell=True)
	temp1_file = open("core1.temp")
	line1 = temp1_file.read()
	temparature_list.append(line1[17:19])

	subprocess.call("./create_core_temp_file.sh", shell=True)
	temp2_file = open("core2.temp")
	line2 = temp2_file.read()
	temparature_list.append(line2[17:19])
	return temparature_list



