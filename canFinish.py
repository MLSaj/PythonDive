class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[]]*numCourses
        ranks = [0] *numCourses
        for item1,item2 in prerequisites:
            if(len(graph[item2]) > 0):
                graph[item2] += [item1]
            else:
                graph[item2] = [item1]
            ranks[item1] += 1

        queue = []
        for i in range(len(ranks)):
            if(ranks[i] == 0):
                queue.append(i)

        while(len(queue) != 0):
            #print(queue)
            item = queue.pop()
            numCourses -= 1
            for neighbor in graph[item]:
                ranks[neighbor] -= 1
                if(ranks[neighbor] <= 0):
                    queue.append(neighbor)
        return numCourses <= 0