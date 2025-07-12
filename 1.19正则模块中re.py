#正则方法
import re
st="hello 你好 world 世界"

#中文匹配
li=re.findall("[\u4e00-\u9fa5]",st)
print()

#sub替换方法(需要替换的元素（规则），新元素，目标，个数）如果全部替换可省去，个数
li=re.sub("[a-zA-Z]","6",st,5)
print()

#split切割方法(切割规则，字符串（目标））
li=re.split("[a-zA-Z]",st)
print()
li=re.split("[\u4e00-\u9fa5]",st)
print()

#findall 匹配所有符合要求的数据 反馈列表
#search 匹配字符串内第一个符合要求的数据 返回的是对象
li=re.search("[\u4e00-\u9fa5]",st)
print()
#match 匹配开头符合要求的数据 返回的是对象 符合要求的数据必须在开头
li=re.match("[\u4e00-\u9fa5]",st)
print()

#print(li.span())获取匹配到的元素下标
#print(li.group())获取匹配到的元素内容



