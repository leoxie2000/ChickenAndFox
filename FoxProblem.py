#Author: Yi Leo Xie  Date: 09/28/2022

class FoxProblem:
    #(chicken,fox,boat)
    def __init__(self, start_state=(1, 1, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)


        # you might want to add other things to the problem,
        #  like the total number of chickens (which you can figure out
        #  based on start_state

    # get successor states for the given state
    def get_successors(self, state):
        successor_list = []
        chicken,fox,boat = state[0],state[1],state[2]
        # print("chicke, fox, boat ", chicken,fox,boat)
        if boat == 1:
            possible_states = [(chicken-2,fox,0),(chicken-1,fox-1,0),(chicken-1,fox,0),
                               (chicken,fox-1,0),(chicken,fox-2,0)]
        if boat == 0:
            possible_states = [(chicken+1,fox,1),(chicken+2,fox,1),(chicken+1,fox+1,1),
                               (chicken, fox+1,1),(chicken,fox+2,1)]
        # print("possible_states ", possible_states)
        for state in possible_states:
            if self.validify_state(state):
                successor_list.append(state)
        return successor_list

        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list

    # I also had a goal test method. You should write one.
    def validify_state(self, state):
        # print("validifying state ", state)
        original_chicken, original_fox = self.start_state[0], self.start_state[1]
        chicken, fox, boat = state[0], state[1], state[2]
        chicken_across = original_chicken - chicken
        fox_across = original_fox - fox
        if 0 <= chicken <= original_chicken and 0 <= fox <= original_fox:
            if chicken == 0 or chicken >= fox:
                if chicken_across == 0 or chicken_across >= fox_across:
                    return True
        return False


    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((3, 3, 1))
    print(test_cp.get_successors((3, 3, 1)))
    print(test_cp)
