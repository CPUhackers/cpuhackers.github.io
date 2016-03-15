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
