# https://leetcode.com/problems/combination-sum-iii/
#
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Example 1:
# Input: k = 3, n = 7
# Output:
# [[1,2,4]]
#
# Example 2:
# Input: k = 3, n = 9
# Output:
# [[1,2,6], [1,3,5], [2,3,4]]
import unittest


def combination_sum(k, n):

    def combination_sum_helper(current_solution, sum_of_current_solution, k):
        if k == 0:
            return

        for i in xrange(current_solution[-1] + 1 if current_solution else 1, 10):
            copied = list(current_solution)

            # if the next number will equal n and there is space for 1 more number,
            # then this is a valid solution
            if sum_of_current_solution + i == n and k == 1:
                copied.append(i)
                all_solutions.append(copied)
                return  # no other numbers will be valid if this one works

            # if the next number is less than n, and there is space for 1+ numbers,
            # then a valid solution may still exist. recurse
            elif sum_of_current_solution + i < n and k > 1:
                copied.append(i)
                combination_sum_helper(copied, sum_of_current_solution + i, k - 1)

    all_solutions = []
    combination_sum_helper([], 0, k)
    return all_solutions


class CombinationSumTest(unittest.TestCase):

    def test_one_combination(self):
        expected = [[1, 2, 4]]
        solutions = combination_sum(3, 7)

        self.assertEquals(solutions, expected)

    def test_multiple_combinations(self):
        expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        solutions = combination_sum(3, 9)
        self.assertEquals(solutions, expected)

    def test_no_combinations(self):
        expected = []
        solutions = combination_sum(3, 3)
        self.assertEquals(solutions, expected)

    def test_multiple_combinations_2(self):
        expected = [[1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6],
                    [2, 3, 7], [2, 4, 6], [3, 4, 5]]
        solutions = combination_sum(3, 12)
        self.assertEquals(solutions, expected)

if __name__ == '__main__':
    unittest.main()
