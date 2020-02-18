class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        asum = 0
        hash_map = {}
        hash_map[0] = 1
        for i in range(len(nums)):
            asum += nums[i]
            if(asum-k in hash_map):
                count += hash_map[asum-k]
            if asum in hash_map:
                hash_map[asum] += 1
            else:
                hash_map[asum] = 1
        return count
        