
def pr(a):
    print(a, id(a))

# a=5
# b=a
# print(a, id(a))
# print(b, id(b))
# pr(a)
# pr(b)


# ab={"name":"qiwsir", "lang":"python"}
# cd=ab
# pr(ab)
# pr(cd)
#
# ef=ab.copy()
# pr(ef)
#
# ef["name"]="itdiffer.com"
# pr(ef)
# pr(ab)


# x={"name":"qiwsir","lang":["python","java","c"]}
# y=x.copy()
# pr(x)
# pr(y)
# y["lang"].remove("c")
# pr(y)
# pr(x)
# x.clear()
# pr(x)
# pr(y)


d={"lang":"python"}
pr(d.get("lan"))
pr(d.get("lang"))
# pr(d.["lan"])

