from search import *
from Problem import *
import numpy as np

class SimpleProblemSolvingAgent:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, problem: MapProblem):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.problem = problem

    def __call__(self):
        """Code that executes all search algorithms and prints.
        """
        # Begin with greedy search and A*.
        self.greedySearch(self.problem)
        print()  # I include these empty print statements to add new lines between search algorithms in terminal.
        self.aStarSearch(self.problem)
        print()
        
        # This is where we switch to using Hill Climbing and Simulated Annealing. Since these
        # methods require that states are completed paths and not individual cities, we use
        # MapPathProblem to make the required adjustments.
        all_possible_solutions = self.pathStateGeneration(self.problem)
        path_problem = MapPathProblem(all_possible_solutions[0], self.problem.map, all_possible_solutions)
        
        self.hillClimbingSearch(path_problem)
        print()

        self.simulatedAnnealing(path_problem)
        print()
        
    def pathStateGeneration(self, problem):
        """
        Returns all possible paths from the initial city to the goal city. I used DFS to generate all
        possible paths.
        """
        frontier = [(Node(problem.initial))]  # Stack
        paths = list()
        # Since we are looking to find all possible paths, we keep running DFS
        # until we have no more nodes in the frontier.
        while frontier:
            node = frontier.pop()
            
            # When we find a path that reaches the goal, add the current path to the list of
            # successful paths. We will return this list once all paths are found.
            if problem.goal_test(node.state):
                paths.append(node.path())
                continue 
            
            # We should only had child nodes that are not already in the current path being found.
            # This is to prevent any duplicate nodes in a path (i.e. loops) and prevents the search
            # running infinitely.
            frontier.extend(child for child in node.expand(problem)
                            if child not in node.path())
        return paths

    def heuristic(self, state):
        """Heuristic function for A*, which is just the euclidean distance from the current node to the goal.
        """
        state_coordinate = self.problem.map.locations[state]
        goal_coordinate = self.problem.map.locations[self.problem.goal]
        signed_distance =  np.sqrt((goal_coordinate[0] - state_coordinate[0])**2 + (goal_coordinate[1] - state_coordinate[1])**2)
        return np.abs(signed_distance)
        
    def printPath(self, path):
        """Prints the path to terminal for the user to view.
        """
        starting_node = path[0]
        print(starting_node.state, end=" ")
        for node in path:
            print("->", node.state, end=" ")
        print()
        
    def printPathCost(self, path):
        """Prints the path cost for user to view."""
        print("Total Cost: ", path[-1].path_cost)

    def greedySearch(self, problem):
        """Performs Greedy Best-First Search based on user inputs."""
        print("Greedy Best-First Search")
        path = best_first_graph_search(problem, lambda node: self.heuristic(problem.initial))
        self.printPath(path)
        self.printPathCost(path)
        
    def aStarSearch(self, problem):
        """Performs A* Search based on user inputs."""
        print("A* Search")
        path = best_first_graph_search(problem, lambda node: self.heuristic(problem.initial)+node.path_cost)
        self.printPath(path)
        self.printPathCost(path)
    
    def hillClimbingSearch(self, problem):
        """Performs Hill Climbing Search based on user inputs."""
        print("Hill Climbing Search")
        path = hill_climbing(problem)
        self.printPath(path)
        self.printPathCost(path)
        return path

    def simulatedAnnealing(self, problem):
        """Performs Simulated Annealing Search based on user inputs."""
        print("Simulated Annealing")
        path = simulated_annealing(problem)
        self.printPath(path)
        self.printPathCost(path)
        
