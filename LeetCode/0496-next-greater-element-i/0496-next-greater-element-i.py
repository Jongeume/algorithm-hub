class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {n: -1 for n in nums2}
        stack = []

        for i in nums2: 
            if not stack:
                stack.append(i)
            while stack and stack[-1] < i :
                result[stack.pop()] = i
            stack.append(i)
        return [result[n] for n in nums1]


        