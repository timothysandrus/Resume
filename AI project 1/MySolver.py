from SlidingTilePuzzle import *
from SlidingTileSolver import *
from PriorityQueue import *

from math import *


class MySolver(SlidingTileSolver):
    def __init__(self, problem, maxTime):
        SlidingTileSolver.__init__(self, problem, maxTime)

    # You need to redefine this function for your algorithm
    # It is currently using breadth-first search which is very slow
    def solve(self):
        size = self._problem._size
        wThen = dict()
        frontier = PriorityQueue()
        frontier.push(0, (0, self._problem.getInitial()))
        seen = set()
        parent = dict()

        # Do not remove the timeRemaining check from the while loop
        while len(frontier) > 0 and self.timeRemaining():
            # last = dict()
            self._numExpansions += 1

            priority, (depth, currentState) = frontier.pop()
            seen.add(currentState)

            for action in self._problem.actions(currentState):
                resultingState = self._problem.result(currentState, action)

                if self._problem.isGoal(resultingState):
                    # Goal reached
                    parent[resultingState] = (currentState, action)
                    path = ""
                    current = resultingState
                    while current != self._problem.getInitial():
                        (current, action) = parent[current]
                        path = action + path
                    return path

                if resultingState not in seen:
                    frontier.push(depth + self.heuristic(resultingState, wThen,size), (depth + 1, resultingState))
                    seen.add(resultingState)
                    parent[resultingState] = (currentState, action)

        return []

    def heuristic(self, state, wT, size):
        g = 0
        for si, x in enumerate(state):
            if x == 0:
                continue
            if x == si:
               continue
            else:
                if (x, si) not in wT:
                  wT[(x, si)] = abs(si// size - x// size) + abs(si% size - x% size)
                  g += wT[(x, si)]
                else:
                  g += wT[(x, si)]
        return g



