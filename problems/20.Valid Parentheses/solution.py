class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in ("(", "{", "["):
                stack.append(item)
            else:
                if len(stack) >= 1 and (
                    (item == ")" and stack[-1] == "(")
                    or (item == "}" and stack[-1] == "{")
                    or (item == "]" and stack[-1] == "[")
                ):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


# more elegant solution
def isValid(self, s):
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []
