def at_most_k_distinct_substring(string,k):
    start = 0 
    end = 0
    max_len = 0
    adict = {}
    while(end < len(string)):
        current_length = 0
        if(string[end] in adict):
            adict[string[end]] += 1
        else:
            adict[string[end]] = 1
        
        
        while(len(adict) > k):
            adict[string[start]] -= 1
            if(adict[string[start]] == 0):
                del adict[string[start]]
            start += 1
        
        max_len = max(current_length,end-start+1)
        end += 1
    return max_len