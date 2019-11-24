class Solution:
    def subsets(self, nums):
        results = set()
        nums.sort()
        queue = [([nums[i]], nums[:i] + nums[i+1:]) for i in range(len(nums))]
        
        
        while queue:
            probable_result, not_visited = queue.pop()
            probable_result.sort()
            
            print(probable_result, not_visited)

            results.add(tuple(probable_result))

            for i in not_visited:
                pr = probable_result.copy()
                pr.append(i)
                if pr not in queue and tuple(pr) not in results:
                    n = not_visited.copy()
                    n.remove(i)
                    queue.append((pr, n))
                        
        results.add(())                 
        return results

s = Solution()
print("result",s.subsets([1,2,3,4,5,6,7,8,9,10]))

