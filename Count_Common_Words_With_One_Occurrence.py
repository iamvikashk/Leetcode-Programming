"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.



Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".

"""


class Solution:
    def countWords(self, words1: [str], words2: [str]) -> int:
        matching_words = []
        one_word = []
        for word in words1:
            if self.checkCount(word, words1):
                if self.checkAltList(word, words1):
                    matching_words.append(word)
        for word in words2:
            if self.checkCount(word, words2):
                if self.checkAltList(word, words2):
                    matching_words.append(word)
        for word in matching_words:
            if self.checkMatchingCount(word, matching_words):
                one_word.append(word)

        return len(set(one_word))

    def checkCount(self, word, words):
        if words.count(word) == 1:
            return True
        else:
            return False

    def checkAltList(self, word, words):
        if word in words:
            return True
        else:
            return False

    def checkMatchingCount(self, word, words):
        if words.count(word) > 1:
            return True
        else:
            return False


words1 = ["leetcode", "is", "amazing", "as", "is"]
words2 = ["amazing", "leetcode", "is"]
# words1 = ["b","bb","bbb"]
# words2 = ["a","aa","aaa"]
# words1 = ["a", "ab"]
# words2 = ["a", "a", "a", "ab"]

cw = Solution()

print(cw.countWords(words1, words2))
