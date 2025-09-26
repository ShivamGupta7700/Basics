class logic :
    
    def toFindLongestSubStr(self, str: str):
        
        #LOGIC 1

        seen = set()
        l = [letters for letters in str if not (letters in seen or seen.add(letters))]
        print(l)
        
        # LOGIC 2
        
        uniq = list(dict.fromkeys(str))  
        print(uniq)
        

logic().toFindLongestSubStr('okok')

