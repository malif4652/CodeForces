n= int(input())
z=0
for i in range(0,n):
    x=str(input())
    if x.count("1")>=2:
        z=z+1
print(z)