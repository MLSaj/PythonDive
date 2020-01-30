def longest_consecutive_sequence(nums):
    num_dict = {}
    max_length = 0
    for num in nums:
        num_dict[num] = 1
        
    for i in range(len(nums)):
        if nums[i]-1 not in num_dict:
            current_streak = 1
            current_num = nums[i]
            while(current_num + 1 in num_dict):
                current_streak += 1
                current_num += 1
            max_length = max(max_length,current_streak)
    
    return max_length  