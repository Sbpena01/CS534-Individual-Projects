
from search import *

class MapProblem(Problem):
    """
    This class represents the romanian map problem, allowing a user to search
    for the best path between two cities.
    """

    def __init__(self, initial, goal, map: Graph):
        """Constructor for the map problem. This specific problem has
        individual cities as states in the search graph.

        Args:
            initial: Initial city as the starting point
            goal: The city the user wants to travel to.
            map (Graph): The romanian map (given by search.py)
        """
        self.initial = initial
        self.goal = goal
        self.map = map

    def actions(self, state):
        """Provides all neighboring cities to the given state.

        Args:
            state (Node): City within the Romanian map

        Returns:
            list: List of the names of cities neighboring the given city
        """
        return self.map.graph_dict[state].keys()

    def result(self, state, action):
        """Lists the result of the action the agent performed from the given state.

        Args:
            state (_type_): The state to evaluate actions from.
            action (_type_): The desired action the agent performs. In this case, it is the neighboring city.

        Returns:
            _type_: Since we are travelling along a map, the result of the action is the action itself.
        """
        return action

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + self.map.graph_dict[state1][state2]


class MapPathProblem(Problem):
    def __init__(self, initial, map: Graph, paths: list):
        """Constructor for the Romanian map problem where each state is a completed path
        from the initial city to the goal city. This is used for Hill Climbing and
        Simulated Annealing

        Args:
            initial (_type_): Initial path from starting city to goal city.
            map (Graph): Romanian map provided by search.py
            paths (list): List of all possible paths from starting city to goal city.
        """
        self.initial = initial
        self.map = map
        self.paths = paths

    def actions(self, state):
        """Returns all possible actions from the given state. Since all paths are neighboring each other,
        we just return all the possible paths.
        """
        return self.paths

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. Since the action is just a neighboring path, we return
        the given path as the result of the action."""
        return action

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. Since there is not really
        a cost to go from one state to another in these methods, we just count upwards."""
        return c + 1

    def value(self, state):
        """Returns the value from an objective function to help grade hill climbing and simulated annealing.
        We decided to grade each path based on the total path cost (the sum of the costs for each node
        in the path).
        """
        last_element = state[-1]
        return last_element.path_cost

