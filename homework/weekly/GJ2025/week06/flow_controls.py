fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit += ", ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(5):
    print(i)

person = {"name": "john", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}:{value}")

count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("No break occurred.")

x = 10
if x > 5:
    print("x is greater than 5")

x = 10
if x < 5:
    print("x is less than 5")
elif x < 15:
    print("x is less than 15")
else:
    print("x is greater than or equal to 15")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("No exception occurred.")
finally:
    print("This will always be executed.")

x = -1
if x < 0:
    raise ValueError("x cannot be negative")
