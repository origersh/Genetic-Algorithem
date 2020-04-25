from random import randint, uniform

class Brain:
    def __init__(self, size):
        self.directions = []
        self.step = 0
        self.size = size
        self.randomize()
    def randomize(self):
        for i in range(self.size):
            self.directions.append((randint(-1, 1), randint(-1, 1)))
    def clone(self):
        c = Brain(self.size)
        for i in range(c.size):
            c.directions[i] = self.directions[i]
        return c
    def mutate(self):
        mutationRate = 0.01
        for i in range(self.size):
            rand = uniform(0.0,1.0)
            if rand < mutationRate:
                self.directions[i] = (randint(-1, 1), randint(-1, 1))