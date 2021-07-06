class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if(n == 0 or logs is None or len(logs) == 0):
            return []
        res = [0]*n
        stack = []
        prev = 0
        for log in logs:
            strArray = log.split(":")
            curr = int(strArray[2])
            if (strArray[1] == "start"):
                if(len(stack) > 0):
                    x = int(stack[-1])
                    res[x] += curr - prev
                    prev = curr
                stack.append(strArray[0])
            else:
                y = int(stack.pop())
                res[y] += curr-prev+1
                prev = curr+1
        return res
