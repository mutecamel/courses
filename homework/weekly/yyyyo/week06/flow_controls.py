fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

message = "Hello"
for char in message:
    print(char)

person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key in person:
    print(key, person[key])

for i in range(5):
    print(i)

for i in range(3):
    for j in range(2):
        print(i, j)

count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())