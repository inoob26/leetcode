from typing import List



class ATM:
    def __init__(self):
        # [0, 1,   0,   1,   1]
        # 20, 50, 100, 200, 500
        self._nominations_map = {
            20: 0,
            50: 0,
            100: 0,
            200: 0,
            500: 0
        }


    def deposit(self, banknotesCount: List[int]) -> None:
        if not banknotesCount or len(banknotesCount) < 5:
            return
        mapper = [(0, 20), (1, 50), (2, 100), (3, 200), (4, 500)]
        for indx, k in mapper:
            self._nominations_map[k] += banknotesCount[indx]

    def withdraw(self, amount: int) -> List[int]:
        res = [0,0,0,0,0]
        mapper = [
            (500, 4),
            (200, 3),
            (100, 2),
            (50, 1),
            (20, 0),
        ]
        nom_lst = []  # (nom, count)

        tmp = amount
        for nom, res_indx in mapper:
            if tmp ==0: break

            available = self._nominations_map[nom]
            if not available: continue
            # берём не больше, чем нужно по сумме, и не больше, чем есть в наличии
            nom_count = min(tmp // nom, available)
            nom_lst.append((nom, nom_count))
            res[res_indx] += nom_count
            tmp -= (nom * nom_count)
        
        if tmp > 0: return [-1]

        for nom, count in nom_lst:
            self._nominations_map[nom] -= count

        return res


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
