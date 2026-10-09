import time

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        start_time = time.perf_counter()
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            # preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        print(f"Runtime: {execution_time:.6f} seconds")