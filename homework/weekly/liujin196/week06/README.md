# mypkg 包说明

这是一个简单的 Python 包 `mypkg`，用于展示如何创建和使用自定义模块。

## 包含模块

- `mypkg.mylib`：包含以下函数：
  - `func1()`：返回模块中 func1 的说明字符串
  - `func2()`：返回模块中 func2 的说明字符串
  - `func3()`：返回 `1 + 2 + 3` 的结果（整数）

## 使用方法

安装包后，在代码中可以这样导入和使用：

```python
from mypkg.mylib import func1, func2, func3

print(func1())
print(func2())
print(func3())
