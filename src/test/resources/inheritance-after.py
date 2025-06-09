# Parent class 1
class Flyable:

    def fly(self):
        return "I can fly!"

# Parent class 2
class Swimmable:

    def swim(self):
        return "I can swim!"

# Child class inheriting from both Flyable and Swimmable
class Duck(Flyable, Swimmable):

    def speak(self):
        return "Quack!"

# Create an instance of Duck
donald = Duck()
# Demonstrate multiple inheritance
print(donald.speak())
print(donald.fly())
print(donald.swim())
