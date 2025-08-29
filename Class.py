# Assignment 1: Design Your Own Class

class Device:   
    def __init__(self, brand):
        self.brand = brand
    
    def power_on(self):
        print(f"{self.brand} device is powering on...")

class Smartphone(Device):  
    def __init__(self, brand, model, storage):
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def take_photo(self):
        print(f"{self.brand} {self.model} took a photo!")

phone1 = Smartphone("Samsung", "Galaxy S24", "256GB")
phone1.power_on()
phone1.call("0712345678")
phone1.take_photo()
