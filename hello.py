def hello():
    return 'Hello world!'

print(hello())

string = "C:/node/npm"

string1 = "kuma"
string2 = "maku"

print(string1 + string2)
print(string1, string2)
print(string)

print(string[0])

print(string[1:5])

# title() -- Cap the first letter of a string
# append() -- 增加element in array
# del -- 删除1st element in array
# pop() -- 最后的一个element in array
# remove('element')  -- 指定删除element
# upper()
# lower()
# strip() -- 去掉空格
# len() -- element number
# sort(reverse=True/False) -- Alphabet Asc order -- 返回原array
# reverse() -- 反转数组排序

# sorted() -- 产生新的array,不影响原array
# sorted(array, reverse=True)

array1 = ['a', 'b', 'c', 'd', 'e']
sorted(array1)
array1.sort(reverse=True)
print(array1)
