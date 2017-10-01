import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        mx = image.shape[0]
        my = image.shape[1]
        for i in range(mx):
            for j in range(my):
                intensityvalue = int(image[i,j])
                hist[intensityvalue] = hist[intensityvalue]+1


        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        modes = 2


        mid = 256//modes
        expectedvalue1 = 0.0
        probabilities = [0.0]*256
        pixelcount1 = 0

        for i in range(mid):
            pixelcount1 = (pixelcount1+hist[i])
        for i in range(mid):
            probabilities[i] = (hist[i]/pixelcount1)
            expectedvalue1 = (expectedvalue1 + (i * probabilities[i]))

        pixelcount2 = 0
        expectedvalue2 = 0.0
        for i in range(mid,256):
            pixelcount2 = (pixelcount2 + hist[i])
        for i in range(mid,256):
            probabilities[i] = (hist[i] / pixelcount2)
            expectedvalue2 = (expectedvalue2 + (i * probabilities[i]))



        threshold = (expectedvalue1 + expectedvalue2)/2

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        h = self.compute_histogram(image)
        thresh = self.find_optimal_threshold(h)
        mx = bin_img.shape[0]
        my = bin_img.shape[1]
        for i in range(mx):
            for j in range(my):
                if (image[i,j] >= thresh):
                    bin_img[i,j] = 0
                else:
                    bin_img[i,j] = 255

        return bin_img


