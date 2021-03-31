#https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if (len(strs) == 0):
            return ''
    
        if (len(strs) == 1):
            return strs[0]
        
        preffix = ''
        word = strs[0]
        j = 0
        preffix_found = False
        
        while (preffix_found == False):
            letter_count = 0
            for i in range(1, len(strs)):
                tmp = strs[i]
                if ( j < len(word) and j < len(tmp)):
                    if (word[j] == tmp[j]):
                        letter_count += 1
                    else:
                        break
                else:
                    break
            if (letter_count == len(strs)-1):
                preffix += word[j]
                j+= 1
            else:
                preffix_found = True
        
        return preffix