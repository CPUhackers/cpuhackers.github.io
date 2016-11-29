import psutil

def get_current_loads():
	return psutil.cpu_percent(interval=2, percpu=True)

def get_core_count():
	return psutil.cpu_count(logical=False)

def get_core_freqeuncies(core_number= 0):
	frequency_file = open("/sys/devices/system/cpu/cpu%s/cpufreq/scaling_available_frequencies" % str(core_number), "r")
	lines = frequency_file.read().split(' ')
	return lines

def max_load():
	return 100

def min_load() :
	return 0




