import os
import requests
import time
import subprocess
import utils


current_loads = utils.get_current_loads()
max_load = utils.max_load()
min_load =utils.min_load()
avail_freqs = utils.get_core_freqeuncies()

def expected_set_frequencies():
	no_of_avail_freqs = len(avail_freqs)
	block_size = (max_load - min_load)/no_of_avail_freqs
	set_freq = []
	for load in current_loads:
		temp = min_load
		for freq in avail_freqs:
			if(temp <= load  <= temp + block_size) :
				set_freq.append(freq)
				break
			temp += block_size	

	return set_freq		

def set_frequencies(freqs):
	safe_temperature = utils.calculate_safe_temperature()
	

if __name__ == "__main__":
	freqs = expected_set_frequencies()
	set_frequencies(freqs)
	
