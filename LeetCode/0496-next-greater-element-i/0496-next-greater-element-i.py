class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {n: -1 for n in nums2}
        stack = []

        for i in nums2: 
            if not stack:
                stack.append(i)
                
            if stack[-1] < i:
                while stack:
                    if stack[-1] < i: 
                        result[stack.pop()] = i
                    else :
                        break
            stack.append(i)
            
        # for j in range(len(nums1)):
        #     nums1[j] = result[nums1[j]]

        return [result[n] for n in nums1]


        