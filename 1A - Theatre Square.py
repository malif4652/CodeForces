import math

m,n,a = [int(i) for i in input().split()]
print(math.ceil(m/a)*math.ceil(n/a))