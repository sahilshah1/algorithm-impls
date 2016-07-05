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
    sub_problems = [[] for _ in xrange(len(value))]
    decode_helper(value, sub_problems, 0)
    return sub_problems[0]


def decode_helper(original_string, sub_problems, cursor):
    def int_to_char(x): return chr(int(x) + 96)

    # if no more characters to decode, or sub problem already solved return
    if cursor == len(original_string) or sub_problems[cursor]:
        print ("Stopped? " + str(cursor))
        return

    # advance cursor past first letter and recurse
    print ("Recursing on: " + original_string[cursor:])
    decode_helper(original_string, sub_problems, cursor + 1)
    first_letter = int_to_char(original_string[cursor])

    if cursor < len(original_string) - 1:
        sub_problems[cursor].extend([first_letter + decoded_string for decoded_string in sub_problems[cursor + 1]])
    else:
        sub_problems[cursor].append(first_letter)

    # print ("Sub problem: " + str(cursor) + " on char " + first_letter)
    # print ("Next sub problem on cursor:" + str(cursor + 1))
    # print ("All sub problem: ")
    # print (sub_problems)

    # check if first 2 letters can be decoded
    if cursor < len(original_string) - 2:
        first_two_letters = original_string[cursor:cursor + 2]
        print ("first two: " + str(first_two_letters))
        if (int(first_two_letters)) <= 26:
            first_two_letters = int_to_char(first_two_letters)
            decode_helper(original_string, sub_problems, cursor + 2)
            # append the current 2 letters to all the strings retrieved in the next sub problem
            # save the appended strings as the solution for this current problem
            if cursor < len(original_string) - 2:
                sub_problems[cursor].extend(
                    [first_two_letters + decoded_string for decoded_string in sub_problems[cursor + 2]])
            else:
                sub_problems[cursor].append(first_two_letters)

            print ("Sub problem: " + str(cursor) + " on char " + first_two_letters)
            print ("Next sub problem on cursor:" + str(cursor + 2))
            print ("All sub problem: ")
            print (sub_problems)


class TestFindExtrema(unittest.TestCase):

    def test_basic(self):
        expected_strings = set(['aabc', 'aaw', 'alc', 'kbc', 'kw'])

        actual_strings = set(decode("1123"))

        self.assertEquals(actual_strings, expected_strings)

if __name__ == '__main__':
    unittest.main()