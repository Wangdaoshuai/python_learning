xiaoming_dict = {"name": "小明",
                 "age": 18,
                 "phone":"1212"}
#迭代遍历字典
#变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print("%s - %s"%(k,xiaoming_dict[k]))