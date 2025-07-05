def twoSum(nums, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
      
        return []


print(twoSum([1,3,5,4,2], 7))