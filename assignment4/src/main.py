import random
from Map import Map
from Individual import Individual
from Population import Population

map = Map('us_states_51_ij.txt')
len_map = len(map.states)
num_p = 100
p_tran = 0.7
p_mu = 0.3
p0 = Population()
for i in range(num_p):
    ind = Individual(map)
    for j in range(len(ind.colors)):
        ind.colors[j] = random.randint(0, 3)
    ind.updatefitness()
    p0.individuals.append(ind)
k, fk = p0.getmaxfitness()

time = 0
while fk < 1 and time < 100000:
    p1 = Population()
    while len(p1.individuals) < num_p:
        n1, n2 = p0.choose()
        ind_tran = random.randint(0, len_map - 1)
        ran_tran = random.uniform(0, 1)
        ran_mu1 = random.uniform(0, 1)
        ran_mu2 = random.uniform(0, 1)
        ind_n1 = Individual(map)
        ind_n1.colors = list(p0.individuals[n1].colors)
        ind_n2 = Individual(map)
        ind_n2.colors = list(p0.individuals[n2].colors)
        if ran_tran < p_tran:
            t = ind_n1.colors[ind_tran]
            ind_n1.colors[ind_tran] = ind_n2.colors[ind_tran]
            ind_n2.colors[ind_tran] = t
        if ran_mu1 < p_mu:
            ind_n1.mutate()
        ind_n1.updatefitness()
        if ran_mu2 < p_mu:
            ind_n2.mutate()
        ind_n2.updatefitness()
        p1.individuals.append(ind_n1)
        p1.individuals.append(ind_n2)
    p0 = p1
    k, fk = p0.getmaxfitness()
    if time % 20 == 0:
        print('Step:', time, ' Fitness:', fk)
    time += 1
print('Step:', time, ' Fitness:', fk)

f = open('colors.txt', 'w')
ppp = str(p0.individuals[k].colors)
f.writelines(ppp)
f.close()

p0.individuals[k].textprint()
p0.individuals[k].picprint()
