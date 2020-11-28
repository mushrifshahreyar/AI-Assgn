from Q1 import getStateSet, Node, BFS, createInput
from Q2 import A_star

AcheivedGoalState = [False, False, False, False, False, False, False]
AcheivedGoalCost = [100, 100, 100, 100, 100, 500, 500]
goalState = ["WWWBBBE", "WWWBBEB", "WWWBEBB", "WWWEBBB", "WWEWBBB", "WEWWBBB", "EWWWBBB"]

def checkGoalState(node):
    state = node.state
    state = getStateSet(state)
    
    i = 0
    
    if(state in goalState):
        k = goalState.index(state)
        if(AcheivedGoalState[k]):
            if(AcheivedGoalCost[k] > node.cost):
                AcheivedGoalCost[k] = node.cost
        else:
            AcheivedGoalState[k] = True
            AcheivedGoalCost[k] = node.cost
        
        for b in AcheivedGoalState:
            if(b):
                i += 1
    
    if(i == 7):

        for i in range(len(goalState)):
            print(goalState[i] + "\t" +str(AcheivedGoalCost[i]))
        return True

    return False

if __name__ == "__main__":
    initialState = input("Enter the input for Puzzle Ex: Input (WWWBBB ):\t")

    print("------------BFS------------")
    bfs_node, bfs_Explored = BFS(createInput(initialState),checkGoalState)
    
    print("\n--------------A*---------------")
    astar_node, astar_Explored = A_star(createInput(initialState),checkGoalState)