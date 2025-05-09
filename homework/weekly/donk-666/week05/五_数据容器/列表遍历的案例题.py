mylist=[1,2,3,4,5,6,7,8,9,10]
mylist2=[]
index=0
while index<len(mylist):
    if mylist[index]%2==0:
        mylist2.append(mylist[index])
    index+=1
print(mylist2)

mylist=[1,2,3,4,5,6,7,8,9,10]
mylist2=[]
for element in mylist:
    if element%2==0:
        mylist2.append(element)
print(mylist2)
