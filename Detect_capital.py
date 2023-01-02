class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (len(word) == 1 ):
            return True
        elif (word[1:].islower()):
            return True
        elif (word.isupper()):
            return True
        else:
            return False
