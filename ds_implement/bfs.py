from collections import deque

def bfs(graph, start):
    visited = []
    # TODO: implement BFS using queue
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

    print("BFS from A:", bfs(graph, 'A'))
    # Expected: ['A', 'B', 'C', 'D', 'E', 'F']
