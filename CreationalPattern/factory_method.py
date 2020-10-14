# __future__库包含新版本的特性，在python2中用from __future__ import *, 就可以使用新版本的特性
# annotations是类型注解
from __future__ import annotations
# ABC类是抽象基类, ABC类有两个功能: 1.可以使用instance判定对象的类型; 2.强制子类必须实现某些方法
from abc import ABC, abstractmethod


# 抽象基类，Creator即相当于一个接口
class Creator(ABC):
    # 抽象方法，含有abstractmethod的类不能实例化，
    # 继承了含有abstractmethod方法的类的子类必须复写所有abstractmethod装饰的子类
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


class ConcreteProduct2(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
