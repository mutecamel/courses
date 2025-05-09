#定义函数，进行文档说明
def add(x,y):
    """
    add函数可以接受两个参数可以进行两数相加的功能
    :param x:x表示相加的一个数字
    :param y:y表示相加的另一个数字
    :return:返回值是两数相加的结果
    """
    result=x+y
    print(f"两数相加的结果是：{result}")
    return result
add(5,6)
