# WAP for identity matrix
#
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

matSize = int(input("Enter the size of matrix: "))

for i in range(0, matSize):
    for j in range(0, matSize):
        if i == j:
            print("1", sep=' ', end=' ')
        else:
            print("0", sep=' ', end=' ')

    print()
