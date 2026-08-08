class Solution:
    def sortArray(self, nums):
        def heapify(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Check if left child is larger
            if left < n and nums[left] > nums[largest]:
                largest = left
            
            # Check if right child is larger
            if right < n and nums[right] > nums[largest]:
                largest = right
            
            # If largest is not root
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)
        
        n = len(nums)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)
        
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # swap
            heapify(nums, i, 0)
        
        return nums
