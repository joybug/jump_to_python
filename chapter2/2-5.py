dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print(dic.keys())

print(list(dic.keys()))


print(dic)
dic['zip'] = "123-456"
print(dic)

print(dic.items())

del dic['name'], dic['phone']
print(dic)

dic.clear()
print(dic)

grade = {'pey': 10, 'julliet': 99}