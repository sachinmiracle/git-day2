# Simple Python Program

def greet(name):
    return f"Hello, {name}! Welcome to Python."

# User input
name = input("Enter your name: Sachin mirkale")

# Call function
message = greet(name)
print(message)

# Loop example
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# List example
fruits = ["Apple", "Banana", "Orange"]

print("\nFruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Dictionary example
student = {
    "name": name,
    "age": 25,
    "country": "Germany"
}

print("\nStudent Information:")
for key, value in student.items():
    print(f"{key}: {value}")
