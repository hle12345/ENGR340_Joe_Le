"""
Author: Prof. Alyssa
Description: Practicing inheritance and other OOP paradigms
student name: Joe Le (924366167)
"""

# Class defining a generic animal
class Animal:
    def __init__(self, name):
        self.name = name          # Stores the animal's name
        self.hungry = False       # Animal starts not hungry (default False)
        self.__healthy = True

        # Extra attribute (your choice)
        # energy represents how much energy the animal has (starts at 10)
        self.energy = 10

    def get_health(self):
        return self.__healthy

    # Print what the animal "says"
    def speak(self):
        print("Speaking! What do I say??")

    def sleep(self):
        print(f"{self.name} slept")
        self.hungry = True

    def eat(self, food):
        if self.hungry:
            print(f"{self.name} ate {food}!")
            self.hungry = False
            return True
        else:
            print(f"{self.name} did not eat {food}...")
            return False

    def play(self, minutes):
        print(f"{self.name} played for {minutes} minutes.")
        self.energy -= minutes

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.nest_location = None
    def fly(self):
        print("I can fly!")
    def speak(self):
        print("chirp chirp chirp")
    def check_health_in_bird(self):
        print(self.__healthy)
    def get_health_from_bird(self):
        return self.get_health()

class Fish(Animal):

    def __init__(self, name):
        super().__init__(name + "fish")

    def swim(self):
        print("Just keep swimming")

""" def run():
    # Initialize an animal
    an_animal = Animal("Alex")
    an_animal.sleep()
    an_animal.eat("carrot")

    a_bird = Bird("Big Bird")
    a_bird.fly()
    a_bird.sleep()
    
    a_bird.speak()
    print(a_bird.nest_location)"""

def run():
    #a_bird = Bird("Big Bird")
    #a_bird.check_health()
    #a_bird.check_health_in_bird()
    #print(a_bird.get_health())
    # print(a_bird.get_health_from_bird())
    a_fish = Fish("Nemo")
    print(a_fish.name)
    a_fish.swim()

    # This will cause error
    # a_fish.fly()

    a_fish.speak()

if __name__ == "__main__":
    run()