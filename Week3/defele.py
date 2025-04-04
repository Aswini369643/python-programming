def printelements(elements):
    for i in range(len(elements)):
        print(elements[i],end='')
elements=[]
limit=int(input("enter the elements"))
for i in range(limit):
    ele=int(input())
    elements.append(ele)
printelements(elements)
