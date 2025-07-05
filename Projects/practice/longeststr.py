from collections import Counter

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            False
    def removeElement(self, nums, val):
        
        l = [a for a in nums if val != a  ]    
        k = len(l)
        print(l)
        return k
    def findLucky(self, arr:list):
         arr.sort(reverse=True)
         for a in arr:
            if a == arr.count(a):
                return 'Lucky'
            else:
                return -1
    def findLucky11(self, arr):
        l = []
        for a in arr:
            if a == arr.count(a):
                l.append(a)
        a = max(l) if len(l) >0 else -1
        return a
    def findLucky(self, arr):
        return max((x for x, f in Counter(arr).items() if x==f), default=-1)
    
    def removeDuplicates(self, nums):
        nums.sort()
        a = [x for x ,y in Counter(nums).items() if len(nums) > 0]
        a.sort()
        del nums[:]
        nums.extend(a)
        k = len(nums)
        return k
    
    def strStr(self, haystac:str, needle:str):
        a = haystac.find(needle)
        return a 
    
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:
            if max(nums) < target:
                    return len(nums)
            else:
                z = 0
                for a in nums:
                    if target < a:
                        return z
                    z +=1
    def reverse(self, x):
        str(x)
        
            
                

c = Solution()
print(c.searchInsert([1,3,5,6],7))