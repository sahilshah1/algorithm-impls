# Given two strings a and b, find whether any anagram of string a is a sub-string of string b. For eg:
# if a = xyz and b = afdgzyxksldfm then the program should return true.
import unittest

# TODO: better implementation using rolling hash (problem since strings are unbounded, will there be hash collisions)?

def anagram_substring(substring, string):
    # substring cannot be greater than string
    if len(substring) > len(string):
        return False

    substring_char_counts = {}
    for letter in substring:
        substring_char_counts[letter] = substring_char_counts.get(letter, 0) + 1

    matched_char_counts = {}

    for i in xrange(0, len(string)):
        # slide the window of the substring across the rest of the string
        # remove the first index to make room for
        # next index in window
        start_index_of_window = i - 1 - len(substring)
        if i == len(substring) and string[start_index_of_window] in matched_char_counts:
            matched_char_counts[string[start_index_of_window]] -= 1

        if string[i] in substring_char_counts:
            matched_char_counts[string[i]] = matched_char_counts.get(string[i], 0) + 1

        # O(ab) time cost
        if substring_char_counts == matched_char_counts:
            return True

    return False


class TestAnagramSubstring(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(anagram_substring("a", "aaa"))

    def test_basic_not_found(self):
        self.assertFalse(anagram_substring("b", "aaa"))

    def test_basic_anagram(self):
        self.assertTrue(anagram_substring("ab", "gbaa"))

    def test_anagram_is_past_window(self):
        self.assertTrue(anagram_substring("ab", "fssdba"))

    def test_anagram_is_in_second_window(self):
        self.assertTrue(anagram_substring("ab", "ffba"))

    def test_anagram_with_repeated_letters(self):
        self.assertFalse(anagram_substring("aab", "bab"))

    def test_anagram_character_count_incorrect_then_correct(self):
        self.assertTrue(anagram_substring("aab", "aaaba"))


if __name__ == '__main__':
    unittest.main()
