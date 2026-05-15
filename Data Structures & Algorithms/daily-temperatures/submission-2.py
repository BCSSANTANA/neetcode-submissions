class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack:
                top = stack[-1]
                while stack and temperatures[i] > top[0]:
                    top = stack.pop()
                    res[top[1]] = i - top[1]
                    if stack:
                        top = stack[-1]
            
            stack.append((temperatures[i], i))
        return res