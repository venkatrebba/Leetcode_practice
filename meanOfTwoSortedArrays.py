"""
Median of two sorted arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

@Author: Venkat Rebba <rebba498@gmail.com>
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        l1 = len(nums1)
        l2 = len(nums2)
        nums3 = []
        
        i, j, k = 0, 0, 0
        
        while True:
            
            if i>=l1 or j>=l2:
                break
                
            if nums1[i] >= nums2[j]:
                nums3.append(nums2[j])
                j += 1
                
            else:
                nums3.append(nums1[i])
                i += 1
            
            k += 1
            
        if l1-i > 0:
            nums3.extend(nums1[i:])
            
        if l2-j > 0:
            nums3.extend(nums2[j:])
            
        
        m = len(nums3)//2         
        med = nums3[m] if (len(nums3)%2 == 1) else (nums3[m-1] + nums3[m])/2
        return med
        
        
n1 = [1,2,3]
n2 = [2, 4, 5]

sol = Solution()
print(sol.findMedianSortedArrays(n1, n2))
        