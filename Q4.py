from Q1 import BFS
from Q2 import A_star
from Q1 import createInput

def printTree(node):
    tempNode = node
    
    while(tempNode != None):
        print(str(tempNode.state) + "\t"+ str(tempNode.cost))
        tempNode = tempNode.parent

if __name__ == "__main__":
    initialState = input("Enter the input for Puzzle Ex: Input (WWWBBB ):\t")
    
    bfsNode = BFS(createInput(initialState))
    astarNode = A_star(createInput(initialState))

    print("\n---Uninformed---")
    printTree(bfsNode)
    
    print("\n---Informed---")
    printTree(astarNode)