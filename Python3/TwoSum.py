class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(0, len(nums)):
            dic[nums[i]] = i

        print(dic)
        for j in range(0, len(nums)):
            pair = target - nums[j]
            if((dic.get(pair,"DNE") != "DNE") and (j != dic[pair])):
                return [j, dic[pair]]
        return 0
        
### Test case ###
nums = [2,7,11,15]
target = 22

out = Solution()
print(out.twoSum(nums,target))