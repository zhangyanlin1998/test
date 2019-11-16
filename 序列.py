列表的创建
# 基本语法[]的创建
a=[10,20,'ll']
a=[]
# list() 使用list()可以将任何迭代的数据转化成列表
b=list()
b=list(range(10))
print(b)
a=list("aaa")
print(a)
a=list(range(1,15,3))
print(a)'''
'''列表元素 增加和删除'''# 一般在列表尾部增加和删除
# append()方法
# 尾部增加新元素
a=[20,40]
a.append(60)
print(a)
# +运算符操作 不是真正尾部加元素二十创建新的列表对象
# extends() 原地操作 将目标列表的所有元素添加到本列表尾部 不创建新对象
a=[20,40]
print(id(a))
a.extend([500])
print(id(a))
