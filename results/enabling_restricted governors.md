**disable the current driver: add intel_pstate=disable to your kernel boot line**

To temporarily add a boot parameter to a kernel:

Start your system and wait for the GRUB menu to show (if you don't see a GRUB menu, press and hold the left Shift key right after starting the system).
Now highlight the kernel you want to use, and press the e key. You should be able to see and edit the commands associated with the highlighted kernel.
Go down to the line starting with linux and add your parameter foo=bar to its end. Now press Ctrl + x to boot.
 
 http://unix.stackexchange.com/questions/153693/cant-use-userspace-cpufreq-governor-and-set-cpu-frequency
 http://askubuntu.com/questions/19486/how-do-i-add-a-kernel-boot-parameter
 
