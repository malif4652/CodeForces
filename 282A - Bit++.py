a=int(input())
n=[input().lower() for i in range(a)]
x=0
for i in range(a):
    if n[i]=="++x" or n[i]=="x++":
        x+=1
    else:
        x-=1
print(x)