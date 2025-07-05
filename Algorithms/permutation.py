class Solution(object):
    def getPermutation(self, n, k):
        results = []
        s = ''.join(str(i) for i in range(1, n + 1))
        def permute(string, packet = ''):
            if len(string) == 0:
                results.append(packet)
            else:
                for i in range(len(string)):
                    letter = string[i]
                    front = string[0:i]
                    back = string[i+1:]
                    together = front +back
                    permute(together, letter+packet)
        permute(s,'')
        results.sort()
        return results[k-1]
        