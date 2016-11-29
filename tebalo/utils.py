import psutil

def get_current_load():
	return psutil.cpu_percent(interval=2, percpu=True)

def get_core_count():
	return psutil.cpu_count(logical=False)

def get_core_freqeuncies(core_number):
	frequency_file = open("/sys/devices/system/cpu/cpu%s/cpufreq/scaling_available_frequencies" % str(core_number), "r")
	lines = frequency_file.read().split(' ')



