"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""Given a string, find the length of the longest substring without repeating characters.
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.
Given bpfbhmipx the answer is 7."""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_map = {}
        starting_index_of_the_curr_substring, len_of_the_curr_substring, len_of_the_longest_substring = 0, 0, 0
        for i, v in enumerate(s):
            if v in index_map:
                starting_index_of_the_curr_substring = index_map[v] + 1
            len_of_the_curr_substring = i - starting_index_of_the_curr_substring + 1
            len_of_the_longest_substring = max(len_of_the_longest_substring, len_of_the_curr_substring)
            index_map[v] = i
        return len_of_the_longest_substring


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abba"))
    print(solution.lengthOfLongestSubstring("bpfbhmipx"))
