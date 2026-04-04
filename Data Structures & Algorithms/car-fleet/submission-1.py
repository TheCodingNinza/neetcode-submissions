class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        
        for i in range(len(position)):
            cars.append(Car(position[i], speed[i]))
            
        sortedCars = sorted(cars, key=lambda x: x.position, reverse=True)
        
        times = []
        
        for car in sortedCars:
            times.append((target-car.position) / car.speed)

        ans = 1
        nextTime = times[0]

        for i in range(1, len(times)):
            if times[i] > nextTime:
                nextTime = times[i]
                ans += 1


        return ans    



class Car:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

    def __repr__(self):
        return f"Car(positon={self.position}, speed={self.speed})";    