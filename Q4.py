from Q1 import BFS, createInput, checkGoalState
from Q2 import A_star

def printTree(node):
    tempNode = node
    stack = []
    while(tempNode != None):
        stack.append(tempNode)
        tempNode = tempNode.parent
    
    while(len(stack) != 0):
        tempNode = stack.pop(len(stack) - 1)
        print(str(tempNode.state) + "\t"+ str(tempNode.cost))

if __name__ == "__main__":
    initialState = input("Enter the input for Puzzle Ex: Input (WWWBBB ):\t")
    
    print("\n------------BFS------------")
    bfs_node, bfs_Explored = BFS(createInput(initialState), checkGoalState)
    printTree(bfs_node)
    print("\n" + str(initialState) + "\nReached Goal State :\t" + str(bfs_node.cost))

    print("\n-------------A*------------")
    astar_node, astar_Explored = A_star(createInput(initialState),checkGoalState)
    print("\n" + str(initialState) + "\nReached Goal State :\t" + str(astar_node.cost))
    printTree(astar_node)
