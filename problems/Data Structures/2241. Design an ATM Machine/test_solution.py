from solution import ATM

def test_solution():
    atm = ATM()
    atm.deposit([0,0,1,2,1])
    res = atm.withdraw(600)
    assert res == [0,0,1,0,1]

    atm.deposit([0,1,0,1,1])
    res = atm.withdraw(600)
    assert res == [-1]

    res = atm.withdraw(550)
    assert res == [0,1,0,0,1]


def test_solution_2():
    atm = ATM()
    atm.deposit([0,10,0,3,0])

    res = atm.withdraw(500)
    assert res == [0,2,0,2,0]