#Given two strings a and b, find whether any anagram of string a is a sub-string of string b. For eg: 
#if a = xyz and b = afdgzyxksldfm then the program should return true.
import unittest 

#TODO: better implementation using rolling hash (problem since strings are unbounded, will there be hash collisions)?

def anagram_substring(a, b):
	# substring cannot be greater than string
	if len(a) > len(b):
		return False

	substring_counts = {}
	for letter in a:
		substring_counts[letter] = substring_counts.get(letter, 0) + 1

	print("substring counts: " + str(substring_counts))

	characters_to_match = sum(substring_counts.values())

	print("characters_to_match: " + str(characters_to_match))

	matched_characters_count = 0
	matched_characters = {} 

	for i in range(0, len(b)):
		print("i: " + str(i))
		print("letter: " + str(b[i]))
		# slide the window of the substring across the rest of the string
		# remove the first index to make room for 
		# next index in window
		if i == len(a) and b[i - 1 - len(a)] in matched_characters:
			matched_characters[b[i - 1 - len(a)]] -= 1
			matched_characters_count -= 1

		if b[i] in substring_counts:
			matched_characters[b[i]] = matched_characters.get(b[i], 0) + 1
			matched_characters_count += 1
			print ("matched_characters:" + str(matched_characters))

		# O(ab) time cost
		if matched_characters_count == characters_to_match and substring_counts == matched_characters:
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