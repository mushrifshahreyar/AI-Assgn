from Q1 import createInput, BFS, printTree, checkGoalState
from Q2 import A_star

if __name__ == "__main__":
    initialState = input("Enter the input for Puzzle Ex: Input (WWWBBB ):\t")
    print("\n------------BFS------------")
    bfs_node, bfs_Explored = BFS(createInput(initialState), checkGoalState)
    print("\n" + str(initialState) + "\nReached Goal State :\t" + str(bfs_node.cost) + "\tExplored Set :\t" + str(bfs_Explored))

    print("\n-------------A*------------")
    astar_node, astar_Explored = A_star(createInput(initialState),checkGoalState)
    print("\n" + str(initialState) + "\nReached Goal State :\t" + str(astar_node.cost) + "\tExplored Set :\t" + str(astar_Explored))