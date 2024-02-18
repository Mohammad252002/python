from random import randint as rnd
from random import shuffle

def mutation(population_list, n, ps, mr):
    chooosen_ones = list(range(ps,ps*2))
    shuffle (chooosen_ones)
    chooosen_ones = chooosen_ones[:int(ps*mr)]

    for i in chooosen_ones:
        cell = rnd(0, n-1)
        val = rnd(0, n-1)
        population_list[i][cell] = val
    return population_list
