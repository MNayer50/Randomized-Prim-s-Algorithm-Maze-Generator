import numpy
from numpy.random import randint as rand
import matplotlib.pyplot as pyplot
import random

def maze():

    #only odd sides
    width = random.randrange(21, 131, 2)
    height = random.randrange(21, 131, 2)

    complexity = random.uniform(0.0,1.0)
    density = random.uniform(0.0,1.0)

    # Builds maze grid with odd sides
    grid = (height , width)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (grid[0] + grid[1]))) # number of components
    density    = int(density * ((grid[0] // 2) * (grid[1] // 2))) # size of components

    # Build actual maze
    Z = numpy.zeros(grid, dtype=bool)

    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles

    for i in range(density):
        x, y = rand(0, grid[1] // 2) * 2, rand(0, grid[0] // 2) * 2 # pick a random position
        Z[y, x] = 1 #block added to maze
        for j in range(complexity):
            neighbours = []
            if x > 1:
                neighbours.append((y, x - 2))
            if x < grid[1] - 2: 
                neighbours.append((y, x + 2))
            if y > 1:            
                 neighbours.append((y - 2, x))
            if y < grid[0] - 2:  
                neighbours.append((y + 2, x))                
            if len(neighbours):
                y1,x1 = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y1, x1] == 0:
                    Z[y1, x1] = 1
                    Z[y1 + (y - y1) // 2, x1 + (x - x1) // 2] = 1
                    x, y = x1, y1
    return Z
pyplot.figure(figsize=(10, 10))
pyplot.imshow(maze(), cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()