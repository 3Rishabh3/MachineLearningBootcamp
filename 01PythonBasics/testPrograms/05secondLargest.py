# WAP to find second-largest number in a list

listSize = int(input("Enter the size of list: "))
myList = []

for i in range(0, listSize):
    element = int(input("Enter the element: "))
    myList.append(element)

myList.sort()
print("Second largest element is: ", myList[listSize-2])
