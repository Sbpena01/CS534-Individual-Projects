from search import *
from SimpleProblemSolvingAgent import *

def main():
    # Inits the user_response to the 'Continue?' question. If it is not yes, then the app
    # closes.
    termination_check = "yes"
    
    # Print out all cities for user to view at beginning of app.
    print("Here are all the possible Romania cities that can be traveled: \n")
    print(*romania_map.graph_dict.keys())
    
    # We want to keep running this code until the user says they don't want to continue.
    while termination_check == "yes":
        # Ask for origin city 
        initial = input("Please enter origin city: ")
        if initial not in romania_map.graph_dict:  # Error check in case origin city is not in graph.
            initial = input("Could not find " + initial + ", please try again: ")
            continue
        
        # Ask for destination city.
        goal = input("Please enter the destination city: ")
        if goal == initial:  # Check to make sure origin and destination are different.
            print("The same city can't be both origin and destination. Please try again.")
            continue
        elif goal not in romania_map.graph_dict:  # Check for destination to be in graph.
            initial = input("Could not find " + goal + ", please try again: ")
            continue
        
        print()  # Print new line for better terminal print
        
        # Perform search algorithm using SimpleProblemSolvingAgent.
        search_algorithm = SimpleProblemSolvingAgent(MapProblem(initial, goal, romania_map, ))
        search_algorithm()
        
        # Ask if the user wants to continue looking for cities.
        termination_check = input("Would you like to find the best path between the other two cities? [yes/no] ").lower()
        
    # If the user inputs an unknown answer to the last question, just close the app.
    if termination_check != "no":
        print("Unknown input. Closing app...")
        exit()
    
    print("Thank You for Using Our App")
    exit()

if __name__ == "__main__":
    main()
