class FoxProblem:
    #(chicken,fox,boat)
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        # you might want to add other things to the problem,
        #  like the total number of chickens (which you can figure out
        #  based on start_state

    # get successor states for the given state
    def get_successors(self, state):
        successor_list = []
        chicken,fox,boat = state[0],state[1],state[2]
        if boat == 1:
            possible_states = [(chicken-2,fox,0),(chicken-1,fox-1,0),()]

        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list

    # I also had a goal test method. You should write one.
    def validify_state(self, state):
        chicken, fox, boat = state[0], state[1], state[2]
        if chicken < 0 or fox < 0:
            return False
        if fox > chicken:
            return False
        chicken_across,fox_across = self.start_state[0],self.start_state[1]
        if fox_across > chicken_across:
            return False

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
