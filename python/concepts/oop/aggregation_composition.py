# Composition and aggregation

class Engine():

    def drive(self):
        return "Engine working!"


class Wheel():

    def drive(self):
        return "Wheels rolling!"

class Car():

    def __init__(self, engine, wheels = None, freshener):
        self.engine = engine
        self.freshener = freshener

        if wheels is None:
            self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
        else:
            self.wheels = wheels

    
    def drive(self):
        engine_status = self.engine.drive()

        wheels_status = [wheel.drive() for wheel in self.wheels]

        return f'{engine_status} and {" ".join(wheels_status)}'
    

engine = Engine()

car = Car(engine)

print(car.drive())