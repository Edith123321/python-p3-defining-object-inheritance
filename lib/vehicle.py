class Vehicle:
    def __init__(self,  wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number= wheel_number
        print(f"{wheel_size}")

    def go(self ):
        return "vrrrrrrrooom!"
        
    def fill_up_tank(self):
        return "filling up!"

my_vehicle=Vehicle(48, 3)
my_vehicle.go()