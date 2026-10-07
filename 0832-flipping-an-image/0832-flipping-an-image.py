class Solution:
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            j = 0
            k = len(image[i]) - 1

            while j <= k:
                image[i][j], image[i][k] = image[i][k], image[i][j]

                image[i][j] = 1 - image[i][j]
                
                if j != k:
                    image[i][k] = 1 - image[i][k]

                j += 1
                k -= 1

        return image