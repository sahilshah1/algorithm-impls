# # https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
import unittest


def length_of_longest_substring(s):
    if not s:
        return 0

    start = 0
    max_len = 0
    letter_to_index = {}
    for index, letter in enumerate(s):
        if letter in letter_to_index:
            # just repeated a letter, save the current substring if it's longer than the previously
            # longest one. do not add 1 to index - start to avoid including repeated letter
            max_len = max(index - start, max_len)

            # since this letter is repeated, anything up to and including the previous occurrence
            # of the letter is invalid, so find the next valid index. the current longest substring
            # will start at the highest index of the letter_to_index, as that's the only valid index
            start = max(start, letter_to_index[letter] + 1)

        letter_to_index[letter] = index

    return max(max_len, len(s) - start)


class LongestSubstringWithoutRepeatsTest(unittest.TestCase):

    def test_one_longest(self):
        solution = length_of_longest_substring("abcabcbb")

        self.assertEquals(3, solution)

    def test_one_character_repeats(self):
        solution = length_of_longest_substring("bbbbbbb")

        self.assertEquals(1, solution)

    def test_one_repeat_in_a_row(self):
        solution = length_of_longest_substring("pwwkew")

        self.assertEquals(3, solution)

    def test_empty(self):
        solution = length_of_longest_substring("")

        self.assertEquals(0, solution)

    def test_abba(self):
        solution = length_of_longest_substring("abba")

        self.assertEquals(2, solution)

    def test_dvdf(self):
        solution = length_of_longest_substring("dvdf")

        self.assertEquals(3, solution)

if __name__ == '__main__':
    unittest.main()
