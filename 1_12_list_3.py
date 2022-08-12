# # list.insert(i, x)中的i是将元素x插入到list中的位置，即将x插入到索引值是i的元素前面。注意，索引是从0开始的。
# all_user=["qiwsir","github","io"]
# print(all_user)
# all_user.insert(0,"python")
# print(all_user)
# all_user.insert(3,"http://")
# print(all_user)
# lenth=len(all_user)
# all_user.insert(lenth, "SQL")
# print(all_user)


# all_user=['python', 'http://', 'qiwsir', 'github', 'io', 'algorithm']
# all_user.remove("http://")
# print(all_user)
# # all_user.remove("QQ")
# # print(all_user)
# all_user.remove("python")
# print(all_user)

# all_users =['python', 'qiwsir', 'github', 'io', 'algorithm']
# print(all_users)
# a=input("请输入要删除的word:")
# if a in all_users:
#     all_users.remove(a)
#     print(all_users)
# else:
#     print(a, "不在all_user中")


# all_users =['python', 'qiwsir', 'github', 'io', 'algorithm']
# print(all_users)
# a=int(input("请输入您想删除对象的index:"))
# all_users.pop(a)
# print(all_users)



# a=[1,2,3,4,5,6]
# a.reverse()       #没有返回值
# print(a)
# a.__reversed__()  # 有返回值
# print(a)

# a=[6,4,8,3,1]
# a.sort()
# print(a)


# all_users =['python', 'qiwsir', 'github', 'io', 'algorithm']
# all_users.sort(key=len)
# print(all_users)


