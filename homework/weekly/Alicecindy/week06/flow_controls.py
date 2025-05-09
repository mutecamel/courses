fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    fruit +=", ok"
    print(fruit)

message = "Hello"
for char in message:
    print(char)

for i in range(5):
    print(i)

person = {'name':'John', 'age':30, 'city':'New York'}
for key, value in person.items():
    print(f"{key}:{value}")

count = 0
while count < 5:
    print(count)
    count = count + 1

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())