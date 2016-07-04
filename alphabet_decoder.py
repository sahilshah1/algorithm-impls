# If a=1, b=2, c=3,....z=26, given a string, find all possible codes that string can generate.
# Give a count as well as print the strings.
#
# For example:
# Input: "1123". You need to general all valid alphabet codes from this string.
#
# Output List
# aabc //a = 1, a = 1, b = 2, c = 3
# kbc // since k is 11, b = 2, c= 3
# alc // a = 1, l = 12, c = 3
# aaw // a= 1, a =1, w= 23
# kw // k = 11, w = 23
import unittest


def decode(value):
    return decode_helper(value, "")


def decode_helper(original_code, decoded, total_strings=set()):
    int_to_char = lambda x: chr(int(x) + 96)

    # if no more characters to decode, print decoded string and return 1 as count
    if len(original_code) == 0:
        print decoded
        total_strings.add(decoded)
        return 1

    count = 0
    if len(original_code) >= 1:
        first_letter = original_code[0]
        count += decode_helper(original_code[1:], decoded + int_to_char(first_letter), total_strings)

    if len(original_code) >= 2:
        first_two_letters = original_code[0:2]
        if (int(first_two_letters)) <= 26:
            count += decode_helper(original_code[2:], decoded + int_to_char(first_two_letters), total_strings)

    return count


class TestFindExtrema(unittest.TestCase):

    def test_basic(self):
        expected_strings = set(['aabc', 'aaw', 'alc', 'kbc', 'kw'])

        actual_strings = set()
        count = decode_helper("1123", "", actual_strings)

        self.assertEqual(count, 5)
        self.assertEquals(actual_strings, expected_strings)

if __name__ == '__main__':
    unittest.main()