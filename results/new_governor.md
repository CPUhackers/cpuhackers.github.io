The Governor Interface in the CPUfreq Core
=============================================

A new governor must register itself with the CPUfreq core using `cpufreq_register_governor`. The struct cpufreq_governor, which has to
be passed to that function, must contain the following values:

* governor->name -	    A unique name for this governor
* governor->governor -	    The governor callback function
* governor->owner	-	    .THIS_MODULE for the governor module (if appropriate)

The governor->governor callback is called with the current (or to-be-set) cpufreq_policy struct for that CPU, and an unsigned int event. The following events are currently defined:

* CPUFREQ_GOV_START:   This governor shall start its duty for the CPU policy->cpu
* CPUFREQ_GOV_STOP:    This governor shall end its duty for the CPU policy->cpu
* CPUFREQ_GOV_LIMITS:  The limits for CPU policy->cpu have changed to policy->min and policy->max.

If you need other `events` externally of your driver, _only_ use the cpufreq_governor_l(unsigned int cpu, unsigned int event) call to the
CPUfreq core to ensure proper locking.


The CPUfreq governor may call the CPU processor driver using one of these two functions:
```
int cpufreq_driver_target(struct cpufreq_policy *policy,
                                 unsigned int target_freq,
                                 unsigned int relation);

int __cpufreq_driver_target(struct cpufreq_policy *policy,
                                   unsigned int target_freq,
                                   unsigned int relation);
```
target_freq must be within policy->min and policy->max, of course. What's the difference between these two functions? When your governor
still is in a direct code path of a call to governor->governor, the per-CPU cpufreq lock is still held in the cpufreq core, and there's
no need to lock it again (in fact, this would cause a deadlock). So use __cpufreq_driver_target only in these cases. In all other cases 
(for example, when there's a `daemonized` function that wakes up  every second), use cpufreq_driver_target to lock the cpufreq per-CPU
lock before the command is passed to the cpufreq processor driver.
