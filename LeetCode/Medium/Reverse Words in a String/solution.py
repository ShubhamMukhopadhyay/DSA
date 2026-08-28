class Solution(object):
    def reverseWords(self, s):
        words = []
        word = ""

        # Step 1: extract words manually
        for ch in s:
            if ch != ' ':
                word += ch
                
            else:
                if word != "":
                    words.append(word)
                    word = ""

        # Add last word if exists
        if word != "":
            words.append(word)

        # Step 2: build reversed string
        result = ""
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if i != 0:
                result += " "

        return result
