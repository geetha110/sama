# sama
num=int(input(""))
i=num
a=0
d=0
while(i!=0):
    k=i
    d=k%10
    a=a+pow(d,3)
    i=i//10    
if(num==a):
    print("yes")
else:
    print("no")
