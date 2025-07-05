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
    def findLucky(self, arr):
        l = []
        for a in arr:
            if a == arr.count(a):
                l.append(a)
        a = max(l) if len(l) >0 else -1

        return a


c = Solution()
c.isPalindrome(121)
print(c.removeElement([3,2,2,3],3))
print(c.findLucky([2,2,2,3,3]))