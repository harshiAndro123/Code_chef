# cook your dish here
t=int(input())
for i in range(t):
    x,h=list(map(int,input().split(' ')))
    if x>=h:
        print("YES")
    else:
        print("NO")
