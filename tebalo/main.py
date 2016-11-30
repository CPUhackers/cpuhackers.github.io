import os
import requests
import time
import subprocess
import utils


max_load = utils.max_load()
min_load = utils.min_load()
avail_freqs = utils.get_core_freqeuncies()
core_count = utils.get_core_count()

def expected_set_frequencies():
	no_of_avail_freqs = len(avail_freqs)
	block_size = (max_load - min_load)/no_of_avail_freqs
	set_freq = []
	current_loads = utils.get_current_loads()
	for load in current_loads:
		temp = min_load
		for freq in avail_freqs:
			if(temp <= load  <= temp + block_size) :
				set_freq.append(freq)
				break
			temp += block_size	

	return set_freq		

def current_temperature(core):
	return utils.get_core_temparature()[core]

def reduce_level(freq):
	
    no_of_avail_freqs = len(avail_freqs)	

    if freq == avail_freqs[no_of_avail_freqs-1]:
    	return freq

    for i in range(1,no_of_avail_freqs) :
    	if freq == avail_freqs[i] :
    		return avail_freqs[i+1]

    #never comes here		
    return avail_freqs[no_of_avail_freqs/2]			

def set_frequencies(freqs):
	safe_temperature = utils.calculate_safe_temperature()

	while True:
		freqs = expected_set_frequencies()
		for i in range(0,core_count) :
			freq = freqs[i]
			if current_temperature(i) <= safe_temperature :
				set_core_frequency(i,freq)	
			else :
				curr_freq = utils.get_current_frequency(i)
				previous_level_freq = reduce_level(curr_freq)
				print i 
				print  "th core freq: " + curr_freq+ " hey: " + previous_level_freq
		    	utils.set_core_frequency(i,previous_level_freq)	
		time.sleep(2)    	

if __name__ == "__main__":
	freqs = expected_set_frequencies()
	set_frequencies(freqs)
	
