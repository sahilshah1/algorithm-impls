# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have
# to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
# return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0.
#  So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
# Another correct ordering is[0,2,1,3].
#

import unittest

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for i in xrange(0, numCourses):
            graph[i] = {"has_prereqs": set(),
                             "is_prereq_for": set()}

        for prereq in prerequisites:
            course = prereq[0]
            req = prereq[1]
            
            graph[course]["has_prereqs"].add(req)
            graph[req]["is_prereq_for"].add(course)

        courses = []

        courses_with_no_prereqs = filter(lambda x: not graph[x]["has_prereqs"], graph.keys())
        while courses_with_no_prereqs:

            courses.append(courses_with_no_prereqs.pop(0))

            if len(courses) == numCourses:
                return courses

            for next_course in graph[courses[-1]]["is_prereq_for"]:
                graph[next_course]["has_prereqs"].remove(courses[-1])
                if not graph[next_course]["has_prereqs"]:
                    courses_with_no_prereqs.append(next_course)

        return []


class CourseScheduleIITest(unittest.TestCase):


    def test_find_order_basic(self):

        order = Solution().findOrder(2, [[1,0]])

        self.assertEquals(order, [0, 1])

    def test_key_error(self):
        order = Solution().findOrder(4,  [[0, 1], [3, 1], [1, 3], [3, 2]])

        self.assertEquals(order, [])


if __name__ == '__main__':
    unittest.main()