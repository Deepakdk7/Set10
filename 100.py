ax=int(input())
s=1
while ax!=0:
    r=ax%10
    s=s*r
    ax=ax//10
print(s)
