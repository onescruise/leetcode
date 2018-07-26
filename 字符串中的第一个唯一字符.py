class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic=collections.Counter(s)#统计字符串中的各字符对应的个数，做成字典
        for i in range(len(s)):
            if dic[s[i]]==1:return i
        return -1