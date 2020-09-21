class Solution:
    def countLargestGroup(self, n: int) -> int:
        hm = {}
        prev = 0
        for i in range(1, n+1):
            if(i % 10):
                sd = prev+1
            else:
                conv = str(i)
                sd = 0
                for i in conv:
                    sd += int(i)
            if(sd in hm):
                hm[sd] += 1
            else:
                hm[sd] = 1
            prev = sd
        #print(hm)
        ans = max(hm.values())
        final = list(hm.values()).count(ans)
        return final
