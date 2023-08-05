# WAP to check if a number is palindrome or not

number = int(input("Enter the number: "))

temp = number
reverse = 0

while number > 0:
    lastDigit = number % 10
    reverse = reverse*10 + lastDigit
    number = number // 10

if temp == reverse:
    print("Number is a palindrome number")
else:
    print("Number is NOT a palindrome number")
