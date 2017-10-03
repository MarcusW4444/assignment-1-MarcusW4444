import numpy as np
import math as math
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        #print("Commencing Blob coloring")
        regions = dict()
        mx = image.shape[0]
        my = image.shape[1]
        regdata = np.zeros(shape=(mx,my))
        regioncount = 0;

        def markPixelForRegion(a,b,r):
            if ((a < 0) or (a >= mx)) or ((b < 0) or (b >= my)):
                return -1 #out of bounds
            if ((image[a,b] > 0) and (regdata[a,b] == 0)): #marks the region pixel in the region data if it has not been marked. Do not mark on background pixels
                regdata[a,b] = r

            return 0

        def rec(x,y,r):
            if ((x < 0) or (x >= mx)) or ((y < 0) or (y >= my)):
                return 0
            if (image[x, y] < 1): #this pixel is not on a blob. terminate
                return 0
            else: # this pixel is on a blob
                if (regdata[x,y] == 0): #this pixel has not been claimed/colored by an existing region.
                    markPixelForRegion(x, y, r)
                    rec(x + 1, y + 0, r)
                    rec(x + 1, y + 1, r)
                    rec(x + 0, y + 1, r)
                    rec(x - 1, y + 1, r)
                    rec(x - 1, y + 0, r)
                    rec(x - 1, y - 1, r)
                    rec(x + 0, y - 1, r)
                    rec(x + 1, y - 1, r)
            return 0

        for i in range(mx):
            for j in range(my):
                if (image[i,j] >= 128): # this pixel is not in the background. Process it.
                    # pos = (i, j)
                    # look at the adjacent pixels in the 8 pixel window
                    if (regdata[i,j] == 0): # this pixel has not been assigned to a region

                        regioncount = regioncount + 1  # discovered a new region

                        r = regioncount
                        rec(i,j,r)
                        # 8 pixel window

                    elif (regdata[i,j] > 0):
                        a = 0 # pixel of existing region


                else:
                    a = 0  # this is a background pixel. Do nothing.

        # collect all of the region values from the region data and put them into the final list
        for i in range(mx):
            for j in range(my):
                r = regdata[i,j]
                if (r == 0):
                    continue
                if (regions.get(r) == None):
                    regions[r] = {}
                regions[r][len(regions[r])] = (i, j)


        return regions

    def compute_statistics(self, regions):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        # print(regions)
        stats = {}
        for i in regions:
            c = 0
            centerx = 0
            centery = 0
            d = {}
            d["Pixels"] = {}


            for j in regions[i]:
                d["Pixels"][len(d["Pixels"])] = (regions[i][j][0], regions[i][j][1])
                c = c + 1
                centerx = centerx + regions[i][j][0]
                centery = centery + regions[i][j][1]

            d["CenterPoint"] = (0, 0)
            d["Area"] = c


            if (c > 0):
                d["CenterPoint"] = (centerx/c, centery/c)
            d["Region#"] = int(i)
            stats[i] = d




        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        mx = image.shape[0]
        my = image.shape[1]
        markedimage = np.zeros(shape=(mx,my))
        global X
        global Y
        X = 0
        Y = 0
        #for i in range(mx):
        #    for j in range(my):
        #        markedimage[i,j] = image[i,j]
        for r in stats:
            if (stats[r]["Area"] >= 15):
                for p in stats[r]["Pixels"]:
                    markedimage[stats[r]["Pixels"][p][0],stats[r]["Pixels"][p][1]] = 255
            else:
                stats[r] = None


        def draw(a,b):
            if ((a < 0) or (a >= mx)) or ((b < 0) or (b >= my)):
                return -1 #out of bounds
            markedimage[a,b] = 128 #255-markedimage[a,b] #simply invert the pixel

        def drawN(a,b,e,f):
            draw(e+b,f+a)
        def markCross(x,y):
            draw(x + 0, y + 0)
            draw(x + 1, y + 0)
            draw(x + 0, y + 1)
            draw(x - 1, y + 0)
            draw(x + 0, y - 1)
            draw(x + 2, y + 0)
            draw(x + 0, y + 2)
            draw(x - 2, y + 0)
            draw(x + 0, y - 2)
            return 0

        def drawNumber(num,x,y):
            X = x
            Y = y


            if (num == 0):
                drawN(-1,-2,x,y)
                drawN(0, -2,x,y)
                drawN(1, -2,x,y)
                drawN(-1, -1,x,y)
                drawN(1, -1,x,y)
                drawN(-1, 0,x,y)
                drawN(1, 0,x,y)
                drawN(-1, 1,x,y)
                drawN(1, 1,x,y)
                drawN(-1, 2,x,y)
                drawN(0, 2,x,y)
                drawN(1, 2,x,y)

            elif (num == 1):
                drawN(1, 2,x,y)
                drawN(1, 1,x,y)
                drawN(1, 0,x,y)
                drawN(1, -1,x,y)
                drawN(1, -2,x,y)
            elif (num == 2):
                drawN(-1, -2,x,y)
                drawN(0, -2,x,y)
                drawN(1, -2,x,y)
                drawN(1, -1,x,y)
                drawN(1, 0,x,y)
                drawN(0, 0,x,y)
                drawN(-1, 0,x,y)
                drawN(-1, 1,x,y)
                drawN(-1, 2,x,y)
                drawN(0, 2,x,y)
                drawN(1, 2,x,y)

            elif (num == 3):
                drawN(-1, -2,x,y)
                drawN(0, -2,x,y)
                drawN(1, -2,x,y)
                drawN(1, -1,x,y)
                drawN(1, 0,x,y)
                drawN(0, 0,x,y)
                drawN(1, 1,x,y)
                drawN(1, 2,x,y)
                drawN(0, 2,x,y)
                drawN(-1, 2,x,y)
            elif (num == 4):
                drawN(-1, -2,x,y)
                drawN(1, -2,x,y)
                drawN(-1, -1,x,y)
                drawN(1, -1,x,y)
                drawN(-1, 0,x,y)
                drawN(0, 0,x,y)
                drawN(1, 0,x,y)
                drawN(1, 1,x,y)
                drawN(1, 2,x,y)
            elif (num == 5):
                drawN(1, -2,x,y)
                drawN(0, -2,x,y)
                drawN(-1, -2,x,y)
                drawN(-1, -1,x,y)
                drawN(-1, 0,x,y)
                drawN(0, 0,x,y)
                drawN(1, 0,x,y)
                drawN(1, 1,x,y)
                drawN(1, 2,x,y)
                drawN(0, 2,x,y)
                drawN(-1, 2,x,y)
            elif (num == 6):
                drawN(1, -2,x,y)
                drawN(0, -2,x,y)
                drawN(-1, -2,x,y)
                drawN(-1, -1,x,y)
                drawN(-1, 0,x,y)
                drawN(0, 0,x,y)
                drawN(1, 0,x,y)
                drawN(1, 1,x,y)
                drawN(1, 2,x,y)
                drawN(0, 2,x,y)
                drawN(-1, 2,x,y)
                drawN(-1, 1,x,y)
            elif (num == 7):
                drawN(-1, -2,x,y)
                drawN(0, -2,x,y)
                drawN(1, -2,x,y)
                drawN(1, -1,x,y)
                drawN(1, 0,x,y)
                drawN(1, 1,x,y)
                drawN(1, 2,x,y)
            elif (num == 8):
                drawN(-1, -2,x,y)
                drawN(0, -2,x,y)
                drawN(1, -2,x,y)
                drawN(-1, -1,x,y)
                drawN(1, -1,x,y)
                drawN(-1, 0,x,y)
                drawN(0, 0,x,y)
                drawN(1, 0,x,y)
                drawN(-1, 1,x,y)
                drawN(1, 1,x,y)
                drawN(-1, 2,x,y)
                drawN(0, 2,x,y)
                drawN(1, 2,x,y)
            elif (num == 9):
                drawN(-1, -2,x,y)
                drawN(0, -2,x,y)
                drawN(1, -2,x,y)
                drawN(-1, -1,x,y)
                drawN(1, -1,x,y)
                drawN(-1, 0,x,y)
                drawN(0, 0,x,y)
                drawN(1, 0,x,y)

                drawN(1, 1,x,y)
                drawN(-1, 2,x,y)
                drawN(0, 2,x,y)
                drawN(1, 2,x,y)
            elif (num == ':'):
                drawN(0, -1, x, y)
                drawN(0, 1, x, y)


            return 0
        def drawMultiDigitNumber(num,x,y,rval):
            if (num >= 1):
                digitsrequired = int(math.log10(int(num)))
            else:
                digitsrequired = 1

            if (rval >= 1):
                digitsrequired = (digitsrequired + int(math.log10(int(rval))))
            else:
                digitsrequired = (digitsrequired + 1)

            X = (x - 6)
            Y = (y + 2+(2 * (digitsrequired)))

            # Determine more optimal positioning of the text for readability
            while True:

                drawNumber(int(num % 10),X,Y)
                num = (num//10)
                Y = (Y - 4)

                if (num <= 0):
                    break
            drawNumber(':', X, Y)
            Y = (Y - 4)
            while True:

                drawNumber(int(rval % 10),X,Y)
                rval = (rval//10)
                Y = (Y - 4)

                if (rval <= 0):
                    break
            return 0
        v = 0
        print("Region Report")
        for r in stats:
            if (stats[r] != None):
                u = int(stats[r]["CenterPoint"][0])
                v = int(stats[r]["CenterPoint"][1])
                # for e in stats[r]["Pixels"]:
                    # markedimage[stats[r]["Pixels"][e][0],stats[r]["Pixels"][e][1]] = 100+r
                markCross(u,v)
                drawMultiDigitNumber(stats[r]["Area"], u, v, r)
                stats[r]["Pixels"] = None
                print(stats[r])
        """
        for i in range(mx):
            for j in range(my):
                markedimage[i,j] = v*255
                if (v == 0):
                    v = 1
                else:
                    v = 0"""


        return markedimage

