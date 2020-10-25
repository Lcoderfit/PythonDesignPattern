from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


class Builder(ABC):
    """用于创建产品对象的不同部分"""
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self._product = None
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    # 每次从外部调用ConcreteBuilder1.product都会创建一个新的Product1类型的对象
    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        # 单前导下划线，表示类内部使用的属性（但是外部仍可调用）
        self._builder = None

    # 修饰的方法名会转换为一个只读属性
    @property
    def builder(self) -> Builder:
        return self._builder

    # 为builder方法添加一个set方法，builder.setter中的builder需要与@property修饰的方法名一致
    # self._builder可以随便命名，不过一般为了规范，与setter装饰器修饰的函数名一致（只是多了个"_"前缀）
    # 在类外要设置self._builder属性的值，一般用：d = Director()    d.builder = Builder1()
    # d.builder中的builder要与setter修饰的方法名一致，（也可用d._builder，但不规范）
    # set方法的好处是，设置属性值时可以加上自己要想的限制条件，防止随意修改
    """如下，如果d.builder = A(), 但是A不为Builer对象的话，d.builder的值就为None
    @builder.setter
    def builder(self, builder):
        if not instance(builder, Builder):
            self.builder = None
        else:
            self.builder = builder
    """
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def builder_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def builder_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("最小化产品: ")
    director.builder_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("全功能产品：")
    director.builder_full_featured_product()
    builder.product.list_parts()
    print("\n")

    print("自定义产品：")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()

    print("自定义产品：")
    builder.produce_part_b()
    builder.produce_part_c()
    builder.product.list_parts()
