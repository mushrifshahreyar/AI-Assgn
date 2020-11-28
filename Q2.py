import heapq

class Node:
    def __init__(self, state, action, parent, cost, priority):
        self.state = state
        self.action = action
        self.parent = parent
        self.cost = cost
        self.priority = priority

    def __lt__(self, other):
        return self.cost < other.cost

actions = ["adjacentLeft", "adjacentRight", "1hopLeft", "1hopRight", "2hopLeft", "2hopRight"]


def childNode(parentNode, action):
    state = parentNode.state.copy()
    n = len(state)
    if(action == 0):
        i = state.index("E")
        if(i+1 == n):
            return None
        state[i] = state[i+1]
        state[i+1] = "E"
        cost = parentNode.cost + 1
        # print(hsld(state))
        node = Node(state, action, parentNode, cost, cost+hsld(state))

        return node
    
    elif(action == 1):
        i = state.index("E")
        if(i == 0):
            return None
        state[i] = state[i-1]
        state[i-1] = "E"
        cost = parentNode.cost + 1
        # print(hsld(state))
        node = Node(state, action, parentNode, cost, cost+hsld(state))

        return node
        
    elif(action == 2):
        i = state.index("E")
        if(i+2 >= n):
            return None
        state[i] = state[i+2]
        state[i+2] = "E"
        cost = parentNode.cost + 1
        # print(hsld(state))
        node = Node(state, action, parentNode, cost, cost+hsld(state))

        return node
        
    elif(action == 3):
        i = state.index("E")
        if(i-2 < 0):
            return None
        state[i] = state[i-2]
        state[i-2] = "E"
        cost = parentNode.cost + 1
        # print(hsld(state))
        node = Node(state, action, parentNode, cost, cost+hsld(state))

        return node

    elif(action == 4):
        i = state.index("E")
        if(i+3 >= n):
            return None
        state[i] = state[i+3]
        state[i+3] = "E"
        # print(hsld(state))
        cost = parentNode.cost + 2
        node = Node(state, action, parentNode, cost, cost+hsld(state))

        return node

    elif(action == 5):
        i = state.index("E")
        if(i-3 < 0):
            return None
        state[i] = state[i-3]
        state[i-3] = "E"
        cost = parentNode.cost + 2
        # print(hsld(state))
        node = Node(state, action, parentNode, cost, cost+hsld(state))

        return node

    else:
        return None

def checkGoalState(node):
    state = node.state
    n = len(state)
    foundBlack = False
    for i in range(n):
        if(state[i] == "B"):
            foundBlack = True
            continue
        if(foundBlack and state[i] == "W"):
            return False
    
    return True

def hsld(state):
    val = 0
    for i in range(len(state)):
        if(state[i] == "B"):
            for j in range(i,len(state)):
                if(state[j] == "W"):
                    val += 1
    # print(val)
    return val

def printTree(node):
    tempNode = node
    
    while(tempNode != None):
        print(str(tempNode.state) + "\t"+ str(tempNode.cost))
        tempNode = tempNode.parent

def getStateSet(state):
    tState = ""
    for s in state:
        tState += str(s)
    return tState


def A_star(initialState):
    
    headNode = Node(initialState, None, None, 0, 0)
    
    if(checkGoalState(headNode)):
        print("Already in Goal State")
        return headNode, 0
    
    priorityQueue = []
    exploredSet = []
    exploredCost = []
    
    
    
    nActions = len(actions)
    val = headNode.cost + hsld(initialState)
    heapq.heappush(priorityQueue,(val, headNode))
    
    while(len(priorityQueue) != 0):
        
        parentNode = heapq.heappop(priorityQueue)[-1]
        
        state = getStateSet(parentNode.state)
        exploredSet.append(state)
        exploredCost.append(parentNode.cost)
        
        for i in range(nActions):
            node = childNode(parentNode, i)
            if(node != None):
                if(checkGoalState(node)):
                    # printTree(node)
                    print(str(initialState) + "\tReached Goal State\t" + str(node.cost))
                    return node, len(exploredCost)

                state = getStateSet(node.state)
                
                if(state in exploredSet):
                    k = exploredSet.index(state)
                    if(node.cost < exploredCost[k]):
                        exploredCost[k] = node.cost
                        val = node.cost + hsld(initialState)
                        heapq.heappush(priorityQueue, (val, node))
                else:
                    val = node.cost + hsld(initialState)
                    heapq.heappush(priorityQueue,(val, node))
    
    return None, 0

def createInput(initialState):
    state = []
    
    for i in range(len(initialState)):
        if(initialState[i] == "W" or initialState[i] == "w"):
            state.append('W')
        elif(initialState[i] == "B" or initialState[i] == "b"):
            state.append('B')
        elif(initialState[i] == " "):
            state.append("E")
        else:
            pass

    return state      

if __name__ == "__main__":
    # initialState = input("Enter the input for Puzzle Ex: Input (WWWBBB ):\t")
    # A_star(createInput(initialState))
    with open("input.txt", "r") as f:

        initialStates = f.readlines()
        for initialState in initialStates:
            A_star(createInput(initialState))

    
