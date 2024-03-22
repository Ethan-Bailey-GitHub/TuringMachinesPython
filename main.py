class state:
    def __init__(self,label,operations):
        #operations is a 2D list that contains lists of the format
        #[input symbol,read, write, move read tape, move write tape]
        #where input symbol, read and writ are terminals,
        #move read tape and move write tape are either "L" (left), "R" (Right)
        #or "N" (None)
        self.label=label
        self.operations=operations
        
        
class terminal:
    def __init__(self,label):
        self.label=label

class tape:
    def __init__(self,state=['#']):
        self.state=state

class readTape(tape):
    def __init__(self,state):
        super().__init__(state)

class writeTape(tape):
    def __init__(self):
        super().__init__()

class DTM:
    def __init__(self,states,start):
        self.states=states
        self.start=start
