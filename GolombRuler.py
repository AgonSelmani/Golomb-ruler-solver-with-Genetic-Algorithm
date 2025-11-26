import random
import time


def create_individual(n, max_value):
    """Creates an individual with n unique sorted points"""
    individual = sorted(random.sample(range(max_value + 1), n))
    return individual

def is_valid_golomb(individual):
    """Checks if the individual is a valid Golomb Ruler"""
    distances = []
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            distance = abs(individual[i] - individual[j])
            if distance in distances:
                return False
            distances.append(distance)
    return True

def calculate_ruler_length(individual):
    """Calculates the total length of the ruler"""
    return individual[-1] - individual[0]

def fitness(individual):
    """Calculates fitness based on number of unique distances and total length"""
    distances = set()
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            distances.add(abs(individual[i] - individual[j]))
    
    total_possible_distances = len(individual) * (len(individual) - 1) // 2
    if len(distances) < total_possible_distances:
        return len(distances) - 1000  # Large penalty for invalid solutions
    
    # For valid Golomb Ruler, return negative length (we want to minimize)
    return -calculate_ruler_length(individual)

def tournament_selection(population, fitness_scores, tournament_size=3):
    """Tournament selection"""
    selected = []
    for _ in range(len(population)):
        contestants = random.sample(range(len(population)), tournament_size)
        winner = max(contestants, key=lambda i: fitness_scores[i])
        selected.append(population[winner])
    return selected

def crossover(p1, p2, max_value):
    """Performs crossover while maintaining correct number of unique points"""
    # Using single-point crossover
    cut = random.randint(1, len(p1) - 1)
    child = p1[:cut] + p2[cut:]
    
    # Ensure we have exactly n unique elements
    child = list(sorted(set(child)))
    
    # Adjust number of points if needed
    while len(child) < len(p1):
        # Find new unique values
        available = [x for x in range(max_value + 1) if x not in child]
        if not available:
            available = [x for x in range(max_value + 1, max_value + 100)]
        new_val = random.choice(available)
        child.append(new_val)
        child.sort()
    
    while len(child) > len(p1):
        # Remove a random point (avoiding endpoints)
        if len(child) > 2:
            remove_idx = random.randint(1, len(child) - 2)
            child.pop(remove_idx)
        else:
            break
    
    return child

def mutate(individual, max_value, mutation_strength=2):
    """Performs mutation while maintaining number of points and uniqueness"""
    mutated = individual.copy()
    
    for _ in range(mutation_strength):
        if random.random() < 0.7:  # 70% chance to modify an existing point
            idx = random.randint(0, len(mutated) - 1)
            current_val = mutated[idx]
            
            # Find possible new values
            neighbors = []
            if idx > 0:
                neighbors.append(mutated[idx - 1] + 1)
            if idx < len(mutated) - 1:
                neighbors.append(mutated[idx + 1] - 1)
            
            if neighbors:
                new_val = random.choice(neighbors)
                if new_val not in mutated:
                    mutated[idx] = new_val
        else:  # 30% chance to add/remove a point (maintaining count)
            if len(mutated) > 2 and random.random() < 0.5:
                remove_idx = random.randint(1, len(mutated) - 2)
                mutated.pop(remove_idx)
                
                # Add a new point
                available = [x for x in range(max_value + 1) if x not in mutated]
                if available:
                    new_val = random.choice(available)
                    mutated.append(new_val)
                    mutated.sort()
    
    return mutated

def calculate_population_diversity(population):
    """Calculates population diversity based on differences between individuals"""
    diversity = 0
    sample_size = min(10, len(population))
    sample_indices = random.sample(range(len(population)), sample_size)
    
    for i in sample_indices:
        for j in sample_indices:
            if i != j:
                # Calculate distance between individuals
                distance = sum(abs(a - b) for a, b in zip(population[i], population[j]))
                diversity += distance
    
    return diversity / (sample_size * (sample_size - 1))

