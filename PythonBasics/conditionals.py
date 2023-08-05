
billAmount = int(input("Enter the bill amount: "))

if billAmount < 500:
    discount = billAmount*0.05
    print("Discount amount is: ", discount)
else:
    discount = billAmount*0.10
    print("Discount amount is: ", discount)

print("Your final amount is: ", billAmount-discount)
