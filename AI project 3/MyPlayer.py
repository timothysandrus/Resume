from Player import *

import copy
import random
import time


class MyPlayer(Player):
    def __init__(self, timeLimit):
        Player.__init__(self, timeLimit)

    # def id(self, state, ghosts, pellets, ):

    def simMove(self, player, action):
        move = {'Left': (0, -1), 'Right': (0, 1), 'Up': (-1, 0), 'Down': (1, 0)}
        player = (player[0] + move[action][0], player[1] + move[action][1])
        return player

    def heuristic(self, state, action):
        player = state.getPlayerPosition()
        ghosts = state.getGhostPositions()
        pellets = state.getPellets()
        powerups = state.getPowerUps()
        value = state.getScore()

        nearest = 100
        for pellet in pellets:
            if state._map.mapDistance(player, pellet) < nearest:
                nearest = state._map.mapDistance(player, pellet)

        value = value + 10 / nearest

        # ghost
        nearest = 100
        if state.getScaredTurnsLeft() != 0:
            for ghost in ghosts:
                if state._map.mapDistance(player, ghost) < nearest:
                    nearest = state._map.mapDistance(player, ghost)
                    closeGhost = ghost
            if nearest == 0:
                nearest = 1
            value = value + 200 / nearest
        else:
            for ghost in ghosts:
                if state._map.mapDistance(player, ghost) < nearest:
                    nearest = state._map.mapDistance(player, ghost)
                    closeGhost = ghost
                if nearest == 0:
                    nearest = 1
                value = value + 200 / nearest

        # Power up
        nearest = 100
        if state._map.mapDistance(player, ghosts[0]) < 5:  # and state.getScaredTurnsLeft() == 0:
            if powerups:
                for powerup in powerups:
                    if state._map.mapDistance(player, powerup) < nearest:
                        nearest = state._map.mapDistance(player, powerup)
                if nearest == 0:
                    nearest = 1
                value = value + 200 / nearest

        if state.getScaredTurnsLeft() > 3:
            value = value + 1000
        return value

    def maxPlayerValue(self, state, depth, a, score, con):
        move = {'Left': (0, -1), 'Right': (0, 1), 'Up': (-1, 0), 'Down': (1, 0)}
        if state.gameOver() or not self.timeRemaining():
            temp = state.getScore()
            score.append(temp)
            return state.getScore(), a
        if depth == 0:
            # print('depth limit reached')
            temp = self.heuristic(state, a)
            score.append(temp)
            return self.heuristic(state, a), a  # state.getScore() # heuristic(state)

        best = (-100000, None)
        player = state.getPlayerPosition()
        ghosts = state.getGhostPositions()
        globalAction = ''
        for action in state.actions():
            if action == 'Stay':
                continue
            result = state.result(action)

            temp = copy.deepcopy(score)
            temp.append(action)
            v = self.randomPlayerValue(result, depth - 1, action, temp)
            # if v > best:
            # if thinking about making one for scared and another for not scared
            if result.getScaredTurnsLeft() == 0:
                if v[0] > best[0] and (player[0] + move[action][0], player[1] + move[action][1]) not in ghosts:
                    best = max(best[0], v[0]), action
                    globalAction = action
            else:
                if v[0] > best[0]:
                    # self.setMove(action)
                    best = max(best[0], v[0]), action
                    globalAction = action

        return best

    def randomPlayerValue(self, state, depth, a, score):
        if state.gameOver() or not self.timeRemaining():
            temp = state.getScore()
            score.append(temp)
            return state.getScore(), 'fuck'
        if depth == 0:
            temp = self.heuristic(state, a)
            score.append(temp)
            return self.heuristic(state, a), 'fuck'  # state.getScore() # heuristic(state)

        average = 0
        for (state, prob) in state.ghostResultDistribution():
            actions = state.actions()
            if 'Stay' in actions:
                actions.remove('Stay')

            best = 0
            for action in actions:
                result = state.result(action)
                temp = copy.deepcopy(score)
                temp.append(action)
                if result.getPlayerPosition() in result.getGhostPositions() and result.getScaredTurnsLeft() == 0 and result.getPlayerPosition() not in result.getPowerUps():
                    v = 0, 'dead'
                else:
                    v = self.maxPlayerValue(result, depth - 1, action, temp, False)
                    if v[0] > best:
                        best = v[0]
            average += prob * best  # v[0]

        return average, 'fuck'

    def findMove(self, state):
        depth = 1
        while (self.timeRemaining()):
            choice = self.maxPlayerValue(state, depth, None, [], True)
            self.setMove(choice[1])
            depth = depth + 1
