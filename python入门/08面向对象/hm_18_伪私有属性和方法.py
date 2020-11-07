class Women:

    def __init__(self, name):

        self.name = name
        # 不要问女生的年龄
        self.__age = 18

    def __secret(self):
        #在对象的方法内部，是可以访问对象的私有属性的
        print("我的年龄是 %d" % self.__age)


xiaofang = Women("小芳")
# 伪私有属性，外部不能直接访问
print(xiaofang._Women__age)

# 伪私有方法，外部不能直接调用
xiaofang._Women__secret()