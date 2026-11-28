class Solution:
    def toGoatLatin(self, sentence):
        words = sentence.split()
        vowels = "aeiouAEIOU"

        ans = []

        for i, word in enumerate(words):
            if word[0] not in vowels:
                word = word[1:] + word[0]

            word += "ma"
            word += "a" * (i + 1)

            ans.append(word)

        return " ".join(ans)