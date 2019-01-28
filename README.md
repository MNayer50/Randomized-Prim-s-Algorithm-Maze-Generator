# Randomized-Prim-s-Algorithm-Maze-Generator
Prim's algorithm is greedy algorithm that finds a minimum spanning tree.

The algorithm can be used to generate mazes. 
This python script will generate a random maze size between 21x21 and 131x131 and pick random complexity and density values.

Start with path-less 2 dimensional array of cells (the grid)

1. Cells have 2 states: Wall or Passage

2. Pick a random Cell and set it as a passage cell

3. Add the walls of the passage cell to wall list

4. while there are remaining walls in the list:
	1. pick a random wall in list.
	if only 1 of 2 cells that the wall divides is visited, then:
		1. make the wall a passage and mark the unvisited cell as part of maze
		2. add neighboring walls of cell to wall list
	2. remove wall from list
    
Each time the program is run a different maze will be generated using the same algorithm.
The final maze is assigned to an array of x and y values and their state where 0 (False) is a wall and 1 (True) is passage.

```pyplot.imshow``` is used to display the final maze image.
