class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1=collections.Counter(s)
        dic2=collections.Counter(t)
        if len(s)!=len(t):return False
        else:
            values=set(s)
            for value in values:
                if dic1[value]!=dic2[value]:
                    return False
            return True