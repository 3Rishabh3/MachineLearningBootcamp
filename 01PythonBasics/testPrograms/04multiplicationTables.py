# WAP to print multiplication tables of a given number
#
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15

number = int(input("Enter the number fot the multiplication table: "))

for i in range(1, 11):
    print(number, " x ", i, " = ", number*i)
