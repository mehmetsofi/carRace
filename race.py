import random
class car:
    def __init__(self,  name, speed):
        self.speed = speed
        self.name = name
    def get_name(self):
        return self.name
    def get_speed(self):
        return self.speed
    def drive(self, distance):
        time_taken = distance / self.speed
        return time_taken

class track:

    def __init__(self, name):
        self.friction = 1.0
        self.name = name
        self.cars = []
    def get_name(self):
        return self.name
    def set_weather(self, weather):
        if weather == "sun":
            self.friction = 1.0
        elif weather == "rain":
            self.friction = 0.6
        elif weather == "fog":
            self.friction = 0.8
        elif weather == "ice storms":
            self.friction = 0.1
        elif weather == "solar storm":
            self.friction = 1.1
        elif weather == "fire tornado":
            self.friction = 10.0
        else:
            self.friction = 1.0
    def add_car(self, car):
        self.cars.append(car)
    def race(self, distance):
        car_won = self.cars[0]
        ref_time = self.cars[0].drive(distance)
        for car in self.cars:
            print(car.get_name() + " completed race in " + str(car.drive(distance)))
            if car.drive(distance) < ref_time : 
                ref_time = car.drive(distance)
                car_won = car
        print("Winner!! -->" + car_won.get_name())
            
track1 = track("Daniel")
track1.set_weather("fire tornado")
cars_list_race = []
for i in range(1000):
   cars_list_race.append(car("Car nº"+str(i),random.randint(50,80)))
for car in cars_list_race:
    track1.add_car(car)
    print(car.get_name() + " with speed set to : "+ str(car.get_speed()))
 
print("RACE NOW!")
track1.race(10000)
