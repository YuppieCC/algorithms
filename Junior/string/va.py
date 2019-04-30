class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = self._make_dict(s)
        td = self._make_dict(t)
        if sd == td:
            return True
        return False

    def _make_dict(self, dic):
        _d = {}
        for i in dic:
            if i not in _d:
                _d[i] = 1
            _d[i] += 1
        return _d


if __name__ == '__main__':
    s = 'helloworld'
    t = 'worldhelli'
    r = Solution().isAnagram(s, t)
    print(r)
