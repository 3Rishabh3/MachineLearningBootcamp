# WAP to calculate the Average of Numbers in a Given List.

listSize = int(input("Enter the size of list: "))
myList = []
totalSum = 0

for i in range(0, listSize):
    myNum = int(input("Enter the number: "))
    myList.append(myNum)

average = sum(myList)/listSize

print("Average of this list is: ", round(average, 3))

