import numpy as np
from resize import interpolation as interp
import math
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """
        #sx = 12.5
        #sy = 12.5
        #image.shape
        fx = float(fx)
        fy = float(fy)
        originalx = image.shape[0]
        originaly = image.shape[1]
        sx = int(image.shape[0] * fx)
        sy = int(image.shape[1] * fy)

        newimage = np.zeros(shape=(sx,sy))
        #maxv = 0;
        for i in range(sx):
            for j in range(sy):
                #print("this "+str(i)+","+str(j))
                #(image[int((i / sx) * image.shape[0]), int((j / sy) * image.shape[1])])
                neighbors = [0,0,0,0,0]
                numneighbors = 0


                #if (newimage[i,j] > maxv):
                    #maxv = newimage[i,j]
                for u in range(5):
                    pixx = 0
                    pixy = 0
                    if (u == 0):
                        pixx = 0
                        pixy = 0
                    elif (u == 1):
                        pixx = 1
                        pixy = 0
                    elif u == 1:
                        pixx = 0
                        pixy = 1
                    elif u == 2:
                        pixx = -1
                        pixy = 0
                    elif u == 3:
                        pixx = 0
                        pixy = -1
                    e = (int((i/sx)*originalx)+pixx)
                    f = (int((j / sy)*originaly)+pixy)
                    if ((((e) >= 0) and (e < originalx)) and ((f >= 0) and (f < originaly))):
                        neighbors[numneighbors] = (image[e,f])
                        numneighbors = numneighbors+1

                if numneighbors > 0:
                    total = 0
                    for n in range(numneighbors):
                        total = total + neighbors[n]
                    avg = (total/numneighbors)
                    newimage[i, j] = avg
                else:
                    print("no neighbors which is impossible")
        #print("Maxv")
        #print(maxv)

        #Write your code for nearest neighbor interpolation here

        return newimage
    def maxval(self,f1,f2):
        if (f1 > f2):
            return f1
        else:
            return f2;
    def minval(self,f1,f2):
        if (f1 < f2):
            return f1
        else:
            return f2;
    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here

        fx = float(fx)
        fy = float(fy)
        originalx = image.shape[0]
        originaly = image.shape[1]
        sx = int(image.shape[0] * fx)
        sy = int(image.shape[1] * fy)

        newimage = np.zeros(shape=(sx, sy))
        # maxv = 0;
        for i in range(sx):
            for j in range(sy):
                ux = ((i/sx)*originalx)+.5 #.5 for center of pixel, not corner
                uy = ((j / sy) * originaly)+.5
                i1 = image[int(ux),int(uy)]

                i2 = image[self.minval(int(ux)+1,originalx-1), int(uy)]
                i3 = image[int(ux), self.minval(int(uy)+1,originaly-1)]
                i4 = image[self.minval(int(ux)+1,originalx-1), self.minval(int(uy)+1, originaly-1)]
                #Choose the correct position based on the scaling of the new image. which can be in between pixels
                nrx = self.minval(ux,originalx-1)
                nry = self.minval(uy, originaly - 1)
                nrx = nrx-int(nrx)
                nry = nry - int(nry)


                newimage[i,j] =  interp.interpolation.bilinear_interpolation(self,i1,i2,i3,i4,nrx,nry)



        return newimage

