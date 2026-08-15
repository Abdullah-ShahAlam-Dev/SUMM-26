import random

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D', 'E'],
    'B': ['F', 'G'],
    'C': ['H', 'I'],
    'G': ['J', 'K'],
    'I': ['L', 'M'],
    'K': ['N', 'O']
}

heuristic = {
    'S': 12, 'A': 9, 'B': 11,
    'C': 8, 'D': 9, 'E': 7, 'F': 9, 'G': 9,
    'H': 6, 'I': 5, 'J': 7, 'K': 6,
    'L': 2, 'M': 0, 'N': 4, 'O': 4
}

# Genetic Algorithm Parameters
POPULATION_SIZE = 10
GENERATIONS = 20
MUTATION_RATE = 0.2
CHROMOSOME_LENGTH = 4 # Graph ki maximum depth 4 hai

def get_path(chromosome):
    """Chromosome ke choices ko use karke graph mein path banata hai"""
    current = 'S'
    path = [current]
    for choice in chromosome:
        neighbors = graph.get(current, [])
        if not neighbors:
            break
        # Choice ke hisaab se neighbor select karna
        next_node = neighbors[choice % len(neighbors)]
        path.append(next_node)
        current = next_node
    return path

def fitness(chromosome):
    """Path ke aakhri node ki heuristic value return karta hai (Lower is better)"""
    path = get_path(chromosome)
    return heuristic[path[-1]]

def genetic_algorithm():
    # Initial population create karna (Random paths)
    population = [[random.randint(0, 2) for _ in range(CHROMOSOME_LENGTH)] for _ in range(POPULATION_SIZE)]

    for gen in range(GENERATIONS):
        # Population ko fitness ki base par sort karna (Kam heuristic wala pehle)
        population.sort(key=fitness)

        # Agar goal node 'M' (heuristic 0) mil jaye toh stop kar do
        if fitness(population[0]) == 0:
            break

        # Elitism: Top 2 best parents ko next generation mein direct copy karna
        next_generation = population[:2]

        # Baqi ki generation create karna
        while len(next_generation) < POPULATION_SIZE:
            # Top half population mein se 2 random parents select karna
            p1 = random.choice(population[:POPULATION_SIZE//2])
            p2 = random.choice(population[:POPULATION_SIZE//2])

            # Crossover (Dono parents ko half se mila dena)
            split = 2
            child = p1[:split] + p2[split:]

            # Mutation (Randomly kisi aik choice ko change karna)
            if random.random() < MUTATION_RATE:
                mutate_index = random.randint(0, 3)
                child[mutate_index] = random.randint(0, 2)

            next_generation.append(child)

        population = next_generation

    # Best result ko print karna
    population.sort(key=fitness)
    best_path = get_path(population[0])
    print("Genetic Algorithm Path Found:", best_path)

# Function ko call karna
genetic_algorithm()