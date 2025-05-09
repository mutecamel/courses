#创建一个Python包
"""
import my_package.my_module
import my_package.my_module2
my_package.my_module.info_print1()
my_package.my_module2.info_print2()
"""
"""
from my_package import my_module
from my_package import my_module2
my_module.info_print1()
my_module2.info_print2()
"""
#通过all变量，控制import*
from my_package import *
my_module.info_print1()
my_module2.info_print2()