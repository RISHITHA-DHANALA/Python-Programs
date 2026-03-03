num = int(input("Enter a number: "))
original = num
reversed_num = 0

while num != 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num //= 10

if original == reversed_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
