class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums == []:
            return False

        numSet = set()
        
        for i,v in enumerate(nums):
            if v in numSet:
                return True
            else:
                numSet.add(v)
        return False
        




