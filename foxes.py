from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search

# Create a few test problems:
problem111 = FoxProblem((1,1,1))
problem331 = FoxProblem((3, 3, 1))
problem541 = FoxProblem((5, 4, 1))
problem551 = FoxProblem((5, 5, 1))
problem1234 = FoxProblem((16,8,1))
# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.
# print(dfs_search((problem1234)))
# print(bfs_search(problem111))
# print(dfs_search(problem111))
# print(ids_search(problem111))

print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))

print(bfs_search(problem551))
print(dfs_search(problem551))
print(ids_search(problem551))

print(bfs_search(problem541))
print(dfs_search(problem541))
print(ids_search(problem541))
