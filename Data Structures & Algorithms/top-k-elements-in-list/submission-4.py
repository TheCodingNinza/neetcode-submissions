class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        num_freq = {}


        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        freq_group = defaultdict(list)

        for key,val in num_freq.items():
            freq_group[val].append(key)

        count = 0;
        print(freq_group)
        for key in sorted(freq_group, reverse=True):
            values = freq_group[key]
            for value in values:
                if count < k:
                    ans.append(value)
                    count += 1
                else:
                    return ans;    

        return ans    
        