# cook your dish here
t=int(input())
for i in range(t):
    n=list(map(int,input().split(' ')))
    n=sorted(n)
    print(n[1])
