
from collections import deque
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        # you write this part

# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions

def bfs_search(search_problem):
    start_node = SearchNode(search_problem.start_state, None)
    frontier = deque([start_node])
    solution = SearchSolution(search_problem, "BFS")

    visited = set()
    visited.add(start_node.state)
    while frontier:
        curr_node = frontier.popleft()
        curr_state = curr_node.state
        if curr_state == search_problem.goal_state:
            path = backtrack(curr_node)
            solution.path += path
            return path

        children = search_problem.get_successors(curr_state)
        for child in children:
            if child not in visited:
                visited.add(child)
                next_node = SearchNode(child, curr_node)
                frontier.append(next_node)
    return "Abort!abort!mission impossible"


def backtrack(node):
    path = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)

    return path.reverse()





# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
dfspath = []
dfsres = []
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    global dfspath,dfsres
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")
    if node.state == search_problem.goal_state:
        dfsres.append(dfspath.copy())
        return
    if depth_limit == 0:
        return
    dfspath.append(node)
    children = search_problem.get_successors(node.state)
    for child in children:
        next_node = SearchNode(child,node)
        dfs_search(search_problem, depth_limit-1, next_node, solution)
    dfspath.pop()
    if dfsres:
        return solution.path.append(dfsres)
    else:
        return "dfs No result"




    # you write this part



def ids_search(search_problem, depth_limit=100):
    global dfspath,dfsres
    # you write this part
    depth = 0
    dfspath = []
    while depth <= depth_limit:
        dfs_search(search_problem, depth)
        depth += 1

