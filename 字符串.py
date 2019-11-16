import time
import io
#字符串切片slice 快速截取子字符串
a='acskkjggv'
print(a[0])
# 结果：a
print(a[1:5:2]) #【起始偏移量：终止偏移量;步长】
#结果：ck
#使用负数操作
print(a[-3:])       #倒数3个
#结果：ggv
print(a[-5:-3])     #从倒数第五到倒数第三 包头不包尾
#结果;kj'''
'''split()分割和join()合并
b=" to be or not to be"
print(b.split())    #不指定分隔符默认使用空白字符
print(b.split("to"))
time01 = time.time()
li = []
for i in range(1000000):
    li.append("yll")
a="".join(li)
time02 =time.time()
print("运算时间："+str(time02-time01))
#字符串驻留机制与字符串的比较
    python对于符合标识符规则的字符串（下划线、字母、数字会启动字符串驻留机制）
a="axc_55"
b="axc_55"
print(a is b)
#字符串常用方法汇总
# 常用查找方法
a='我爱北京天安门，天安门上太阳升，伟大领袖毛主席，指引我们向前进'
print(len(a))    # 字符串长度
print(a.startswith("我爱北京"))    # 以指定字符串开头
print(a.endswith("前进"))     # 以指定字符串结尾
print(a.find("我"))     # 第一次出现字符串的位置
print(a.rfind("我"))   # 最后一次出现字符串的位置
print(a.count("我"))   # 字符串共出现几次
print(a.isalnum())   # 是否全是字母或数字
# 去除首位信息
# strip()去除字符串首尾指定信息，lstrip()去除左边的指定信息
print(" xxx ".strip())
print(" x*x*x*".strip("*"))
print("*xxxx*".lstrip("*"))
print("*xxx*".rstrip("*"))
#  大小写转换
c="wo ai beijing tiananmen weida lingx MZX"
print(c.capitalize())   # 产生新字符串首字母大写
print(c.title())   # 每个单词首字母大写
print(c.upper())   # 所有全部大写
print(c.lower())  # 全部小写
print(c.swapcase())   # 大小写转换
# 格式排版
d="YLL"
print(d.center(10,"8"))   # 10个字符其余用*代替居中
print(d.ljust(10,"*"))   # 10个字符其余用*代替左靠拢
# 其他方法
print(d.isalnum())  # 是否为字母或数字
print(d.isalpha())  # 是否只由字母组成含汉字
print(d.isdigit())  # 是否只由数字
print(d.isspace())  # 是否为空白符'''
'''字符串的格式化
# format() {}为占位符
a="名字叫做:{0},年龄是：{1}"
print(a.format("岩琳琳",25))
b="名字叫做:{name},年龄是：{age}"
print(b.format(name='雯雯',age=18))
# 填充与对其
#  ^,<,>表示居中 左对齐，右对齐
# ：后表示要填充的字符
a="我是{0}，我喜欢数字{1:*^8}"
print(a.format("岩林",666))
# 数字格式化
# 浮点数通过f 整数d
a="我是{0}，存款有{1:.2f}"   # 小数点后两位
print(a.format("岩林林",1555.2555))
print("{:0>10d}".format(2))  # 记得加引号
#可变字符串
s="hello,world"
sio=io.StringIO(s)
print(sio)
print(sio.getvalue())
sio.seek(7)
sio.write("h")
print(sio.getvalue())
