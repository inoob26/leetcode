from solution import MinStack


def test_solution():
    stack = MinStack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    stack.pop()
    assert 3 == stack.top()
    assert 1 == stack.getMin()
