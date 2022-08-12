
# print(dir(list))


#
# # 列表是可以修改的。这种修改，不是复制一个新的，而是在原地进行修改。
# la=[1,2,3]
# print(la)
# print(id(la))
# lb=["qiwir","python"]
# print(lb)
# la.extend(lb)
# la.extend(["LM","GE"])   # 可以把数组中的所有成员加入到la中
# print(la)
# print(id(la))
# la.append(["Terry","Sun"])  # 可以把整个数组以一个元素的方式放在list 最后
# print(la)
# print(id(la))
# print(lb)


# lst=["python","qiwsir"]
# lst.extend("itdiffer")
# print(lst)
# lst.extend("8")    # extend 需要是list 类型, str也是list类型,  int 就不是了.
# print(lst)
# lst.extend(8)      # extend 需要是list 类型, str也是list类型,  int 就不是了.
# print(lst)


la=[1,2,1,1,3]
print(la.count(1))
la.append("a")
la.append("a")
print(la.count("a"))
print(la.count("a"))
print(la.count(10))
print(la.index(3))
print(la.index(1))
