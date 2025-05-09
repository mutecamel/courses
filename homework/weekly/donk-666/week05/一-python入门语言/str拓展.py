# string可以用三种类型
# 使用单引号定义法，使用单引号包围
name='黑马程序员'
print(type(name))
#双引号定义
name="黑马程序员"
print(type(name))
name="""
我是
黑马
程序员
"""
print(type(name))

#在string包含双引号
name='"黑马程序员"'
print(name)
#在string里包含单引号
name="'黑马程序员'"
print(name)
#使用转义字符,\解除引号的效用
name="\"黑马程序员\""
print(name)
