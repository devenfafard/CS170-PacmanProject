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

import util

# Container class to hold traversal information
class Node:
    def __init__(self, state, previous_node=None, next_node=None):
        self.state = state
        self.previous_node = previous_node
        self.next_node = next_node

class  UCSNode:
    def __init__(self, state, previous_node=None, next_node=None, cost = 0):
        self.state = state
        self.previous_node = previous_node
        self.next_node = next_node
        self.cost = cost



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
    print "Start's successors:", problem.getSuccessors(problem.getStartState())"""
    
    "*** YOUR CODE HERE ***"

    frontier = util.Stack()    # stack to hold all unvisited nodes
    visited_states = set()     # set to hold all visited states
    path = []                  # array to hold the valid path

    root = problem.getStartState()
   
    # Create a root node to start traversal + push to the frontier
    node = Node(root, None, None)
    frontier.push(node)

    # While we have unexplored nodes...
    while not frontier.isEmpty():
        current_node = frontier.pop()
        current_state = current_node.state

        # If we've found the goal state...
        if (problem.isGoalState(current_state)):
            # Working backwards from the current node, reconstruct the path out of here
            print "\n Goal reached! \n"
            while (current_node.previous_node is not None):
                path.insert(0, current_node.next_node)
                current_node = current_node.previous_node
            break
        else:
            # Else, continue the search.
            print "\n Goal not reached! Continuing search..."

            # If we've seen this state before, skip it.
            if(current_state in visited_states):
                continue
            else:
                # Else, add it to the list of visited states and search each of it's children.
                visited_states.add(current_state)
                for state in problem.getSuccessors(current_state):
                    if(state[0] not in visited_states):
                        new_node = Node(state[0], current_node, state[1])
                        frontier.push(new_node)                   
    return path
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()    # queue to hold all unvisited nodes
    visited_states = set()     # set to hold all visited states
    path = []                  # array to hold the valid path

    root = problem.getStartState()
   
    # Create a root node to start traversal + push to the frontier
    node = Node(root, None, None)
    frontier.push(node)

    # While we have unexplored nodes...
    while not frontier.isEmpty():
        current_node = frontier.pop()
        current_state = current_node.state

        # If we've found the goal state...
        if (problem.isGoalState(current_state)):
            # Working backwards from the current node, reconstruct the path out of here
            print "\n Goal reached! \n"
            while (current_node.previous_node is not None):
                path.insert(0, current_node.next_node)
                current_node = current_node.previous_node
            break
        else:
            # Else, continue the search.
            print "\n Goal not reached! Continuing search..."

            # If we've seen this state before, skip it.
            if(current_state in visited_states):
                continue
            else:
                # Else, add it to the list of visited states and search each of it's children.
                visited_states.add(current_state)
                for state in problem.getSuccessors(current_state):
                    if(state[0] not in visited_states):
                        new_node = Node(state[0], current_node, state[1])
                        frontier.push(new_node)                   
    return path

def uniformCostSearch(problem):
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "Search the node of least total cost first."
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()    # priority queue to hold all unvisited nodes, ranked by cost
    visited_states = set()             # set to hold all visited states
    path = []                          # array to hold the valid path

    root = problem.getStartState()
   
    # Create a root node to start traversal + push to the frontier
    node = UCSNode(root, None, None, 1)
    frontier.push(node, node.cost)

    # While we have unexplored nodes...
    while not frontier.isEmpty():
        current_node = frontier.pop()
        current_state = current_node.state
        current_cost = current_node.cost

        # If we've found the goal state...
        if (problem.isGoalState(current_state)):
            # Working backwards from the current node, reconstruct the path out of here
            print "\n Goal reached! \n"
            while (current_node.previous_node is not None):
                path.insert(0,current_node.next_node)
                current_node = current_node.previous_node
            break
        else:
            # Else, continue the search.
            print "\n Goal not reached! Continuing search..."

            # If we've seen this state before, skip it.
            if(current_state in visited_states):
                continue
            else:
                # Else, add it to the list of visited states and search each of it's children.
                visited_states.add(current_state)
                for state in problem.getSuccessors(current_state):
                    if(state[0] not in visited_states):
                        new_node = UCSNode(state[0], current_node, state[1], current_cost + state[2])
                        frontier.push(new_node, new_node.cost)                
    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()    # priority queue to hold all unvisited nodes, ranked by cost
    visited_states = set()             # set to hold all visited states
    path = []                          # array to hold the valid path

    root = problem.getStartState()
   
    # Create a root node to start traversal + push to the frontier
    node = UCSNode(root, None, None, 0)
    heuristic_cost = heuristic(node.state, problem) + node.cost
    frontier.push(node, heuristic_cost)

    # While we have unexplored nodes...
    while not frontier.isEmpty():
        current_node = frontier.pop()
        current_state = current_node.state
        current_cost = current_node.cost

        # If we've found the goal state...
        if (problem.isGoalState(current_state)):
            # Working backwards from the current node, reconstruct the path out of here
            print "\n Goal reached! \n"
            while (current_node.previous_node is not None):
                path.insert(0,current_node.next_node)
                current_node = current_node.previous_node
            break
        else:
            # Else, continue the search.
            print "\n Goal not reached! Continuing search..."

            # If we've seen this state before, skip it.
            if(current_state in visited_states):
                continue
            else:
                # Else, add it to the list of visited states and search each of it's children.
                visited_states.add(current_state)
                for state in problem.getSuccessors(current_state):
                    if(state[0] not in visited_states):
                        new_node = UCSNode(state[0], current_node, state[1], current_cost + state[2])
                        frontier.push(new_node, heuristic(state[0], problem) + new_node.cost)                
    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
