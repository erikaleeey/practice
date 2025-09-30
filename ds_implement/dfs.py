def dfs(graph, start):
    visited = []
    # TODO: implement recursive or iterative DFS
    return visited


# ---------- TEST ----------
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("DFS from A:", dfs(graph, 'A'))
    # Expected: ['A', 'B', 'D', 'E', 'F', 'C'] (order can vary but must be DFS)
