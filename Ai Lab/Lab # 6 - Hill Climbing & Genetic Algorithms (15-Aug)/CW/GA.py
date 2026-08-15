import random

# Step 1: Create initial population
# [10, 0, 8, 29]

#population = [random.randint(0, 31) for _ in range(4)]
population = [10,0,8,29]

goal = 30

print("Initial population:", population)

generation = 0

# for generation in range(10):
while True:
    generation += 1

    # Step 2: Find best two numbers
    population.sort(reverse=True)
    parent1, parent2 = population[0], population[1]

    # Step 3: Crossover (mix bits)
    child = (parent1 & 0b111100) | (parent2 & 0b000011)

    # Step 4: Mutation (flip last bit randomly)
    if random.random() < 0.3:
        child ^= 1

    # Step 5: Replace worst number
    population[-1] = child

    print(f"Gen {generation}: {population}")

    # Stop if we find 31
    if goal in population:
        print("Solution found")
        break