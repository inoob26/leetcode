from solution import Node, Solution


def get_values(node: Node):
    queue = [node]
    result = []
    seen = set()
    while queue:
        curr = queue.pop(0)
        if curr in seen:
            continue
        new_vals = []
        for neighbor in curr.neighbors:
            new_vals.append(neighbor.val)
            queue.append(neighbor)
        result.append(new_vals)
        seen.add(curr)
    return result[1:]


def test_solution():
    root = Node()
    a = Node(1, [])
    b = Node(2, [])
    c = Node(3, [])
    d = Node(4, [])

    a.neighbors.append(b)
    a.neighbors.append(d)

    b.neighbors.append(a)
    b.neighbors.append(c)

    c.neighbors.append(b)
    c.neighbors.append(d)

    d.neighbors.append(a)
    d.neighbors.append(c)

    root.neighbors.append(a)
    root.neighbors.append(b)
    root.neighbors.append(c)
    root.neighbors.append(d)

    result = Solution().cloneGraph(root)
    expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
    assert result != root
    assert expected == get_values(result)


test_solution()
