from solution import Solution


def test_solution():
    turnedOn = 1
    expected = [
        "0:01",
        "0:02",
        "0:04",
        "0:08",
        "0:16",
        "0:32",
        "1:00",
        "2:00",
        "4:00",
        "8:00",
    ]
    result = Solution().readBinaryWatch(turnedOn)
    assert expected == result

    turnedOn = 9
    expected = []
    result = Solution().readBinaryWatch(turnedOn)
    assert expected == result
