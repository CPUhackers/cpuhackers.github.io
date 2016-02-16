

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

We used [Lulesh benchmark](https://codesign.llnl.gov/lulesh.php) for studying the change in temparature and execution time with change in frequency

##Results







