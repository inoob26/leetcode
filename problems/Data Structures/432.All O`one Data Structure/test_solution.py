from solution import AllOne


def test_solution():
    allOne = AllOne()
    allOne.inc("hello")
    allOne.inc("hello")
    assert "hello" == allOne.getMaxKey()
    assert "hello" == allOne.getMinKey()
    allOne.inc("leet")
    assert "hello" == allOne.getMaxKey()
    assert "leet" == allOne.getMinKey()

    allOne = AllOne()
    allOne.inc("hello")
    allOne.inc("goodbye")
    allOne.inc("hello")
    allOne.inc("hello")
    assert "hello" == allOne.getMaxKey()
    allOne.inc("leet")
    allOne.inc("code")
    allOne.inc("leet")
    allOne.dec("hello")
    allOne.inc("leet")
    allOne.inc("code")
    allOne.inc("leet")
    assert "leet" == allOne.getMaxKey()
