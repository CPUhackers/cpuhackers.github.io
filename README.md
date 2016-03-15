

##How to change the CPU frequency?

###Installation

```
sudo apt-get install cpufrequtils
```

###Running

Save the below in a set_freq.sh file
```sh
sudo cpufreq-set -c0 -g userspace
sudo cpufreq-set -c1 -g userspace
sudo cpufreq-set -c2 -g userspace
sudo cpufreq-set -c3 -g userspace

sudo cpufreq-set -c0 -f $1GHz
sudo cpufreq-set -c1 -f $1GHz
sudo cpufreq-set -c2 -f $1GHz
sudo cpufreq-set -c3 -f $1GHz


cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq
cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq
cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq

```

Now execute 

```
chmod +x set_freq.sh
```

To change the frequncy exeucute the below command

```
./set_freq.sh 2.2
```

The available freqencies can be found by 

```
more cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
```

##Running Benchmarks

We used [Lulesh benchmark](https://codesign.llnl.gov/lulesh.php) for studying the change in temperature and execution time with change in frequency

##Results

| Frequency  | Temp Core 1 ℃ | Temp Core ℃ | Execution Time  in Seconds |
| ------------- |:-------------:| -----:| ----:|
| 1197000 | 35 | 37 | 79.65 |
| 2261000 | 39 | 43 | 40.34 |
| 2394000 | 39 | 43 | 39.49 |
| 2527000 | 41 | 44 | 37.05 |
| 2660000 | 43 | 45 | 35.52 |
| 2793000 | 43 | 45 | 34.26 |
| 2926000 | 43 | 46 | 33.70 |
| 3059000 | 44 | 47 | 32.27 |
| 3192000 | 45 | 48 | 30.74 |
| 3193000 | 45 | 50 | 31.15 |



### Frequency vs Tempararture Graph

![Temparature-Frequency](images/freq-temp.png) 

### Frequency vs Time Graph

![Time-Frequency](images/time-freq.png) 

##Temparature reading in HPC Computer

![Silp Temparature Reading](images/temparature-silp.png)

##How to read CPU voltage for 64 bit computer

```bash
 sudo apt-get install msr-tools
 sudo mdprobe msr
 sudo rdmsr 408 --bitfield 47:32 --decimal --processor 0
 ```
 
The value of register 408(x198) can be used to calculate the value of voltage. 
The value obtained from 32:47 bits on multiplying with (1 / 2^^13) gives the voltage.

##Comparison of Frequency Vs Voltage

|Max Frequency Max Voltage |Min Voltage |
|---------|-------------| ------- |
|1.2 GHz|0.86890 Volt|0.70386 Volt|
|1.4 GHz|0.86890 Volt|0.71838 Volt|
|1.6 GHz|0.86890 Volt|0.73291 Volt|
|1.8 GHz|0.86890 Volt|0.75232 Volt|
|2.0 GHz|0.87366 Volt|0.81055 Volt|
|2.2 GHz|0.87366 Volt|0.80579 Volt|
|2.4 GHz|0.90771 Volt|0.86890 Volt|


###Graph

![Freq vs Voltage](images/freqvsvol.png)

 





