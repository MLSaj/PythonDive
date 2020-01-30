from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
            #Two pointer approach
        if not t or not s:
                return ""
        start = 0
        end = 0
        hash_set = Counter(t)

        find_set = {}
        required = len(hash_set)
        formed = 0
        answer = (float("inf"),0, 0)

        while(end < len(s)):
            end_char = s[end]
            if end_char in hash_set:
                if end_char in find_set:
                    find_set[end_char] += 1
                else:
                    find_set[end_char] = 1

                if(find_set[end_char] == hash_set[end_char]):
                    formed += 1



            while(formed == required):
                if(end-start+1 < answer[0]):
                    answer = (end-start+1, start,end)
                    print(answer)


                start_char = s[start]

                if(start_char in hash_set):
                    find_set[start_char] -= 1

                    if(find_set[start_char] < hash_set[start_char]):
                        formed -= 1
                start += 1


            end += 1

        if answer[0] == float("inf"):
            return ""
        else:
            return s[answer[1] : answer[2] + 1]