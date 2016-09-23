class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        X0 = 0
        X1 = 1
        HEIGHT = 2
        building_stack = []
        ret = []

        for b in buildings:
            if building_stack:
                peek = building_stack[0]

                # non overlapping region:
                if peek[X1] <= b[X0]:
                    building_stack.pop()
                    if peek[X1] != b[X0]:
                        ret.append([peek[X1], 0])
                    building_stack.insert(0, b)
                # heights equal and overlapping region
                if peek[X0] <= b[X0] <= peek[X1] and b[HEIGHT] == peek[HEIGHT]:
                    peek[X1] = b[X1]
                # height of next building greater and overlapping region
                elif peek[X0] <= b[X0] < peek[X1] <= b[X1] and b[HEIGHT] > peek[HEIGHT]:
                    ret.append([b[X0], b[HEIGHT]])
                    building_stack.pop()
                    building_stack.insert(0, [b[X1], b[X1], b[HEIGHT]])
                # height of next building smaller and overlapping region
                elif peek[X0] <= b[X0] < peek[X1] <= b[X1] and b[HEIGHT] < peek[HEIGHT]:
                    ret.append([peek[X1], b[HEIGHT]])
                    building_stack.pop()
                    building_stack.insert(0, [peek[X1], b[X1], b[HEIGHT]])
                # height of next building greater and contained in peek
                elif peek[X0] <= b[X0] <= b[X1] <= peek[X1] and b[HEIGHT] > peek[HEIGHT]:
                    ret.append([peek[X0], peek[HEIGHT]])
                    ret.append([b[X0], b[HEIGHT]])
                    building_stack.insert(0, b)
                # height of next building smalelr and contained in peek
                elif peek[X0] <= b[X0] <= b[X1] <= peek[X1] and b[HEIGHT] < peek[HEIGHT]:
                    pass #do nothing
            else:
                ret.append([b[X0], b[HEIGHT]])
                building_stack.insert(0, b)

        print building_stack

        ret.append([buildings[-1][X1], 0])

        return ret


