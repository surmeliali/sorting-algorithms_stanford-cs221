''' Insertion Sort '''

# the idea is to keep swaping the elements while iterating through the list. Unlike selection sort, here you are iterating thru the sorted list each time.

nums = [1, 4, 0, 1, 8, 9, 7, 232, 5]


def insertionSort(nums):
    for i in range(1, len(nums)):
        # must add i > 0, python allows negative indexing
        while nums[i-1] > nums[i] and i > 0:
            # Pythonic way of doing the below operation (swapping) is nums[i], nums[i-1] = nums[i-1], nums[i]
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
            # check the next left
            i = i - 1

    return nums


# test case
print(insertionSort(nums))
