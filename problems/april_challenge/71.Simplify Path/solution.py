class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for target in path.split("/"):
            if target in ("", "."):
                continue
            if target == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(target)
        return "/" + "/".join(stack)
