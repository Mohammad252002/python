from parameters import *
from initial_population import init_population
from cross_over import cross_over
from mutation import mutation
from fitness import fittness
from presentation_function import show

current_population = init_population(N,PS)
current_population = fittness(current_population,N )
current_population = sorted(current_population, key=lambda x:x[-1])
if current_population[0][-1]==0:
        print("Solution was found in the initial population stage:" ,current_population[0] )
        show(current_population[0],N)
else:
    for i in range(EPOCH):
        current_population = cross_over(current_population, N, PS)
        current_population = mutation(current_population, N, PS, MR)
        current_population = fittness(current_population,N )
        current_population = sorted(current_population, key=lambda x:x[-1])
        current_population = current_population[:PS]
        if current_population[0][-1]==0:
            print(i+1,"Solution Found:" ,current_population[0] )
            show(current_population[0],N)
            break
        else:
            print(i+1,"Best solution so far:" ,current_population[0] )


    else:
        print("Sorry, we could not find you a solution")
        show(current_population[0],N)        