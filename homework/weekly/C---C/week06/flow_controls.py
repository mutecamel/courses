fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ",ok"
    print(fruit)

    s = "Python"
for char in s:
    print(char)

    for i in range(5):
        print(i)

person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key)

person = {"name": "Alice", "age": 30, "city": "New York"}
for value in person.values():
    print(value)

count = 1
while count <= 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
breakpoint()
while numbers:
    print(numbers.pop())

my_list = [10, 20, 30, 40]
while my_list:
    element = my_list.pop(0)
    print(element)
