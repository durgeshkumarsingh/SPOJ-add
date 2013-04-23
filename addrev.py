import math
T=int(raw_input())
for i in range(0,T):
    x,y=raw_input().split(" ")
    z=str(int(x[::-1])+int(y[::-1]))
    print str(z[::-1]).lstrip('0')
    
