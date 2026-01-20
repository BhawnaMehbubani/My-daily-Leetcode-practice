class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[2,7,11,15]
        dic = {}
        for i in range(len(nums)): 
            #dict{nums[i]}=i #[2:0,7:1,11:2,15:3]
            diff=target-nums[i] #17-2=15 #17-15=2

            if diff in dic.keys():
                return [dic[diff],i]
            else:
                dic[nums[i]] = i




