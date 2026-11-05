#------1--------
from math import*
q0 = 2
p = 8
q = 0.15
ln = log(2)/p
for t in range(5,1000,5):
    Q = q0*exp(-ln*t)
    if Q <= q:
        print(t)
        break

#--------2---------
N = int(input())
for K in range(1,N+1):
    if K*K>N:
        print(K)
        break
    
#------3-------
n = int(input())
sm = 0
for i in range(1, n + 1):
    sm += 1 + (1/i**2)
print(sm)























