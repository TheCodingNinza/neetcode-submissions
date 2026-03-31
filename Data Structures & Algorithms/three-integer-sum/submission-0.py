class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        start = 0
        end = len(nums) - 1

        lookup = set()

        for i in range(len(nums) - 2):
            target =  - nums[i]
            lookup.clear()
            for j in range(i+1, len(nums), 1):
                if target - nums[j] in lookup:
                    temp = [-target, target - nums[j], nums[j]]
                    temp.sort()
                    ans.append(temp)
                else:
                    lookup.add(nums[j])    
        return [list(a) for a in set(tuple(x) for x in ans)]            



        