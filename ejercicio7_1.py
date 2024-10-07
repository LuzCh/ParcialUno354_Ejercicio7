import random
from deap import base, creator, tools

# Definir la función objetivo: f(x) = x^2
def eval_function(individual):
    x = individual[0]
    fitness_value = x ** 2
    return fitness_value,

# Configuración del algoritmo genético
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()
toolbox.register("attr_int", random.randint, 1, 10)  # Limitar el rango a [1, 10]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual, 30)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)  # Cambiar sigma para adaptarse al nuevo rango
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval_function)

# Proceso evolutivo
def evolve(population, generations=3):
    for gen in range(generations):
        print(f"\n-- Generación {gen + 1} --")
        print([ind[0] for ind in population])  # Mostrar los individuos antes de evolucionar
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < 0.5:
                toolbox.mate(child1, child2)
                del child1.fitness.values, child2.fitness.values

        for mutant in offspring:
            if random.random() < 0.2:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        for ind in invalid_ind:
            ind.fitness.values = toolbox.evaluate(ind)

        population[:] = offspring
        print([ind[0] for ind in population])  # Mostrar los individuos después de evolucionar

# Función principal
def main():
    population = toolbox.population()
    print("Población inicial:", [ind[0] for ind in population])

    for ind in population:
        ind.fitness.values = toolbox.evaluate(ind)

    evolve(population)

if __name__ == "__main__":
    main()
