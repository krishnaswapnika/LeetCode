class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            i = L
            j = 0
            k = 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
                
        def mergeSort(arr, L, R):
            if L >= R:
                return
            M = (L + R) // 2
            mergeSort(arr, L, M)
            mergeSort(arr, M + 1, R)
            merge(arr, L, M, R)
        mergeSort(nums, 0, len(nums) - 1)
        return nums

