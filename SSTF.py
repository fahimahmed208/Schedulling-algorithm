f=[98,183,37,122,14,124,65,67]

n= int(input("Enter the Head of the Queue: "))

f.insert(0,n)

ln= len(f)


temp=0

nf=[]
a=[]

idx=0
c=f[idx]
print("Path : ",end=" ")
for i in range(ln):
    for j in range(ln):
        if f[j]==c:
            nf.append(9999)
            continue
        else:
            temp= f[j]-c
            if temp<0 :
                temp*=-1
            nf.append(temp)

    print(f[idx],end=' ')
    a.append(f[idx])
    f[idx]=9999
    idx= nf.index(min(nf))
    nf.clear()
    c=f[idx]


print()
sum=0

for i in range(ln-1):

    temp= a[i+1]-a[i]
    if temp<0 :
        temp*=-1
    sum+=temp
print("Total distance is: ",sum)