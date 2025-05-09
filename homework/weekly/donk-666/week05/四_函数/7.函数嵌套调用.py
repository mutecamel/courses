#定义函数fun_b
def fun_b():
    print("....2....")

#定义函数fun_a
def fun_a():
    print("....1....")
    fun_b()
    print(".....3....")
fun_a()