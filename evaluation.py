import random
import heapq

# Function to initialize the grid environment with obstacles and dirt
def initialize_environment(X, Y, num_obstacles, num_dirty_cells, seed=None):
    if seed:
        random.seed(seed)
    
    grid = [['_' for _ in range(Y)] for _ in range(X)]
    
    # Randomly place obstacles
    obstacles = set()
    while len(obstacles) < num_obstacles:
        obstacle_pos = (random.randint(0, X-1), random.randint(0, Y-1))
        if grid[obstacle_pos[0]][obstacle_pos[1]] == '_':
            grid[obstacle_pos[0]][obstacle_pos[1]] = 'O'
            obstacles.add(obstacle_pos)
    
    # Randomly place dirty cells
    dirty_cells = set()
    while len(dirty_cells) < num_dirty_cells:
        dirty_pos = (random.randint(0, X-1), random.randint(0, Y-1))
        if grid[dirty_pos[0]][dirty_pos[1]] == '_':
            grid[dirty_pos[0]][dirty_pos[1]] = 'D'
            dirty_cells.add(dirty_pos)

    # Randomly place the vacuum cleaner in a non-obstacle, non-dirty cell
    vacuum_position = None
    max_attempts = 1000  # Prevent infinite loops in case of small grids
    attempts = 0
    while not vacuum_position and attempts < max_attempts:
        vac_pos = (random.randint(0, X-1), random.randint(0, Y-1))
        if grid[vac_pos[0]][vac_pos[1]] == '_':
            grid[vac_pos[0]][vac_pos[1]] = 'V'
            vacuum_position = vac_pos
        attempts += 1
    
    if not vacuum_position:
        raise ValueError("Could not find a valid position for the vacuum.")

    return grid, vacuum_position, dirty_cells

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

# Placeholder for random movement cleaning (should be implemented)
def random_movement_cleaning(grid, vacuum_position, dirty_cells):
    print("Random movement cleaning is not yet implemented.")

# Placeholder for A* cleaning (should be implemented)
def a_star_cleaning(grid, vacuum_position, dirty_cells):
    print("A* search cleaning is not yet implemented.")

# Define a function to evaluate the random movement strategy
def evaluate_random_movement(X, Y, num_obstacles, num_dirty_cells, seed=None):
    print(f"Random Movement Strategy: Grid {X}x{Y} with {num_obstacles} obstacles and {num_dirty_cells} dirty cells\n")
    
    # Initialize the environment
    grid, vacuum_position, dirty_cells = initialize_environment(X, Y, num_obstacles, num_dirty_cells, seed=seed)
    
    # Print initial grid
    print("Initial Grid:")
    print_grid(grid)
    
    # Perform random movement cleaning
    random_movement_cleaning(grid, vacuum_position, dirty_cells)

# Define a function to evaluate the A* search strategy
def evaluate_a_star(X, Y, num_obstacles, num_dirty_cells, seed=None):
    print(f"A* Search Strategy: Grid {X}x{Y} with {num_obstacles} obstacles and {num_dirty_cells}\n")
    
    # Initialize the environment
    grid, vacuum_position, dirty_cells = initialize_environment(X, Y, num_obstacles, num_dirty_cells, seed=seed)
    
    # Print initial grid
    print("Initial Grid:")
    print_grid(grid)
    
    # Perform A* cleaning
    a_star_cleaning(grid, vacuum_position, dirty_cells)

# Run the evaluation scenarios
if __name__ == "__main__":
    seed_value = 42  # Set seed for reproducibility
    
    # Small world evaluation (5x5 and 10x10)
    print("Evaluating Small Worlds...\n")
    evaluate_random_movement(5, 5, num_obstacles=3, num_dirty_cells=4, seed=seed_value)
    evaluate_random_movement(10, 10, num_obstacles=5, num_dirty_cells=8, seed=seed_value)
    
    evaluate_a_star(5, 5, num_obstacles=3, num_dirty_cells=4, seed=seed_value)
    evaluate_a_star(10, 10, num_obstacles=5, num_dirty_cells=8, seed=seed_value)
    
    # Large world evaluation (50x50 and 100x100)
    print("\nEvaluating Large Worlds...\n")
    evaluate_random_movement(50, 50, num_obstacles=30, num_dirty_cells=40, seed=seed_value)
    evaluate_random_movement(100, 100, num_obstacles=40, num_dirty_cells=50, seed=seed_value)
    
    evaluate_a_star(50, 50, num_obstacles=30, num_dirty_cells=40, seed=seed_value)
    evaluate_a_star(100, 100, num_obstacles=40, num_dirty_cells=50, seed=seed_value)
