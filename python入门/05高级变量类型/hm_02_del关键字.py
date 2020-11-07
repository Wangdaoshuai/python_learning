name_list=["zhangsan","lisi","wangwu"]
# (知道)使用 del 关键字可以删除列表元素
#提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

#del 关键字本质上是将一个变量从内存中删除
name = "小米"
del name
#del后续的代码就不能再使用这个变量了
print(name_list)