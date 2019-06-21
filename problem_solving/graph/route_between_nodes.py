from queue import Queue


def route_between_nodes(graph: dict, start, end) -> bool:

    q = Queue()
    q.put([start])

    visited = set()
    visited.add(start)

    while not q.empty():

        path = q.get()

        for vertex in graph[path[-1]]:

            route = path + [vertex]

            if vertex not in visited:
                visited.add(vertex)
                q.put(route)

            if vertex == end:
                return True

    return False
