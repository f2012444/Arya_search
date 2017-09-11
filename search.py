# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util, sys

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # stack for holding the nodes since it is dfs
    st = util.Stack()


    startState = problem.getStartState()

    if startState is None:
        print " Invalid Start state"
        sys.exit()

    # row_length represents total no of rows
    # col_length represents total no of cols

    # the set to keep track of the expanded nodes
    expandedSet = set()

    if problem.isGoalState(startState):
        print " Goal found "
        return []

    dir = {'West': 'W', 'East': 'E', 'South': 'S', 'North': 'N'}

    if startState not in expandedSet:
        for state in problem.getSuccessors(startState):
            # We push tuples with each of size 2 onto stack
            # first element is state, second element is direction you take to get to that state from the starting point
            # Thank you Kevin (Undergrad TA) for helping me with this
            st.push((state, state[1]))

        expandedSet.add(startState)




    # the dfs algorithm

    while st is not None:

        if st.isEmpty():
            print " Goal not found"
            return []

        tup  = st.pop()
        curState = tup[0]
        path = tup[1]

        if problem.isGoalState(curState[0]):
            print " Goal found "
            # Goal is found at this state
            #actions = getpath(path)
            return path.split(',')
            #return actions
        if curState[0] not in expandedSet:
            for state in problem.getSuccessors(curState[0]):
                st.push((state, path +','+ state[1]))
            expandedSet.add(curState[0])


    print " Goal not found"
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    qu = util.Queue()

    startState = problem.getStartState()

    if startState is None:
        print " Invalid Start state"
        sys.exit()

    # row_length represents total no of rows
    # col_length represents total no of cols

    # the set to keep track of the expanded nodes
    expandedSet = set()

    if problem.isGoalState(startState):
        print " Goal found "
        return []


    if startState not in expandedSet:
        for state in problem.getSuccessors(startState):
            # We push tuples with each of size 2 onto stack
            # first element is state, second element is direction you take to get to that state from the starting point
            # Thank you Kevin (Undergrad TA) for helping me with this
            qu.push((state, state[1]))

        expandedSet.add(startState)

    # the dfs algorithm

    while qu is not None:

        if qu.isEmpty():
            print " Goal not found"
            return []

        tup = qu.pop()
        curState = tup[0]
        path = tup[1]

        if problem.isGoalState(curState[0]):
            print " Goal found "
            # Goal is found at this state
            # actions = getpath(path)
            return path.split(',')
            # return actions
        if curState[0] not in expandedSet:
            for state in problem.getSuccessors(curState[0]):
                qu.push((state, path + ',' + state[1]))
            expandedSet.add(curState[0])

    print " Goal not found"
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    pq = util.PriorityQueue()

    startState = problem.getStartState()

    if startState is None:
        print " Invalid Start state"
        sys.exit()

    # row_length represents total no of rows
    # col_length represents total no of cols

    expandedSet = set()
    if problem.isGoalState(startState):
        print " Goal found "
        return []


    # PriorityQueue is pushed with tuples each of size 3 and also the priorirty value
    # first element is state, second element is direction you take to get to that state from the starting point
    # third element represent the cost to get to that node from the starting location
    # the priority value is obtained from the third element of the above tuple

    if startState not in expandedSet:
        for state in problem.getSuccessors(startState):
            pq.push((state, state[1], state[2]), state[2])
        expandedSet.add(startState)

    # UCS algorithm

    while pq is not None:
        if pq.isEmpty():
            print " Goal not found"
            return []

        tup = pq.pop()
        curState = tup[0]
        path = tup[1]
        pathlength = tup[2]
        # actions.append(dir[curState[1]])
        if problem.isGoalState(curState[0]):
            print " Goal found "
            # actions.append(dir[curState[1]])
            return path.split(',')
        if curState[0] not in expandedSet:
            for state in problem.getSuccessors(curState[0]):
                    pq.push((state, path +',' + state[1], pathlength + state[2]), pathlength + state[2])
        expandedSet.add(curState[0])

    print " Goal not found"
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    pq = util.PriorityQueue()

    startState = problem.getStartState()

    if startState is None:
        print " Invalid Start state"
        sys.exit()

    # row_length represents total no of rows
    # col_length represents total no of cols

    expandedSet = set()
    if problem.isGoalState(startState):
        print " Goal found "
        return []

    # PriorityQueue is pushed with tuples each of size 3 and also the priorirty value
    # first element is state, second element is direction you take to get to that state from the starting point
    # third element represent the cost to get to that node from the starting location
    # the priority value is obtained from the third element of the above tuple

    if startState not in expandedSet:
        for state in problem.getSuccessors(startState):
            heur = heuristic(state[0], problem)
            pq.push((state, state[1], state[2]), heur + state[2])
        expandedSet.add(startState)

    # UCS algorithm

    while pq is not None:
        if pq.isEmpty():
            print " Goal not found"
            return []

        tup = pq.pop()
        curState = tup[0]
        path = tup[1]
        pathlength = tup[2]
        # actions.append(dir[curState[1]])
        if problem.isGoalState(curState[0]):
            print " Goal found "
            # actions.append(dir[curState[1]])
            return path.split(',')
        if curState[0] not in expandedSet:
            for state in problem.getSuccessors(curState[0]):
                heur = heuristic(state[0], problem)
                pq.push((state, path + ',' + state[1], pathlength + state[2]), heur + pathlength + state[2])
        expandedSet.add(curState[0])

    print " Goal not found"
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
