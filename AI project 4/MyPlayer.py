import random

class MyPlayer:
  def setMove(self, move):
    self._move = move
    
  def getMove(self):
    return self._move
  
  def findMove(self, state):
    actions = state.neighborhood(1)
    if len(actions) == 0:
      actions = state.actions()
    self.setMove(random.choice(actions))
