import random
n=random.randint(0,10)
count=5
while(count>0):
           x=int(input("Enter the number"))
           if(x>n):
              print("too low")
           elif(x<n):
                print("too low")
           else:
                print("congrats")
                break
           count-=1
 print("you lost")
          
