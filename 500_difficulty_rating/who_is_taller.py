# cook your dish here
n=int(input())
for i in range(n):
    x,y=list(map(int,input().split(' ')))
    if x>y:
        print("A")
    else:
        print("B")
