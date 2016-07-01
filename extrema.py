import unittest

# Find the length of the longest strictly increasing or strictly decreasing sub-sequence in a sequence.
def findExtrema(arr):
	if arr is None or arr == []:
		return 0

	if len(arr) == 1:
		return 1 # makes logic in the for loop simpler

	index_of_first_extrema = 0
	index_of_second_extrema = 0
	for index, value in enumerate(arr):
		is_extrema = False

		# bounds of array are always extrema
		if index == 0:
			is_extrema = arr[index] != arr[index + 1] # only check the next index for the left bound
		if index == len(arr) - 1:
			is_extrema = arr[index] != arr[index - 1] # only check the previous index for the right bound
		else:
			# check if slope changes from positive, i.e. on index 2: [1,2,3,3]
			is_max_extrema = arr[index - 1] < arr[index] and arr[index] >= arr[index + 1]
			# check if slope changes from negative, i.e. on index 2: [3,2,1,1]
			is_min_extrema = arr[index - 1] > arr[index] and arr[index] <= arr[index + 1]
			is_extrema = is_min_extrema or is_max_extrema

		if is_extrema:
			old_longest_length = index_of_second_extrema - index_of_first_extrema
			new_longest_length = index - index_of_second_extrema

			if (new_longest_length > old_longest_length):
				index_of_first_extrema = index_of_second_extrema
				index_of_second_extrema = index

	# add 1 to include the index of the extrema
	return index_of_second_extrema - index_of_first_extrema + 1

class TestFindExtrema(unittest.TestCase):

    def test_increasing(self):
    	self.assertEqual(findExtrema([1,2,3,4]), 4)

    def test_decreasing(self):
    	self.assertEqual(findExtrema([4,3,2,1]), 4)

    def test_increasing_then_level(self):
    	self.assertEqual(findExtrema([1,2,3,3]), 3)

    def test_decreasing_then_level(self):
    	self.assertEqual(findExtrema([3,2,1,1]), 3)

    def test_more_increasing_than_decreasing(self):
    	self.assertEqual(findExtrema([1,2,3,4,1]), 4)

    def test_two_strictly_increasing(self):
    	self.assertEqual(findExtrema([1,2,3,4,1,2,3,4,5]), 6)

    def test_flat(self):
    	self.assertEqual(findExtrema([3,3,3]), 1)

    def test_empty(self):
    	self.assertEqual(findExtrema([]), 0)

    def test_singular(self):
    	self.assertEqual(findExtrema([4]), 1)

if __name__ == '__main__':
    unittest.main()