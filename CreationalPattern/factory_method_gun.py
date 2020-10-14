from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


class GunCreator(ABC):
    @abstractmethod
    def create_gun(self):
        pass

    @staticmethod
    def print_gun_info(gun):
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
    if gun_type == "ak47":
        gun = Ak47Creator()
    if gun_type == "musket":
        gun = MusketCreator()

    if not gun:
        return
    gun.print_gun_info(gun.create_gun())


if __name__ == "__main__":
    main("ak47")
    print()

    main("musket")
    print()
