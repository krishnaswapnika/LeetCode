class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        v = set('aeiouAEIOU')
        hasv = False
        hasc = False
        for i in word:
            if not i.isalnum():
                return False
            if i.isalpha():
                if i in v:
                    hasv= True
                else:
                    hasc = True
        return hasv and hasc
