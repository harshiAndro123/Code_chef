# cook your dish here
t=int(input())
for i in range(t):
    x,y=list(map(int,input().split(' ')))
    print(int((x/10)*y))
