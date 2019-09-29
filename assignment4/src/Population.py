import random


class Population:
    def __init__(self):
        self.individuals = []

    def choose(self):
        sum = 0
        roll_list = []
        for i in range(len(self.individuals)):
            sum += self.individuals[i].fitness
            roll_list.append(sum)
        ran1 = random.uniform(0, sum)
        r_index = 0
        while ran1 > roll_list[r_index]:
            r_index += 1
        n1 = r_index
        ran2 = random.uniform(0, sum)
        r_index = 0
        while ran2 > roll_list[r_index]:
            r_index += 1
        n2 = r_index
        return n1, n2

    def getmaxfitness(self):
        max_ind = 0
        max_fit = self.individuals[max_ind].fitness
        for i in range(len(self.individuals)):
            if self.individuals[i].fitness > self.individuals[max_ind].fitness:
                max_ind = i
                max_fit = self.individuals[i].fitness
        return max_ind, max_fit
