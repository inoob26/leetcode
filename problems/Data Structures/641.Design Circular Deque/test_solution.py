from solution import MyCircularDeque


def test_solution():
    myCircularDeque = MyCircularDeque(3)
    assert True == myCircularDeque.insertLast(1)
    # return True
    assert True == myCircularDeque.insertLast(2)
    # return True
    assert True == myCircularDeque.insertFront(3)
    # return True
    assert False == myCircularDeque.insertFront(4)
    #  return False, the queue is full.
    assert 2 == myCircularDeque.getRear()
    #  return 2
    assert True == myCircularDeque.isFull()
    #  return True
    assert True == myCircularDeque.deleteLast()
    #  return True
    assert True == myCircularDeque.insertFront(4)
    #  return True
    assert 4 == myCircularDeque.getFront()
    #  return 4
