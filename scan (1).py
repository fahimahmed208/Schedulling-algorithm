def Disk_scheduling(a,b):
    lower=[]
    upper=[]
    for i in b:
        if i < a :
            lower.append(i)
        else:
            upper.append(i)
    upper.sort()
    lower.sort(reverse=True)

    return (lower,upper)

Input = input("Enter the queue: ").split(" ")
head= int(input("Head start at: "))
Lower_bound= int(input("lower bound: "))
Upper_bound= int(input("upper bound: "))

print()

queue = [int(value) for value in Input]
L,U=Disk_scheduling(head,queue)

L.insert(0,head)
if Lower_bound != L[len(L)-1]:
    L.append(Lower_bound)

L.extend(U)
print("path: ", L)

previous_value=head
totalDistance=""
distance=0
for i in L:
    if i==head:
        continue
    if previous_value>int(i):
        totalDistance= totalDistance+'('+str(previous_value)+'-'+str(i)+')+'
        distance= distance +previous_value - i
    else:
        totalDistance= totalDistance+'('+str(i)+'-'+str(previous_value)+')+'
        distance= distance + i - previous_value
    previous_value=i

print()

print("Total distance: "+totalDistance[0:len(totalDistance)-1]) 
print('total head movement of = '+str(distance))