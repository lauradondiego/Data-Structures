# DEPTH-FIRST SEARCH (RECURSIVE)

- The depth-first search algorithm allows us to determine whether two nodes, node x and node y, have a path between them. The DFS algorithm does this by looking at all of the children of the starting node, node x, until it reaches node y. It does this by _RECURSIVELY_ taking the same steps, again and again, in order to determine if such a path between two nodes even exists.
- Tells us if a path even exists, not the shortest path
- Traverse down a single path, one child node at a time
- sticks with one path, following that path down a graph structure until it ends
- Stack

# BREADTH-FIRST SEARCH

-
- Good for finding the shortest path b/w 2 nodes on a graph
- Traverse thru a graph one level of children at a time
- evaluates all the possible paths from a given node equally, checking all potential vertices from one node together, and comparing them simultaneously
- Queue
