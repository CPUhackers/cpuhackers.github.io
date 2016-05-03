(echo "./lulesh2.0 -s $1"; echo ./log_temperature.sh) | parallel
parallel ::: command1 command2