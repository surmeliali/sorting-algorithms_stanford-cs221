''' Merge Sort'''

# it is a tree based sorting algorithm. divide the list in a half until you have one element in each list. Then combine the lists while
# sorting the elements (Divide and Conquer)
# O(n log n)

nums = [3, 2, 4, 5]


def mergeSort(nums, leftIndex, rightIndex):
    if leftIndex >= rightIndex:
        return

    # get the middle value
    middle = (leftIndex + rightIndex) // 2
    # left side of the tree
    mergeSort(nums, leftIndex, middle)
    # right side of the tree
    mergeSort(nums, middle+1, rightIndex)
    merge(nums, leftIndex, rightIndex, middle)


def merge(nums, leftIndex, rightIndex, middle):
    print(middle)
    leftArray = nums[leftIndex:middle+1]
    rightArray = nums[middle+1:rightIndex+1]

    # left and right pointers
    currentLeft = 0
    currentRight = 0
    sortedIndex = leftIndex

    # go thru the both arrays until no element left at least one of them
    while currentLeft < len(leftArray) and currentRight < len(rightArray):
        if leftArray[currentLeft] < rightArray[currentRight]:
            nums[sortedIndex] = leftArray[currentLeft]
            currentLeft += 1

        else:
            nums[sortedIndex] = rightArray[currentRight]
            currentRight += 1

        sortedIndex += 1

    # check if any element has left for the leftArray
    while currentLeft < len(leftArray):
        nums[sortedIndex] = leftArray[currentLeft]
        currentLeft += 1
        sortedIndex += 1

    # check if any element has left for the rightArray
    while currentRight < len(rightArray):
        nums[sortedIndex] = rightArray[currentRight]
        currentRight += 1
        sortedIndex += 1


# test case
mergeSort(nums, 0, len(nums) - 1)
print(nums)
