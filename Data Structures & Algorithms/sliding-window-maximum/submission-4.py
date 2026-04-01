class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()

        n = len(nums)

        ans = []

        for i in range (k):
            curr_elem = nums[i]
            if not deq:
                deq.append(i)
            else:
                if nums[deq[-1]] < curr_elem:
                    while deq and nums[deq[-1]] < curr_elem:
                        deq.pop()        
                deq.append(i)    

        ans.append(nums[deq[0]])

        for i in range(k, n):
            curr_elem = nums[i]
            if nums[deq[-1]] < curr_elem:
                    while deq and nums[deq[-1]] < curr_elem:
                        deq.pop()        
            deq.append(i)
            if deq and deq[0] == (i - k):
                deq.popleft()
            
            ans.append(nums[deq[0]])

        return ans        


