num = int(input("Enter a number: "))
original = num
result = 0
n = len(str(num))

while num != 0:
    remainder = num % 10
    result += remainder ** n
    num //= 10

if result == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
