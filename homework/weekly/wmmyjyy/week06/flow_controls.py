fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    fruit = fruit + ", ok"
    print(fruit)

word = "Python"
for char in word:
    print(char)

for i in range(5):
    print(i)

for i in range(3):
    for j in range(2):
        print(i, j)

person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, ":", person[key])

count = 0
while count < 5:
    print(count)
    count = count + 1

fruits = ["apple", "banana", "cherry"]
while fruits:
    print(fruits.pop())
