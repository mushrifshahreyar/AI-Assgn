
class Node:
    def __init__(self, state, action, parent, cost):
        self.state = state
        self.action = action
        self.parent = parent
        self.cost = cost

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
        node = Node(state, action, parentNode, parentNode.cost + 1)

        return node
    
    elif(action == 1):
        i = state.index("E")
        if(i == 0):
            return None
        state[i] = state[i-1]
        state[i-1] = "E"
        node = Node(state, action, parentNode, parentNode.cost + 1)

        return node
        
    elif(action == 2):
        i = state.index("E")
        if(i+2 >= n):
            return None
        state[i] = state[i+2]
        state[i+2] = "E"
        node = Node(state, action, parentNode, parentNode.cost + 1)

        return node
        
    elif(action == 3):
        i = state.index("E")
        if(i-2 < 0):
            return None
        state[i] = state[i-2]
        state[i-2] = "E"
        node = Node(state, action, parentNode, parentNode.cost + 1)

        return node

    elif(action == 4):
        i = state.index("E")
        if(i+3 >= n):
            return None
        state[i] = state[i+3]
        state[i+3] = "E"
        node = Node(state, action, parentNode, parentNode.cost + 2)

        return node

    elif(action == 5):
        i = state.index("E")
        if(i-3 < 0):
            return None
        state[i] = state[i-3]
        state[i-3] = "E"
        node = Node(state, action, parentNode, parentNode.cost + 2)

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

def printTree(node):
    tempNode = node
    
    while(tempNode != None):
        print(str(tempNode.state) + "\t"+ str(tempNode.cost))
        tempNode = tempNode.parent

def BFS(initialState):
    
    headNode = Node(initialState, None, None, 0)
    state = getStateSet(headNode.state)
    
    if(checkGoalState(headNode)):
        print("Already in Goal State")
        return

    queue = []
    exploredSet = []

    nActions = len(actions)
    
    queue.append(headNode)

    while(len(queue) != 0):
        parentNode = queue.pop(0)
        state = getStateSet(parentNode.state)

        exploredSet.append(state)
        
        for i in range(nActions):
            node = childNode(parentNode, i)
            if(node != None):
                if(checkGoalState(node)):
                    printTree(node)
                    print(str(headNode.state) + "\tReached Goal State\t" + str(node.cost))
                    return node
                
                state = getStateSet(node.state)

                if(state not in exploredSet):
                    queue.append(node)
                
    return None

def getStateSet(state):
    tState = ""
    for s in state:
        tState += str(s)
    return tState

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
    # initialState = input("Enter the input for Puzzle Ex: Input (WWW BBB):\t")
    with open("output.txt", "r") as f:
        initialStates = f.readlines()
        for initialState in initialStates:
            BFS(createInput(initialState))

    
    # BFS(createInput(initialState))
