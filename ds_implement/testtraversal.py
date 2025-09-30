import dfs, bfs

def test_dfs_basic_and_cycle():
    g = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    order = dfs(g, 'A')
    assert order[0] == 'A'
    # DFS visits all reachable nodes once
    assert set(order) == {'A', 'B', 'C', 'D', 'E', 'F'}

def test_bfs_basic_and_levels():
    g = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'D'],  # duplicate neighbor
        'C': [],
        'D': ['B']
    }
    order = bfs(g, 'A')
    # Level order from A
    assert order[:3] == ['A', 'B', 'C']
    assert set(order) == {'A', 'B', 'C', 'D'}

def test_start_not_in_graph_and_empty_graph():
    assert dfs({}, 'X') == []
    assert bfs({}, 'X') == []
    g = {'A': []}
    assert dfs(g, 'Z') == []
    assert bfs(g, 'Z') == []

def test_self_loop_and_disconnected_component():
    g = {
        'A': ['A', 'B'],  # self-loop at A
        'B': [],
        'C': ['D'],       # disconnected component
        'D': []
    }
    d = dfs(g, 'A')
    b = bfs(g, 'A')
    assert set(d) == {'A', 'B'}
    assert set(b) == {'A', 'B'}
