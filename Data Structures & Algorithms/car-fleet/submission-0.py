class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        Fleets = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if not Fleets or time > Fleets[-1]:
                Fleets.append(time)

        return len(Fleets)


        