echo > ""
while true; do
	sensors -u | grep " temp2_input:" >> log1.txt
	sleep 0.5
done