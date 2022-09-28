#Author: Yi Leo Xie  Date: 09/28/2022
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
    # frontier maintained as a queue to maintain ordering
    while frontier:
        curr_node = frontier.popleft()
        curr_state = curr_node.state
        if curr_state == search_problem.goal_state:
            path = backtrack(curr_node)
            if path:
                solution.path += path
            return solution
        children = search_problem.get_successors(curr_state)
        for child in children:
            if child not in visited:
                visited.add(child)
                solution.nodes_visited+=1
                next_node = SearchNode(child, curr_node)
                frontier.append(next_node)
    return None


def backtrack(node):
    # search until there's no more paretns
    path = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)
    res = []
    for i in range(len(path)-1,-1,-1):
        res.append(path[i])

    return res





# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded

def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state

    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")
    solution.nodes_visited += 1
    # found the solution
    if node.state == search_problem.goal_state:
        solution.path.append(node.state)
        return solution
    # base case
    if depth_limit == 0:
        return None
    # pre order add node
    solution.path.append(node.state)

    children = search_problem.get_successors(node.state)
    # print("children ", children)
    for child in children:
        if child in solution.path:
            continue
        next_node = SearchNode(child,node)
        # recursive with one less depth limit
        res = dfs_search(search_problem, depth_limit-1, next_node, solution)
        if res:
            return solution
    # post order pop node
    solution.path.pop()
    return None





    # you write this part



def ids_search(search_problem, depth_limit=100):
    # you write this part
    depth = 0
    node = SearchNode(search_problem.start_state)
    solution = SearchSolution(search_problem, "IDS")

    # gradually increment the depth as we search
    while depth <= depth_limit:
        res = dfs_search(search_problem, depth, node, solution)
        depth += 1
        if res:
            return res

    return None

