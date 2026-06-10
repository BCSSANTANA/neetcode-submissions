class TimeMap:

    def __init__(self):
        self.s = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.s[key] = []
        self.s[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.s:
            return ""
        t = self.s[key]
        l = 0
        r = len(t) - 1
        c = (l + r) // 2
        res = [-float("inf"), ""]
        while l <= r:
            c = (l + r) // 2
            if t[c][0] == timestamp:
                return t[c][1]
            if t[c][0] > res[0] and t[c][0] <= timestamp:
                res[0] = t[c][0]
                res[1] = t[c][1]
            if timestamp < t[c][0]:
                r = c - 1
            else:
                l = c + 1
        return res[1]