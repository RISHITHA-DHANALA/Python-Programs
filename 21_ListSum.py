n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

print("Sum of list elements =", sum(numbers))
