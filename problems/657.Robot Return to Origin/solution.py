class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # more faster
        return (moves.count("R") == moves.count("L")) & (
            moves.count("U") == moves.count("D")
        )
        # my solution
        # location = {"x": 0, "y": 0}
        # indx = 0
        # while indx < len(moves):
        #     if moves[indx] == "U":
        #         location["y"] += 1
        #     elif moves[indx] == "D":
        #         location["y"] -= 1
        #     elif moves[indx] == "L":
        #         location["x"] -= 1
        #     elif moves[indx] == "R":
        #         location["x"] += 1
        #     indx += 1
        # return location["x"] == 0 and location["y"] == 0
