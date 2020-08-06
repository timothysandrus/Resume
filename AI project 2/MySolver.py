from SuguruSolver import *

class MySolver(SuguruSolver):  
  def __init__(self, problem, maxTime, visualizer):
    SuguruSolver.__init__(self, problem, maxTime, visualizer)
    
  # You should improve these functions to improve performance
  def selectUnassignedLocation(self, state):
    # Find the first location on the board has more than one possibility
    # then return it.  In class we talked about heuristics that might 
    # perform better than this.
    for row in range(self._problem.getSize()[0]):
      for col in range(self._problem.getSize()[1]):

        if len(state.getPossibleValues((row,col))) > 1:
          return (row,col)
          
  def isConsistent(self, state, location, value):
    # Check if putting value at location on the board is consistent
    # with the problem constraints.  This needs to be implemented.
    # Right now it says that it is always consistent.
    #print(state.getCell(state.getCellId(location)))
    cell = state.getCell(state.getCellId(location))
    row,col = state.getSize()
    p1,p2 = location[0], location[1]
    for i in cell:
      if state.isValueKnown(i):
        if state.getPossibleValues(i)[0] == value:
          return False

    for x in range(-1,2):
      for y in range(-1,2):
        if (p2+y >= 0 and y+p2 < col):
          if(p1 + x >= 0 and x + p1 < row):
            loc = (x+p1,y+p2)
            posval = state.getPossibleValues(loc)[0]
            if state.isValueKnown(loc):
              if posval == value:
                return False
    return True
    
  def infer(self, state, changedLocations, initial=False):
    # Perform inference to reduce the possibilities values that can
    # be filled in.  There are a variety of heuristic you could do
    # here to improve performance.  Currently it makes no improvements.
    while len(changedLocations) > 0:
      cl = changedLocations.pop()
      if state.getPossibleValues(cl) == []:
        continue
      #print(state.getPossibleValues(cl)[0])
      if state.getPossibleValues(cl):
        val = state.getPossibleValues(cl)[0]
        for y in range(-1, 2):
          for x in range(-1, 2):
            if ((cl[1] + x) > -1 and (x + cl[1]) < state.getSize()[1]):
              if ((cl[0] + y) > -1 and (y + cl[0]) < state.getSize()[0]):
                if (y + cl[0], x + cl[1]) == cl:
                  continue
                if val in state.getPossibleValues((y + cl[0], x + cl[1])):
                    state.removePossibleValue((y + cl[0], x + cl[1]), val)
                    if state.isValueKnown((y + cl[0], x + cl[1])) and (len(state.getPossibleValues((y + cl[0], x + cl[1])))==1):
                      changedLocations.append((y + cl[0], x + cl[1]))
        for p, i in enumerate(state.getCell(state.getCellId(cl))):
          if i != cl:
            if(val in state.getPossibleValues(i)):
              state.removePossibleValue(i,val)
              if state.isValueKnown(i)and (len(state.getPossibleValues(i))==1):
                changedLocations.append(i)


    #print(state.getPossibleValues((1,1)))
    return state
