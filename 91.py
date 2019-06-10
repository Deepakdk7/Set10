ax=list(map(int,input().split()))
l=ax[0]
b=ax[1]
h=ax[2]
a=2*l*b+2*l*h+2*h*b
b=l*b*h
print(a,b)
