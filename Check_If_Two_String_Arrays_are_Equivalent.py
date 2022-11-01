"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.



Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""


def arrayStringsAreEqual(word1, word2):
    word_one = ""
    word_two = ""
    for word in word1:
        word_one = word_one + word
    for word in word2:
        word_two = word_two + word
    if word_one == word_two:
        return True
    else:
        return False


# word1 = ["abc", "d", "defg"]
# word2 = ["abcddefg"]
# word1 = ["a", "cb"]
# word2 = ["ab", "c"]
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2))
