from Q1 import BFS
from Q2 import A_star
from Q1 import createInput
from Q1 import printTree

if __name__ == "__main__":
    initialState = input("Enter the input for Puzzle Ex: Input (WWWBBB ):\t")
    print("------------BFS------------")
    bfs_node, bfs_Explored = BFS(createInput(initialState))
    print(bfs_Explored)

    print("\n--------------A*---------------")
    astar_node, astar_Explored = A_star(createInput(initialState))
    print(astar_Explored)