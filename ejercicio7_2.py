import random

def eval_function(individual):
    return (individual[0] ** (2*individual[0])) -1

# Inicializar 30 individuos (números naturales positivos)
def init_population(size):
    return [[random.randint(1, 100)] for _ in range(size)]

# Seleccionar los mejores individuos (por torneo)
def select(population, k=3):
    return [max(random.sample(population, k), key=eval_function) for _ in range(len(population))]

# Cruce: combinar dos individuos (simple suma en este caso)
def mate(ind1, ind2):
    return [(ind1[0] + ind2[0]) // 2]

# Mutación: aumentar o disminuir el número aleatoriamente
def mutate(ind, prob=0.1):
    if random.random() < prob:
        ind[0] += random.randint(-10, 10)
        ind[0] = max(1, ind[0])  

def evolve(population, generations=3):
    for gen in range(generations):
        print(f"\n-- Generación {gen + 1} --")
        print("Individuos antes de la evolución:", population)
        
        # Selección
        offspring = select(population)
        
        # Cruce
        for i in range(0, len(offspring), 2):
            if i + 1 < len(offspring):
                offspring[i] = mate(offspring[i], offspring[i + 1])
        
        # Mutación
        for ind in offspring:
            mutate(ind)
        
        # Actualizar la población
        population[:] = offspring
        
        print("Individuos después de la evolución:", population)

# Función principal
def main():
    population = init_population(30)
    
    print("Población inicial:")
    print(population)
    
    # Ejecutar el algoritmo evolutivo
    evolve(population)
    
    print("\nPoblación final:")
    print(population)

if __name__ == "__main__":
    main()
