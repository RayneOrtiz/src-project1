import heapq
import random

# Priority queue item for A* search
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# Function to calculate Manhattan distance (used for heuristic in A*)
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Function to find the closest dirty cell
def find_closest_dirty_cell(vacuum_position, grid):
    dirty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'D']
    if not dirty_cells:
        return None, float('inf')  # No dirty cells remaining
    
    closest_cell = min(dirty_cells, key=lambda cell: manhattan_distance(vacuum_position, cell))
    return closest_cell, manhattan_distance(vacuum_position, closest_cell)

# A* Search algorithm to navigate to the closest dirty cell
def a_star_search(grid, start, goal):
    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Priority queue to explore the nodes
    frontier = PriorityQueue()
    frontier.put(start, 0)
    
    # Dictionary to store the cost and path
    came_from = {}
    cost_so_far = {}
    
    # Initial position of the vacuum cleaner
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        # If we reach the goal (a dirty cell), stop
        if current == goal:
            break
        
        # Explore the neighbors (up, down, left, right)
        for direction in directions:
            next_node = (current[0] + direction[0], current[1] + direction[1])
            
            # Ensure the neighbor is within grid bounds
            if 0 <= next_node[0] < len(grid) and 0 <= next_node[1] < len(grid[0]):
                # Ensure we are not moving into an obstacle
                if grid[next_node[0]][next_node[1]] != 'O':
                    new_cost = cost_so_far[current] + 1  # Cost of moving to the next node
                    # Check if this path is the shortest to the next node
                    if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                        cost_so_far[next_node] = new_cost
                        priority = new_cost + manhattan_distance(next_node, goal)
                        frontier.put(next_node, priority)
                        came_from[next_node] = current
    
    # Reconstruct the path from start to goal
    if goal not in came_from:
        return []  # No valid path

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    
    return path

# Function to clean the closest dirty cell using A* search
def clean_closest_dirty_cell(vacuum_position, grid):
    closest_dirty_cell, _ = find_closest_dirty_cell(vacuum_position, grid)
    
    if closest_dirty_cell:
        # Perform A* search to move the vacuum cleaner to the dirty cell
        path_to_dirty = a_star_search(grid, vacuum_position, closest_dirty_cell)
        
        if path_to_dirty:
            # Simulate the vacuum cleaner moving along the path and cleaning the dirty cell
            for step in path_to_dirty:
                vacuum_position = step
                print(f"Vacuum moved to {step}")
            
            # Clean the dirty cell
            print(f"Vacuum cleaned cell {closest_dirty_cell}")
            grid[closest_dirty_cell[0]][closest_dirty_cell[1]] = '_'
            
            # Return the updated vacuum position
            return vacuum_position
        else:
            print(f"No path to dirty cell at {closest_dirty_cell}")
            return vacuum_position
    else:
        print("No dirty cells remaining!")
        return vacuum_position

# Function to create the grid environment
def create_grid(x, y, seed=None):
    if seed is not None:
        random.seed(seed)
    
    grid = [['_' for _ in range(y)] for _ in range(x)]
    
    # Randomly place obstacles and dirty cells
    num_obstacles = random.randint(1, x * y // 5)  # Random number of obstacles
    num_dirty_cells = random.randint(1, x * y // 4)  # Random number of dirty cells
    
    for _ in range(num_obstacles):
        obstacle_x = random.randint(0, x - 1)
        obstacle_y = random.randint(0, y - 1)
        grid[obstacle_x][obstacle_y] = 'O'
    
    for _ in range(num_dirty_cells):
        dirty_x = random.randint(0, x - 1)
        dirty_y = random.randint(0, y - 1)
        if grid[dirty_x][dirty_y] == '_':  # Ensure it's not an obstacle
            grid[dirty_x][dirty_y] = 'D'
    
    return grid

# Function to place the vacuum in a random empty spot
def place_vacuum(grid):
    while True:
        vacuum_x = random.randint(0, len(grid) - 1)
        vacuum_y = random.randint(0, len(grid[0]) - 1)
        if grid[vacuum_x][vacuum_y] == '_':
            grid[vacuum_x][vacuum_y] = 'V'
            return (vacuum_x, vacuum_y), grid

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

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
    
    # Simulate cleaning all dirty cells
    while True:
        new_vacuum_position = clean_closest_dirty_cell(vacuum_position, grid)
        
        # Break if the vacuum didn't move, meaning there are no dirty cells left
        if new_vacuum_position == vacuum_position:
            break
        vacuum_position = new_vacuum_position
