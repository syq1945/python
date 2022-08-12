
#
# t=1,"123",[123,"abc"],("python","learn")    #元组是用圆括号括起来的，其中的元素之间用逗号隔开。（都是英文半角）
# print(t)
# print(t[2])
# print(t[2:])
# print(t[2][1])


# 一般认为,tuple有这类特点,并且也是它使用的情景:
# Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
# 如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
# Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
# Tuples 可以用在字符串格式化中。