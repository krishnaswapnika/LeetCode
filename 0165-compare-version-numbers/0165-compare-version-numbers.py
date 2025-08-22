class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = [int(x) for x in version1.split('.')]
        v2_parts = [int(x) for x in version2.split('.')]
        n = max(len(v1_parts), len(v2_parts))
        for i in range(n):
            v1 = v1_parts[i] if i<len(v1_parts) else 0
            v2 = v2_parts[i] if i<len(v2_parts) else 0
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
        return 0