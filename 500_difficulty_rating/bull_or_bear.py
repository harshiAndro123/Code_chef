# cook your dish here
t=int(input())
for i in range(t):
    x,y=list(map(int,input().split(' ')))
    if x>y:
        print("LOSS")
    elif x<y:
        print("PROFIT")
    else:
        print("NEUTRAL")
