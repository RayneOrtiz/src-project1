# Function to initialize the environment
def initialize_environment(X, Y, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Create a grid with random dirt and obstacles
    grid = []
    for i in range(X):
        row = []
        for j in range(Y):
            if random.random() < 0.2:  # 20% chance of being dirty
                row.append('D')
            elif random.random() < 0.1:  # 10% chance of being an obstacle
                row.append('O')
            else:
                row.append('_')
        grid.append(row)

    # Place the vacuum at a random position that is not an obstacle
    while True:
        vacuum_position = (random.randint(0, X-1), random.randint(0, Y-1))
        if grid[vacuum_position[0]][vacuum_position[1]] != 'O':
            break
    
    # Return the grid and the vacuum position
    return grid, vacuum_position

# Example usage:
if __name__ == "__main__":
    X, Y = 5, 5  # Define the size of the grid
    seed_value = 42  # Seed for reproducibility (optional)
    
    # Initialize the environment
    grid, vacuum_position = initialize_environment(X, Y, seed=seed_value)
    
    # Collect all dirty cells' positions
    dirty_cells = [(i, j) for i in range(X) for j in range(Y) if grid[i][j] == 'D']
    
    # Print the initial grid
    print("Initial grid:")
    print_grid(grid)
    
    # Perform random movement cleaning
    random_movement_cleaning(grid, vacuum_position, dirty_cells)
