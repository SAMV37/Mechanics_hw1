class IntersectionController:

    def __init__(self):
        self.intersectionWidthRange = (5, 21)
        self.yellowLightDurationRange = (2, 6)
        self.width = 0
        self.yellowLightDuration = 0

    def get_variables_defined_random(self):
        self.width = randrange(*self.intersectionWidthRange)
        self.yellowLightDuration = randrange(*self.yellowLightDurationRange)


class DecisionController:
    
    def __init__(self):
        self.initialSpeed = 0
        self.accelerationPos = 0
        self.accelerationNeg = 0
        self.allDistance = 0
        self.distance = 0
        self.yellowLightDuration = 0

    def make_decision(self, car, intersection):
        self.initialSpeed = car.initialSpeed
        self.accelerationPos = car.accelerationPos
        self.accelerationNeg = car.accelerationNeg
        carDistance = car.initDistance
        self.distance = carDistance
        intersectionWidth = intersection.width
        self.allDistance = carDistance + intersectionWidth
        self.yellowLightDuration = intersection.yellowLightDuration
        suggestion = self.calculate_decision()
        return suggestion

    def calculate_time_needed_accelerating(self, acceleration):
        time = ((-1*self.initialSpeed) + (math.sqrt((pow(self.initialSpeed, 2) + 2 * acceleration * self.allDistance)))) / acceleration
        return time

    def calculate_time_needed_decelerating(self, acceleration):
        time = (self.initialSpeed - (math.sqrt((pow(self.initialSpeed, 2) - 2 * acceleration * self.distance)))) / acceleration
        return time

    def calculate_decision(self):
        timeNeeded = self.calculate_time_needed_accelerating(self.accelerationPos)
        timeNeededDec = self.calculate_time_needed_decelerating(self.accelerationNeg)

        if timeNeeded < self.yellowLightDuration:
            if timeNeededDec > self.yellowLightDuration:
                return "Please Accelerate"
            else:
                return "Accelerate or Decelerate"
        elif time_needed_dec < self.yellow_light_duration:
            return "Please Decelerate"
        else:
            return "Not accelerate nor decelerate"




class CarController:

    def __init__(self):
        self.initSpeedRange = (20, 81)
        self.initDistanceRange = (10, 150)
        self.accelerating = True
        self.accelerationPosRange = (1, 4)
        self.accelerationNegRange = (1, 4)
        self.initSpeed = 0
        self.initDistance = 0
        self.accelerationPos = 0
        self.accelerationNeg = 0


    def get_variables_defined_random(self):
        self.initSpeed = randrange(*self.initSpeedRange)
        self.initDistance = randrange(*self.initDistanceRange)
        self.accelerationPos = randrange(*self.accelerationPosRange)
        self.accelerationNeg = randrange(*self.accelerationNegRange)
        self.initSpeed = randrange(*self.initSpeedRange)

class MainControl:

    def __init__(self):
        # Create Car
        self.car = CarController()
        self.intersection = IntersectionController()
        self.decision_controller = DecisionController()

    # @staticmethod
    def define_variables(self):
        self.car.get_variables_defined_random()
        self.intersection.get_variables_defined_random()

    def make_decision(self):
        return self.decision_controller.make_decision(car=self.car, intersection=self.intersection)


if __name__ == "__main__":
    control = MainControl()
    control.define_variables()
    decision = control.make_decision()
    print(decision)

