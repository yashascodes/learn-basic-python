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
