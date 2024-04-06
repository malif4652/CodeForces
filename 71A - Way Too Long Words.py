n=int(input())
if n>=1 and n<=100:
    for i in range(0, n):
        x=str(input())
        print(f"{x[0]}{len(x)-2}{x[len(x)-1]}") if len(x)>10 else print(x)