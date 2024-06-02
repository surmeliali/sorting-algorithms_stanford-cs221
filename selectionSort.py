''' Selection Sort '''

# The idea is to keep track on the index which has the min value and the index of the outer loop

nums = [1, 4, 0, 1, 8, 9, 7, 232, 5]

# ascending selection sort


def selectionSort(nums):
    for i in range(len(nums)):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j

        temp = nums[i]
        nums[i] = nums[minIndex]

        nums[minIndex] = temp

    return nums


# test the function
print(selectionSort(nums))
