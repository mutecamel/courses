# 创建字典
# 使用花括号创建字典
student = {"name": "Alice", "age": 20, "major": "Computer Science"}

# 使用 dict() 函数创建字典
employee = dict(name="Bob", age=30, department="HR")

# 通过键访问值
print(student["name"])  # 输出: Alice

# 使用 get() 方法访问值
print(student.get("age"))  # 输出: 20
print(student.get("gender", "Unknown"))  # 输出: Unknown

# 修改和添加元素
# 修改已存在的值
student["age"] = 21
print(student)  # 输出: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}

# 添加新的键值对
student["city"] = "New York"
print(
    student
)  # 输出: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'city': 'New York'}
