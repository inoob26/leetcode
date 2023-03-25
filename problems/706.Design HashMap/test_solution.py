from solution import MyHashMap


def test_solution():
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)
    myHashMap.put(2, 2)

    assert myHashMap.get(1) == 1
    assert myHashMap.get(3) == -1

    myHashMap.put(2, 1)
    assert myHashMap.get(2) == 1
    myHashMap.remove(2)
    assert myHashMap.get(2) == -1
