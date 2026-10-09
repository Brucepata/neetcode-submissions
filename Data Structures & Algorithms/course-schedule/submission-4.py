from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()
        course_dict = dict()

        for i in range(numCourses):
            course_dict[i] = deque([])

        for crs, prq in prerequisites:
            course_dict[crs].append(prq)

        for i in range(numCourses):
            if not self.dfs(i, course_dict, visited, visiting):
                return False

        return True

    def dfs(self, i, course_map, visited, visiting):

        if i in visiting:
            return False

        if i in visited:
            return True

        visiting.add(i)

        for prereq in course_map[i]:
            dfs_res = self.dfs(prereq, course_map, visited, visiting)
            if not dfs_res:
                return False

        visiting.remove(i)
        visited.add(i)

        return True


        