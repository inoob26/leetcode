from solution import LFUCache


def test_solution():
    # ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert 1 == cache.get(1)
    cache.put(3, 3)
    assert -1 == cache.get(2)
    assert 3 == cache.get(3)
    cache.put(4, 4)
    assert -1 == cache.get(1)
    assert 3 == cache.get(3)
    assert 4 == cache.get(4)
