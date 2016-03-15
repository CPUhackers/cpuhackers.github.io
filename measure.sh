while :
do
	X1="$(cpufreq-info -f -c 0)"
	X2="$(sudo rdmsr 408 --bitfield 47:32 --decimal --processor 0)"
	echo $X1 " " $X2
done
