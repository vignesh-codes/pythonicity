import hashlib
import bisect


class ConsistentHashLoadBalancer():
    def __init__(self, targets):
        self.targets = sorted(targets)
        self.ring = [self._hash(t) for t in self.targets]

    def _hash(self, s):
        return int(hashlib.md5(s.encode('utf-8')).hexdigest(), 16)

    def _find_target(self, key):
        h = self._hash(key)
        i = bisect.bisect(self.ring, h)
        if i == len(self.ring):
            i = 0
        return self.targets[i]

    def route(self, key):
        return self._find_target(key)