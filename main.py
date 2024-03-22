class state:
    def __init__(self,label,operations,valid):
        #operations is a 2D list that contains lists of the format
        #[input symbol, read, write, move read tape, move write tape, nextState]
        #where input symbol, read and writ are terminals,
        #move read tape and move write tape are either "L" (left), "R" (Right)
        #or None (None)
        self.label=label
        self.operations=operations
        self.valid=valid  #Checks the state implies a valid input

    def changeNextState(self,operationIndex,nextState):
        self.operations[operationIndex][5]=nextState

        
class terminal:
    def __init__(self,label):
        self.label=label

class tape:
    def __init__(self,state=['#']):
        self.state=state

class readTape(tape):
    def __init__(self,state):
        super().__init__(state)
        self.index=0
    
class writeTape(tape):
    def __init__(self):
        super().__init__()
        self.index=1

class DTM:
    def __init__(self,states,start):
        self.states=states
        self.start=start

    def checkInput(self,inp):
        currentRead = readTape(list(inp))
        currentWrite = writeTape()
        for operation in self.states[self.states.index(self.start)].operations:
            pass

S1=state("S1",(("x",None,None,"R",None,None),(">",None,None,None,None,None)),False) #S1 has one operation: x, ∆/∆, R, N
S1.changeNextState(0,S1)  #S1 now goes to itself in its first operation
S2=state("S2",(),True)
S1.changeNextState(1,S2) #S1 now goes to the valid state in its second operation
