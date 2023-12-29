# _*_ utf-8 _*_
# @time: 2023/12/29
# @author: nj
# @file: 024_面向对象
# @project: python_basic2
# 创建类

class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.age = age
        self.name = name
        self.__weight = weight

    def speak(self):
        print("%s 说：我 %d 岁。" % (self.name, self.age))

    def getWeight(self):
        print("体重：%d" % self.__weight)

# 实例化某个对象
p = people('lily', 10, 30)
p.speak()
p.getWeight()

# 对象的继承
# 单继承示例 student 继承 people 对象
class student(people):
    grade = ''

    def __init__(self, name, age, weight, grade):
        people.__init__(self, name, age, weight)
        self.grade = grade

    # 覆写父类方法
    def speak(self):
        print("%s 说：我 %d 岁, 在读 %s 年级" % (self.name, self.age, self.grade))


stu = student('ken', 10, 60, 4)
stu.speak()
# 多继承 class DerivedClassName(Base1, Base2, Base3):


class speaker():
    topic = ''
    name = ''
    def __init__(self, topic, name):
        self.name = name
        self.topic = topic

    def speak(self):
        print("我叫：%s，我是一个演说家，我演讲的主题是：%s" % (self.name, self.topic))

# 多继承
class sample(speaker, student):
    a = ''

    def __init__(self, name, age, weight, grade, topic):
        student.__init__(self, name, age, weight, grade)
        speaker.__init__(self, topic, name)

test = sample('tom', 23, 60, 4, 'python')
print("多继承，覆写方法示例")
#方法名同，默认调用的是在括号中参数位置排前父类的方法，即调用spaker.speak()；如果是student放在前面，那么调用的是student.speak()
test.speak()   #方法名同，默认调用的是在括号中参数位置排前父类的方法

# 方法重写；父类的方法不满足子类的需求，可以在子类中重写父类的方法

class parent:
    def my_method(self):
        print("调用父类防范")

class child(parent):
    def my_method(self):
        print("调用子类方法")


c = child()
c.my_method()
# 使用super来强制调用父类的方法
super(child, c).my_method()




