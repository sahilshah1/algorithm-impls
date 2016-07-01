import unittest
# There is an island which is represented by square matrix NxN. 
#A person on the island is standing at any given co-ordinates (x,y). He can move in any direction one step right, left, up, down on the island. If he steps outside the island, he dies. 
#
#Let island is represented as (0,0) to (N-1,N-1) (i.e NxN matrix) & person is standing at given co-ordinates (x,y). He is allowed to move n steps on the island (along the matrix). What is the probability that he is alive after he walks n steps on the island? 

#Write a psuedocode & then full code for function 
#" float probabilityofalive(int x,int y, int n) ".

def probability_of_alive(x, y, n, N):
	(valid_paths, invalid_paths) = calculate_valid_and_invalid_paths(x, y, n, N, 0, 0)
	return float(valid_paths) / (valid_paths + invalid_paths)


def calculate_valid_and_invalid_paths(x, y, n, N, valid_paths, invalid_paths):

	# if x,y is invalid, return that the current path is invalid
	if not ((0 <= x and x < N) and (0 <= y and y < N)):
		return (valid_paths, invalid_paths + 1)
	# if x,y is valid, and there are no more steps to take, return that the path is valid
	elif n == 0 and ((0 <= x and x < N) and (0 <= y and y < N)):
		return (valid_paths + 1, invalid_paths)
	# recurse in each direction 
	else:
		left_direction_paths = calculate_valid_and_invalid_paths(x - 1, y, n - 1, N, valid_paths, invalid_paths)
		right_direction_paths = calculate_valid_and_invalid_paths(x + 1, y, n - 1, N, valid_paths, invalid_paths)
		up_direction_paths = calculate_valid_and_invalid_paths(x, y - 1, n - 1, N, valid_paths, invalid_paths)
		down_direction_paths = calculate_valid_and_invalid_paths(x, y + 1, n - 1, N, valid_paths, invalid_paths)

		valid_paths += sum(x[0] for x in (left_direction_paths, right_direction_paths, up_direction_paths, down_direction_paths))
		invalid_paths += sum(x[1] for x in (left_direction_paths, right_direction_paths, up_direction_paths, down_direction_paths))

	return (valid_paths, invalid_paths)

# TODO: this will not work! this is just the ratio of valid paths to invalid paths. the probability of x,y to some step is multiplication


class TestPathFinder(unittest.TestCase):

    def test_increasing(self):
    	x = 0
    	y = 0
    	n = 3
    	N = 2

    	valid_paths, invalid_paths = calculate_valid_and_invalid_paths(x, y, n, N, 0, 0)

    	self.assertEqual(valid_paths, 2)


if __name__ == '__main__':
    unittest.main()



