print('.......Example-1.........')
class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object directly.

print('.......Example-2.........')
'''The maxspeed can be modified from inside Car class'''
class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive() # still prints 200 as variable was private

print('...........Example3.........')
class Car:
    __maxspeed = 0
    __name     =""
    def __init__(self):
        self.__maxspeed=200
        self.__name="Arin"
    def drive(self):
        print('driving max speed '+str(self.__maxspeed))
    '''setter method to set value from outisde'''
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

redcar = Car()
redcar.drive()
'''calling setter method which will update private variable'''
redcar.setMaxSpeed(290)
redcar.drive()