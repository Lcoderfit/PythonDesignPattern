from __future__ import annotations
from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()


class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        print("num: 10")
        print("name: apples")


class Ship(Transport):
    def deliver(self):
        print("num: 20")
        print("name: banana")


class Solution:
    def main(self, transport_type):
        transport = None
        if transport_type == 'truck':
            transport = RoadLogistics()
        elif transport_type == 'ship':
            transport = SeaLogistics()
        if not transport:
            print("None transport")
        transport.plan_delivery()


if __name__ == '__main__':
    s = Solution()
    s.main("truck")
    s.main("ship")
