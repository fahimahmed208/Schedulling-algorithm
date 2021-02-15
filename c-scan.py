def Disk_scheduling(a,b):
    lower=[]
    upper=[]
    for i in b:
        if i < a:
            lower.append(i)
        else:
            upper.append(i)
    upper.sort()
    lower.sort()
    

    return (lower,upper)


Input= input("Enter the queue: ").split(" ")
head= int(input("Head start at: "))
Lower_bound= int(input("Lower bound: "))
Upper_bound= int(input("Upper bound: "))

print()

queue = [int(value) for value in Input]
L,U=Disk_scheduling(head,queue)


U.insert(0,head)
if Upper_bound != U[len(U)-1]:
    U.append(Upper_bound)

if L[0]!=Lower_bound:
    L.insert(0,Lower_bound)
U.extend(L)

print("path: ", U)

previous_value=head
totalDistance=""
distance=0
for i in U:
    if i==head:
        continue
    if previous_value>int(i):
        totalDistance= totalDistance+'('+str(previous_value)+'-'+str(i)+')+'
        distance= distance + previous_value - i
    else:
        totalDistance= totalDistance+'('+str(i)+'-'+str(previous_value)+')+'
        distance= distance + i - previous_value
    previous_value=i

print()

print("Total distance: "+totalDistance[0:len(totalDistance)-1]) 
print('Total head movement of = '+str(distance))