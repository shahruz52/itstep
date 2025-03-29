class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}")

class Charger:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print("Зарядка аккумулятора...")

class Autonomous:
    def __init__(self, sensors):
        self.sensors = sensors

    def navigate(self):
        print("Автоматическая навигация...")

class Autonomous_Charger_Vehicle(Vehicle, Charger, Autonomous):
    def __init__(self, brand, model, battery_capacity, sensors):
        Vehicle.__init__(self, brand, model)
        Charger.__init__(self, battery_capacity)
        Autonomous.__init__(self, sensors)

    def display_all_info(self):
        self.display_info()
        print(f"Емкость аккумулятора: {self.battery_capacity} кВт/ч")
        print(f"Датчики: {', '.join(self.sensors)}")

    def perform_actions(self):
        self.charge()
        self.navigate()


my_car = Autonomous_Charger_Vehicle(
    brand="Tesla",
    model="Model S",
    battery_capacity=100,
    sensors=["Лидар", "Камера", "Радар"])

my_car.display_all_info()
my_car.perform_actions()