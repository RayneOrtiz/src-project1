import random

# Function to create the grid environment
def create_grid(x, y, seed=None):
    # Define the possible states for each cell: Dirty (D), Clean (_), and Obstacle (O)
    cell_states = ['D', '_', 'O']
    
    # Set a seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Create the grid and randomly assign states
    grid = [[random.choice(cell_states) for _ in range(x)] for _ in range(y)]
    
    return grid

# Function to place the vacuum cleaner on a random clean cell
def place_vacuum(grid):
    # Find all clean cells that are not obstacles
    clean_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == '_']
    
    # Randomly choose a clean cell for the vacuum cleaner
    vacuum_position = random.choice(clean_cells)
    
    # Place the vacuum in the grid (represented by 'V')
    grid[vacuum_position[0]][vacuum_position[1]] = 'V'
    
    return vacuum_position, grid

# Manhattan distance function
def manhattan_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

# Function to find the closest dirty cell
def find_closest_dirty_cell(vacuum_position, grid):
    dirty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 'D']
    
    # Find the closest dirty cell using Manhattan Distance
    closest_cell = None
    min_distance = float('inf')
    
    for dirty_cell in dirty_cells:
        distance = manhattan_distance(vacuum_position, dirty_cell)
        if distance < min_distance:
            min_distance = distance
            closest_cell = dirty_cell
    
    return closest_cell, min_distance

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# Main setup
def initialize_environment(x, y, seed=None):
    # Create the grid environment
    grid = create_grid(x, y, seed)
    
    # Place the vacuum cleaner on the grid
    vacuum_position, grid_with_vacuum = place_vacuum(grid)
    
    # Print the initial grid with the vacuum
    print("Initial Grid Environment:")
    print_grid(grid_with_vacuum)
    
    return grid_with_vacuum, vacuum_position

# Example usage:
if __name__ == "__main__":
    X, Y = 5, 5  # Define the size of the grid
    seed_value = 42  # Seed for reproducibility (optional)
    
    # Initialize the environment
    grid, vacuum_position = initialize_environment(X, Y, seed=seed_value)
    
    # Find the closest dirty cell
    closest_dirty_cell, distance_to_closest_dirty = find_closest_dirty_cell(vacuum_position, grid)
    
    if closest_dirty_cell:
        print(f"\nClosest dirty cell to vacuum at {vacuum_position} is at {closest_dirty_cell} with a Manhattan distance of {distance_to_closest_dirty}.")
    else:
        print("\nNo dirty cells found!")
