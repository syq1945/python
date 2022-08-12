#
# citys=["suzhou","tanshan","beijing","shanghai"]
# print(type(citys))
# city_codes=["0512","0315","011","012"]
# i=0
# while i <len(citys):
#     print("{}:{}".format(citys[i],city_codes[i]))
#     i=i+1


# mydict={}
# print(mydict)
# print(type(mydict))

'''
"name":"qiwsir"，有一个优雅的名字：键值对。
前面的name叫做键（key），后面的qiwsir是前面的键所对应的值(value)。
在一个dict中，键是唯一的，不能重复。
值则是对应于键，值可以重复。
键值之间用(:)英文的冒号，每一对键值之间用英文的逗号(,)隔开。
'''

# person={"name":"qiwsir", "site":"qiwsir.github.io","language":"python"}
# print(person)
# print(id(person))
# person["name2"]="qiwsir"
# print(person)
# print(id(person))


# name=(["first","Google"],["second","Yahoo"])
# website=dict(name)
# # print(website)
# print(id(website))
# website={}.fromkeys(("third","fourth"),"facebook")
# # print(website)
# print(id(website))
# print(website["third"])


city_codes={"suzhou":"0512","tangshan":"0315","beijing":"011","shanghai":"012"}
print(city_codes["suzhou"])
print(city_codes["tangshan"])
city_codes["tianjin"]="022"
print(city_codes)
print(len(city_codes))
city_codes["shanghai"]="999"    #字典的值可以改变
print(city_codes)
del city_codes["shanghai"]      #用del，将那一项都删掉。
print(city_codes)
print("tianjin" in city_codes)
print("shanghai" in city_codes)
print("022" in city_codes)       #值不能使用in 字典名
