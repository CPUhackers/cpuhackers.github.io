echo -n "" > log1.txt
echo -n "" > log2.txt
while true; do
	sensors  | grep "Core 0" >> log1.txt
	sensors  | grep "Core 2" >> log2.txt
	sleep 0.2
done