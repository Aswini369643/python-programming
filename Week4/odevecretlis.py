def evenindexsum(l):
    evensum=0
    for i in range(len(l)):
           if i % 2 ==0:
                  evensum+=l[i]
    return evensum
    
def oddindexsum(l):
    oddsum=1
    for i in range(len(l)):
            if i % 1 ==1:
                oddsum+=[i]
    

def createlist(l,rangeofl):
        for i in range(rangeofl):
            temp=int(input("enter the elements"))
            l.append(temp)
        return l
        
        
l1=[]
l2=[]
l3=[]
rangeofl1=int(input("enter first range"))
rangeofl2=int(input("enter second range"))
rangeofl3=int(input("enter third range"))

l1=createlist(l1,rangeofl1)
print(l1)
l2=createlist(l2,rangeofl2)
print(l2)
l3=createlist(l3,rangeofl3)
print(l3)        
        
        
    







