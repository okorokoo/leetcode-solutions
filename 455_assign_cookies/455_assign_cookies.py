class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        s = sorted(s)[::-1]
        g = sorted(g)[::-1]
        for _g in g:
            if not s:
                break
            if s[0] >= _g:
                count += 1
                s.remove(s[0])
        return count