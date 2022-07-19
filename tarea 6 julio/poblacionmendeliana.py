#FUNCIÓN 1. de creación de una población con alelos al azar

import scipy # for random numbers

def build_population(N, p):
    """The population consists of N individuals.Each individual has two chromosomes, containing
    allele "A" or "a", with probability p or 1-p, respectively.The population is a list of tuples.
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population
    
    
    
# FUNCIÓN 2. Conteo de pares de alelos
def compute_frequencies(population):
    """ Count the genotypes.Returns a dictionary of genotypic frequencies."""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})
    
    
    
# FUNCIÓN 3. Creación de nueva población

def reproduce_population(population):
    """ Create new generation through reproduction. For each of N new offspring:
    - choose the parents at random, 
    - the offspring receives a chromosome from each of the parents.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation