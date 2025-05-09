# myjob.py
from mylib import (
    func1,
    func2,
    func3,
    func4,
    func5,
    func6,
    func7,
    func8,
    func9,
    func10,
    func11,
    func12,
)


def main():
    # func1
    func1()

    # func2
    result = func2()
    print(f"func2返回: {result}")

    # func3
    print("\nfunc3测试:")
    func3("位置实参")  # 位置实参
    func3(param="命名实参")  # 命名实参
    try:
        func3()  # 不传实参 (会报错)
    except TypeError as e:
        print(f"预期错误: {e}")

    # func4
    print("\nfunc4测试:")
    func4("位置实参")  # 位置实参
    func4(param="命名实参")  # 命名实参
    func4()  # 不传实参 (取默认值)

    # func5
    print("\nfunc5测试:")
    func5(1, 2)  # 只传位置参数
    func5(1, 2, named1="命名1")  # 位置+命名
    func5(1, 2, named2="命名2", named1="命名1")  # 位置+命名(顺序不同)

    # func6
    print("\nfunc6测试:")
    func6(1, 2)  # 只能位置传参
    try:
        func6(1, pos2=2)  # 尝试命名传参 (会报错)
    except TypeError as e:
        print(f"预期错误: {e}")

    # func7
    print("\nfunc7测试:")
    func7(named1="a", named2="b")  # 只能命名传参
    try:
        func7("a", "b")  # 尝试位置传参 (会报错)
    except TypeError as e:
        print(f"预期错误: {e}")

    # func8
    print("\nfunc8测试:")
    func8(1, 2, 3, 4)  # 任意数量位置参数

    # func9
    print("\nfunc9测试:")
    func9(a=1, b=2, c=3)  # 任意数量命名参数

    # func10
    print("\nfunc10测试:")
    args = (1, 2)
    func10(*args, named1="命名")  # 解包位置参数

    # func11
    print("\nfunc11测试:")
    kwargs = {"named1": "a", "named2": "b", "named3": "c"}
    func11(**kwargs)  # 解包命名参数

    # func12
    print("\nfunc12测试:")
    result = func12(42, "字符串")
    print(f"func12返回: {result}")
    print(func12.__doc__)  # 打印文档字符串


if __name__ == "__main__":
    main()
