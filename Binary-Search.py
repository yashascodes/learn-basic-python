def binary_search(nums, target):
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid - 1
    else:
      high = mid - 1


list = [1,2,3,4,5]

print(binary_search(list, 3)) 

# the above print statement prints 2 because the number 3 is at the index of 2. (REMEMBER: python lists are zero-index based, meaning they start at zero.)
