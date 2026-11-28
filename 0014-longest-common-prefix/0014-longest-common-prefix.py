
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        ans = strs[0]

        for s in strs[1:]:
            while not s.startswith(ans):
                ans = ans[:-1]

                if ans == "":
                    return ""

        return ans
