class Solution:
    def reverseWords(self, s):
        words = s.split()

        for k in range(len(words)):
            word = list(words[k])

            i = 0
            j = len(word) - 1

            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1

            words[k] = "".join(word)

        return " ".join(words)