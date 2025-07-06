import time


numbers = list(range(100000000))

class Solution:
    def basic(self, numberList:list, target):
        for a in numberList:
            if a == target:
                return 'Done'
    
    
    def find_number(self, target:int, numberList:list[int] = numbers):
        
        least = 0 
        high = len(numberList) - 1
        while least <= high:
            mid = (high + least)//2

            if numberList[mid] == target:
                return 'Yes it is here'

            elif numberList[mid] < target:
                least = mid + 1

            else:
                high = mid - 1
        return 'target value not found' 

x = Solution()
start_basic = time.perf_counter()
x.basic(numbers, 99999999)  
end_basic = time.perf_counter()
print(f"Linear search execution time: {end_basic - start_basic:.6f} seconds")


start_binary = time.perf_counter()
print(x.find_number(99999999))  
end_binary = time.perf_counter()
print(f"Binary search execution time: {end_binary - start_binary:.6f} seconds")