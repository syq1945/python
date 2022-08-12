# 内建函数id()可以查看每个对象的内存地址，即身份
''''
a,b,c=id(3),id(3.0),id(3.00)
# 显示3这个对象保存到哪个内存地址了
print(a)
print(b)
print(c)
'''
# 运行结果
r''' 
C:\Users\212618862\Anaconda3\python.exe "C:/Users/212618862/PycharmProjects/Excel Operation/Studay_Python_From_0/number.py"
2415041145200
2415050373552
2415050373552

Process finished with exit code 0
'''


# 对象有类型，变量无类型。
# 等同于标签的变量x没有类型之说，它不仅可以贴在整数类型的对象上，还能贴在其它类型的对象上，比如后面会介绍到的str（字符串）类型的对象等等。
'''x=5
print(x)
x=7
print(x)
x="Hello World!"
print(x)
'''

# 可以用一个命令：type(object)来检测一个数是什么类型。
'''
a=4+2
b=4.0+2
c=4.0+2.0
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
'''

