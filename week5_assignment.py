# defining a class


class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = battery

    def phone_info(self):
        print(f"{self.brand} {self.model} {self.storage}GB storage.")

    def battery_status(self):
        print(f"Battery level: {self.__battery}%")

    def charge_battery(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"Charged battery now at {self.__battery}%")


# Inherited class
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, camera_quality, battery):
        super().__init__(brand, model, storage, battery)
        self.camera_quality = camera_quality

    def phone_info(self):
        print(
            f"{self.brand} {self.model} Pro with {self.storage}GB and {self.camera_quality}MP camera"
        )


# Create object
phone1 = Smartphone("Samsung", "A24", 128, 90)
phone2 = SmartphonePro("Apple", "iphone 16", 256, 48, 100)

# Demonstrate the functionability
phone1.phone_info()
phone1.battery_status()
phone1.charge_battery(50)

phone2.phone_info()
phone2.battery_status()
