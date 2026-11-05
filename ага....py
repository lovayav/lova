'''''''''
for n in range(10000,100000):
    a = [int(d) for d in str(n)]
    s1 = sum(x for x in a if x%2 == 0)
    s2 = sum(x for x in a if x%2!=0)
    m = max(a) + min(a)
    p1 = s1 + m
    p2 = s2 + m
    t = sorted([p1,p2])
    r = str(t[0]) + str(t[1])
    if int(r) == 812:
        print(n)
'''''''''
'''''''''
from itertools import*
k=0
for x in product('опачки', repeat = 5):
    s = ''.join(x)
    if s[0]  != 'о' and s[0]  != 'а' and s[0]  != 'и' and s[-1]!='п' and s[-1]!='ч' and s[-1]!='к'\
        and 'оо' not in s and 'аа' not in s and 'ии' not in s and 'пп' not in s and 'чч' not in s and 'кк' not in s:
        k+=1
print(k)
'''''''''
'''''''''
for x in range(1001):
    a = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    ans = []
    k = 0
    while a:
        if (a%7)%2!=0:
            k+=1
        a//=7
#print(k,x)
    if k>5:
        print(k,x)
'''''''''
'''''''''
f = [int(x) for x in open('17_29839.txt')]

mx = max([x for x in f if x%100 == 37])
print(mx)
ans = []
for i in range(len(f)-2):
    x,y,z = f[i],f[i+1],f[i+2]
    if ((100 <= abs(x) <= 999) + (100 <= abs(y) <= 999) + (100 <= abs(z) <= 999)) == 2:
        if ((x+y+z)/3)>0 and ((x+y+z)/3) < mx:
            ans.append(x+y+z)
print(len(ans),max(ans))
'''''''''
def f(a,b):
    if a > b: return 0
    if a == b: return 1
    else: return f(a+1,b)+f(a+7,b)+f(a*2,b)
print((f(7,20)*f(20,31)*f(31,40)) - (f(7,20)*f(20,40)) - (f(7,31)*f(31,40)))




























