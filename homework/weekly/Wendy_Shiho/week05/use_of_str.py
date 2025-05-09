print("列名")
s = "group"
print(s)
print(isinstance(s, str))
assert type(s) is str

print("f-string")
x = "red velvet"
s = f"name:{x}"
print(s)

name = "Wendy"
age = 31
# 使用 f-string 格式化字符串
message = f"My name is {name} and I'm {age} years old."
print(message)

pi = 3.1415926
formatted_pi = f"Pi is approximately {pi:.2f}"
print(formatted_pi)  # 保留两位小数
# 在花括号里嵌套
numbers = [1, 2, 3, 4, 5]
message = f"The sum of {', '.join(str(num) for num in numbers)} is {sum(numbers)}."
print(message)

s = "-"
s = s * 10
print(s * 20)

s = "aespa"
u = s.upper()
print(u)

t = "name:{}，age {}"
t1 = t.format("Wendy", "31")
print(t1)

a = "red "
b = "velvet"
c = a + b
assert c == "red velvet"
print(c)

try:
    print(a - b)
except TypeError as e:
    print(e)

print("abc" > "ABC")

a = "book"
print(iter(a))

for c in a:
    print(c)

print(ord("o"))
print(a.capitalize())
print(a.count("oo"))

print("0base1".isalnum())

q = ["it", "pops", "like", "candy"]
print("*".join(q))

print(" song ha ".strip())
print(" song ha ".rstrip())

a = "love is cosmic"
print(a.split(" "))

assert a.partition(" ") == ("love", " ", "is cosmic")
