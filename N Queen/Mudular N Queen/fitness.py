def fittness(population_list, n):
    lenth =len(population_list)
    for i in range(lenth):
        confilict = 0
       
        for j in range(n):
            for k in range(j+1,n):
                
                # column
                if population_list[i][j]==population_list[i][k]:
                    confilict+=1
                
                #diagnol
                if abs(j-k)==abs(population_list[i][j]-population_list[i][k]):
                    confilict+=1   

                    
        population_list[i][-1]=confilict
    return population_list