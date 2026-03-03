# Writing to file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python File Handling Example.")

# Reading from file
with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)
