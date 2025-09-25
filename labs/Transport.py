from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name: str, speed: int, capacity: int):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self, distance: int) -> float:
        pass
    # returns travel time in hours

    @abstractmethod
    def fuel_consumption(self, distance: int) -> float:
        pass
    # returns fuel/energy consumption
        
    @abstractmethod
    def info(self) -> str:
        pass
    # returns transport description

    def calculate_cost(self, distance: int, price_per_unit: float) -> float:
        return self.fuel_consumption(distance) * price_per_unit
    # calculates the total travel cost


class Car(Transport):
    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        return distance * 0.07

    def info(self) -> str:
        return f"Car: {self.name}, speed: {self.speed} km/h, capacity: {self.capacity}"


class Bus(Transport):
    def __init__(self, name: str, speed: int, capacity: int, passengers: int):
        super().__init__(name, speed, capacity)
        self.passengers = passengers

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        if self.passengers > self.capacity:
            print("Overloaded!")
            return 0
        return distance * 0.15

    def info(self) -> str:
        return f"Bus: {self.name}, speed: {self.speed} km/h, passengers: {self.passengers}/{self.capacity}"


class Bicycle(Transport):
    def __init__(self, name: str, capacity: int = 1):
        super().__init__(name, speed=20, capacity=capacity)

    def move(self, distance: int) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: int) -> float:
        return 0.0

    def info(self) -> str:
        return f"Bicycle: {self.name}, speed: {self.speed} km/h"


class ElectricCar(Car):
    def fuel_consumption(self, distance: int) -> float:
        return 0.0

    def battery_usage(self, distance: int) -> float:
        return distance * 0.2

    def calculate_cost(self, distance: int, price_per_unit: float) -> float:
        return self.battery_usage(distance) * price_per_unit

    def info(self) -> str:
        return f"Electric Car: {self.name}, speed: {self.speed} km/h, capacity: {self.capacity}"


if __name__ == "__main__":
    transports = [
        Car("BMW M3", 120, 5),
        Bus("Bogdan", 80, 45, passengers=25),
        Bicycle("Ukraine"),
        ElectricCar("Tesla X", 120, 7)
    ]

    distance = 100
    price_per_unit = 45.0  

    for t in transports:
        print("===")
        print(t.info())
        print(f"Travel time for {distance} km: {t.move(distance):.2f} hours")
        print(f"Fuel/Energy consumption: {t.fuel_consumption(distance):.2f}")
        print(f"Travel cost: {t.calculate_cost(distance, price_per_unit):.2f} UAH")
