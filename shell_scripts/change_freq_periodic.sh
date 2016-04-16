NAME[0]=3193000
NAME[1]=2660000
NAME[2]=1197000
TT=0
            
while true; do
  ./change.sh ${NAME[TT]}
  sleep 2
  TT=$((TT + 1))
  TT=$((TT%3))
done
