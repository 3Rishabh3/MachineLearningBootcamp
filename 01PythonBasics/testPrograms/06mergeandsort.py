# WAP to merge two lists and sort it.

myList1 = []
myList2 = []

listSize1 = int(input("Enter the size of list 1: "))

for i in range(0, listSize1):
    element = int(input("Enter the element: "))
    myList1.append(element)

listSize2 = int(input("Enter the size of list 2: "))

for i in range(0, listSize2):
    element = int(input("Enter the element: "))
    myList2.append(element)

mergedList = myList1 + myList2;
mergedList.sort()

print("Merged list is: ", mergedList)
