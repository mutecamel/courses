#多态：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
#多态常用来作用在继承关系上：以父类做声明定义，以子类做实际工作，用以获得同一行为不同状态
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def make_noise(animal:Animal):
    animal.speak()
dog=Dog()
cat=Cat()
make_noise(dog)
make_noise(cat)

#演示的抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_l_r(self):
        """左右摆风"""
        pass

class Media(AC):
    def cool_wind(self):
        """制冷"""
        print("美的空调制热")
    def hot_wind(self):
        """制热"""
        print("美的空调制冷")
    def swing_l_r(self):
        """左右摆风"""
        print("美的空调左右摆风")
class Gree(AC):
    def cool_wind(self):
        """制冷"""
        print("格力空调制热")
    def hot_wind(self):
        """制热"""
        print("格力空调制冷")
    def swing_l_r(self):
        """左右摆风"""
        print("格力空调左右摆风")
def make_cool(ac:AC):
    ac.cool_wind()

media_ac=Media()
gree_ac=Gree()

make_cool(media_ac)
make_cool(gree_ac)

