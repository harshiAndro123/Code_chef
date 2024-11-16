# cook your dish here
t=int(input())
for i in range(t):
    x,y=list(map(int,input().split(' ')))
    if (y>=x):
        print("0")
    else:
        print(x-y)
