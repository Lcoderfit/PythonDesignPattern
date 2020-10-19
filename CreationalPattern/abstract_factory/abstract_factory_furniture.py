from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def count_legs(self) -> None:
        pass

    @abstractmethod
    def sit_on(self) -> None:
        pass


class Chair(AbstractProductA):
    def count_legs(self) -> int:
        return 4

    def sit_on(self) -> str:
        return "Sit on place 1"


class Sofa(AbstractProductA):
    def count_legs(self) -> int:
        return 8

    def sit_on(self) -> str:
        return "sit on place 2"


class CoffeeTable(AbstractProductA):
    def count_legs(self) -> int:
        return 6

    def sit_on(self) -> str:
        return "sit on place 3"


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_coffee_table(self):
        pass


class ArtDecoFactory(AbstractFactory):
    def create_chair(self):
        return