def genetic_algorithm(n, population_size=50, max_generations=500, mutation_rate=0.2, 
                     optimal_length=None, max_time=300):
    """Improved genetic algorithm for Golomb Ruler"""
    
    start_time = time.time()
    max_value = n * 2  # Initial maximum value for points
    best_solution = None
    best_fitness = float('-inf')
    best_length = float('inf')
    
    # Create initial population
    population = [create_individual(n, max_value) for _ in range(population_size)]
    
    # Progress tracking
    improvement_history = []
    diversity_history = []
    
    # Adaptive stopping parameters
    no_improvement_streak = 0
    max_no_improvement = 50
    min_diversity = 1.0  # Minimum diversity threshold
    
    for generation in range(max_generations):
        # Check maximum time
        if time.time() - start_time > max_time:
            print(f"Stopping after {max_time} seconds")
            break
            
        # Evaluate fitness for each individual
        fitness_scores = [fitness(ind) for ind in population]
        
        # Find current best solution
        current_best_idx = max(range(population_size), key=lambda i: fitness_scores[i])
        current_best = population[current_best_idx]
        current_best_score = fitness_scores[current_best_idx]
        current_length = calculate_ruler_length(current_best)
        
        # Update global best solution
        if current_best_score > best_fitness:
            best_solution = current_best.copy()
            best_fitness = current_best_score
            best_length = current_length
            max_value = max(best_solution) * 2  # Adjust range based on best solution
            no_improvement_streak = 0
        else:
            no_improvement_streak += 1
        
        # Calculate diversity
        current_diversity = calculate_population_diversity(population)
        diversity_history.append(current_diversity)
        
        # Print progress
        if generation % 20 == 0 or generation == max_generations - 1:
            print(f"Generation {generation}: Best length {best_length} "
                  f"(Fitness: {-best_fitness:.1f}), Diversity: {current_diversity:.1f}")
            if is_valid_golomb(best_solution):
                print("   ✓ Valid Golomb Ruler solution")
        
        # Check stopping criteria
        if optimal_length is not None and best_length == optimal_length:
            print(f"Found optimal solution with length {optimal_length}!")
            break
            
        if no_improvement_streak >= max_no_improvement:
            print(f"Stopping after {max_no_improvement} generations without improvement")
            break
            
        if current_diversity < min_diversity:
            print(f"Stopping due to low diversity ({current_diversity:.2f})")
            break
        
        # Parent selection (tournament)
        parents = tournament_selection(population, fitness_scores)
        
        # Create offspring
        new_population = []
        for i in range(0, population_size, 2):
            p1, p2 = parents[i], parents[i+1]
            
            # Perform crossover
            child1 = crossover(p1, p2, max_value)
            child2 = crossover(p2, p1, max_value)
            
            # Perform mutation
            if random.random() < mutation_rate:
                child1 = mutate(child1, max_value)
            if random.random() < mutation_rate:
                child2 = mutate(child2, max_value)
            
            new_population.extend([child1, child2])
        
        # Elitism - keep best solution
        if best_solution is not None:
            new_population[0] = best_solution
        
        # Update population
        population = new_population[:population_size]
        
        # Adaptive parameter adjustment
        if no_improvement_streak > 20:
            mutation_rate = min(0.5, mutation_rate * 1.2)  # Increase mutation if no improvement
    
    return {
        'solution': best_solution,
        'length': best_length,
        'is_valid': is_valid_golomb(best_solution),
        'generations': generation + 1,
        'time_elapsed': time.time() - start_time,
        'improvement_history': improvement_history,
        'diversity_history': diversity_history
    }

# Known Golomb Ruler data (optimal lengths for different n)
KNOWN_OPTIMAL_LENGTHS = {
    1: 0, 2: 1, 3: 3, 4: 6, 5: 11, 6: 17, 7: 25, 8: 34, 9: 44, 10: 55,
    11: 72, 12: 85, 13: 106, 14: 127, 15: 151, 16: 177, 17: 199, 18: 216, 19: 246
}

# Algorithm testing
if __name__ == "__main__":
    print("Number of points on Golomb Ruler (e.g., 4, 5, 6... up to 19): ")
    n = int(input())  # Number of points on ruler
    optimal_length = KNOWN_OPTIMAL_LENGTHS.get(n)
    
    print(f"\nSearching for Golomb Ruler with {n} points (Known optimal length: {optimal_length})")
    
    result = genetic_algorithm(
        n=n,
        population_size=100,
        max_generations=100,
        mutation_rate=0.3,
        optimal_length=optimal_length,
        max_time=120  # 2 minutes maximum time
    )
    
    print("\nFinal Result:")
    print(f"Solution: {result['solution']}")
    print(f"Length: {result['length']}")
    print(f"Is valid: {'Yes' if result['is_valid'] else 'No'}")
    print(f"Generations executed: {result['generations']}")
    print(f"Execution time: {result['time_elapsed']:.2f} seconds")