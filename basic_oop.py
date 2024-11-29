# Class - blueprint for creating objects - custom data type

# Camel case - eg. helloThere

class Car: # Pascal case - eg. HelloThere
    # Constructor - optional special method that sets up attributes of a new instance
    # will be called automatically when a new instance is created
    def __init__(self, make, model): # self is passed implicitly by the interpreter
        # create an attribute 'make' and copy the value of the 'make' parameter into it
        self.make = make # dot notation - <object>.<attribute/method>
        self.model = model
        # implicity returns self

    def start(self):
        print(f'{self.make} {self.model} started!')


# Main

my_car = Car('Ford', 'XR6') # create a new instance of Car
# my_car is now an object of class 'Car'
your_car = Car('Toyota', 'Landcruiser')
# print(my_car)
#print(your_car)
my_car.start()
your_car.start()
