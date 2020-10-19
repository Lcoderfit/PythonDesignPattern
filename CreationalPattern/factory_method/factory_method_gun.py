from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


"""
注：在Java中，抽象类中包含方法和属性，而接口里全部都是抽象方法，不包含属性
Python可以通过抽象类来实现接口
"""


class GunCreator(ABC):
    @abstractmethod
    def create_gun(self):
        pass

    def print_gun_info(self):
        gun = self.create_gun()
        print(gun.get_name())
        print(gun.get_power())


class Ak47Creator(GunCreator):
    def create_gun(self):
        return Ak47()


class MusketCreator(GunCreator):
    def create_gun(self):
        return Musket()


class Gun(ABC):
    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def power(self):
        pass


class Ak47(Gun):
    # 1.修改方法，使方法名可以想属性一样被访问，如果在外部像用函数的方式调用反而会报错
    # 例：a = Ak47()  a.name()是错的，而a.name是正确的
    # 2.修饰的方法名会转换为只读属性，无法修改
    @property
    def name(self):
        return "Ak47 gun"

    @property
    def power(self):
        return 5


class Musket(Gun):
    @property
    def name(self):
        return "Musket gun"

    @property
    def power(self):
        return 1


def main(gun_type):
    gun = None
    # 返回Ak47Creator类，然后调用print_gun_info方法，
    # 该方法内部会调用Ak47Creator中的create_gun方法，返回一个具体的产品类型Ak47，
    # 然后再在print_gun_info内部用创建的Ak47类的对象调用get_name和get_power
    if gun_type == "ak47":
        gun = Ak47Creator()
    if gun_type == "musket":
        gun = MusketCreator()

    if not gun:
        return
    gun.print_gun_info()


if __name__ == "__main__":
    main("ak47")
    print()

    main("musket")
    print()
