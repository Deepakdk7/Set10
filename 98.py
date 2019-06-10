ax=int(input())
l=list(map(int,input().split()))
for i in range(ax):
    if(l[i+1]!=l[i]+1):
        print(i+1)
        break
