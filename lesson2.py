import random

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 365
#         self.progress = 0
#         self.alive = True


#     def to_study(self):
#         print("Time to study")
#         self.progress += 0.12
#         self.gladness -= 5


#     def to_sleep(self):
#         print("I will sleep")
#         self.gladness += 3


#     def to_chill(self):
#         print("Rest time")
#         self.gladness += 5
#         self.progress -= 0.1


#     def is_alive(self):
#         if self.progress < -0.5:
#             print("Cast out…")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depression…")
#             self.alive = False
#         elif self.progress > 5:
#             print("Passed externally…")
#             self.alive = False




#     def end_of_day(self):
#         print(f"Gladness = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
                    
#     def live(self, day):
#         day = "Day" + str(day) + "of" +self.name + "life"
#         print(f"{day:=^365}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()

#         elif live_cube == 3:
#             self.to_chill()
#             self.end_of_day()
#             self.is_alive ()
# nick = Student(name="Nick")
# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)


# --------------------------------------------------------------------

class Cat:
    def __init__(self,name):
        self.name = name
        self.progress = 0
        self.alive = True

    def to_hunt(self):
        print("Time to hunt")
        self.progress -=0.25

    def to_sleep(self):
        print("I will sleep")
        self.progress += 3

    def eat_fish(self):
        print("Tuday is lucky day")
        self.progress += 5

    def run_away_the_dog(self):
        print("help me")
        self.progress -= 5

    def is_alive(self):
        if self.progress > -5:
            print("unlucky")
            self.alive == False
        elif self.progress >= 0:
            print("lucky")
            self.alive == True



    def end_of_day(self):
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^1}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_hunt()
        elif live_cube == 2:
            self.to_sleep()

        elif live_cube == 3:
            self.eat_fish()

        elif live_cube == 4:
            self.run_away_the_dog()
            self.end_of_day()
            self.is_alive ()
Рыжик= Cat(name = "Рыжик")
for day in range(10):
    if Рыжик.alive == False:
        break
    Рыжик.live(day)
  
