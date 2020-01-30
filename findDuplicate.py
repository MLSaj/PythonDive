for i in range(len(nums)):
    #print(nums[i])
    number = abs(nums[i]) -1
    if(nums[number] < 0):
        print(abs(nums[i]))
        break;
    else:
        nums[number] = -1 * nums[number]