class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        # store index and value into map type
        for inx, value in enumerate(nums):
            if value in m:
                m[value].append(inx)
            else:
                m[value] = [inx]
        # for each value in m, check the diff whether in m
        for value in m:
            diff = target - value
            if diff == value and len(m[value]) >= 2:
                return [m[value][0], m[value][1]]
            elif diff == value and len(m[value]) < 2:
                continue
            if diff in m:
                return [m[value][0], m[diff][0]] if m[value][0] < m[diff][0] else [m[diff][0], m[value][0]]
