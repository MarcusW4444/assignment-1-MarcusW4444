Marcus Washington

Data Image Processing Assignment 1 Report


1. Resampling:
    Method-
        For nearest_neighbor Interpolation, the first thing to do is establish the dimensions of the new scaled image as
        the product of the size of the original image and the scale factors along both axes.
        Process each pixel in the new image; look at the pixel's potential position on the original image and look at the
        pixel at that location and it's four adjacent neighbors then take the average of those pixel intensity values and
        set that as the new intensity on the new image. (and if there happen to be fewer than 4 neighbors, take the average of
        what is there)

        For Bilinear Interpolation, establish the new image size based on the scale factors.
        Process each pixel for the new image by locating the pixel it would be on for the original image. Take the pair of
        horizontal pixels and the pair of vertical pixels and interpolate both pairs based on the pixels relative position
        compared to the relative position of its original pixel on one axis, then interpolate the results of
        those H and V interpolations based on its position along the other axis.
    Findings-
        Bilinear seems to be the most effective for scaling upwards as each square of pixels that would occupy the same
        pixel on the original image are smoothly interpolated at a higher resolution whereas Nearest Neighbor.
        Nothing to significant when scaling downward, they seem roughly the same.
        Scaling longways/nonuniformally, Bilinear still provides smoothly stretched results.
2. Region Counting:
    Method-
        Before any regions can be counted, the optimal Threshold must be calculated from the expected value of the image
        by counting how many pixels of each intensity appear in the image. The list saved is stored and converted to a
        histogram for observational purposes. Since the threshold is meant to deal with bimodal histograms, the expected
        value of each half of the histogram is calculated by adding up all of the intensities multiplied by the ratio
        of how often a pixel of that intensity appears in the image. Now simply average the resulting two expected values
        of the histogram halves to determine the Threshold.
    Findings-
        The image appears to have a rather fair distribution of dark and light pixels as the optimal threshold would
        reliably fall near intensity 128.
2a. Binarizing
    Method-
        Now that the optimal threshold has been determined, create a new image with the same dimensions as the original
        image. Iterate through all of the pixels in the image, if the intensity is lesser than the threshold, write on
        the new image with an intensity of 0, otherwise if the intensity of the pixel on the original image is above the
        threshold, set the pixel on the new image to intensity 255. (I chose White=1 Black=0 because the example looked
        like that. It does not make a difference beyond conventional formalities)
    Findings-
        The algorithm does a solid job discerning which pixels in the image are in the background or represent objects
        inside the image. At first I was not certain on how it would perform with lower intensities but now I understand
        that the purpose of computing the optimal threshold of an image dictates precisely how it is supposed to reliably
        discern what values will be foreground or background respectively with excellent accuracy.
2b. Blobcoloring
    Method-
        The objective of Blobcoloring is to identify and label blobs of pixels on the image. To do this, create a new
        data table of the same dimensions, and dict() object and iterate over all of the pixels in the new image.
        If a pixel of intensity 0 is detected, then move on; if a pixel of 255 (or just greater than 0) is detected, ask
        if this location is marked in the new data table as 0 (free) then mark it as the beginning of a new region by
        incrementing the regionindex at marking the data table with the regionindex as the new value. Now since this pixel
        is on a blob on the binary image, perform a recursive operation that checks adjacent pixels in the window if they are
        on a blob and are also marked as free (0) on the data table. If it is free, mark it with the current regionindex and
        recursively move on to the adjacent pixels; the recursive calls terminate when they encounter pixels that are not on
        a blob and pixels that are marked as occupied on the data table (r > 0); the result is an entire blob of pixels being
        marked with a regionindex number on the data table. Once the recursive calls are through, the algorithm will most
        likely encounter the many pixels that were marked as occupied by the recently created region, it just ignores the
        pixels in that blob and carries on to find another pixel on a blob that has not been registered in the data table
        and will mark another region based on the pixels in that blob, and so on until the algorithm has iterated through all of
        the pixels in the image.
    Findings-
        Nothing out too of the ordinary that was not to be expected by the algorithm fulfilling its goals.
2c. Cell Ignore and Report
    Method-
        After scanning and processing the binary image, the data table is processed to compute the Centroid and Area of all of thethe regions.
        It also proceeds to check the Area (or pixel counts) of all of the regions that were registered and culls out any regions
        that occupy fewer than 15 pixels on the image.
        After computation, the resulting image must be annotated by writing numeric values over the image as well as adding
        an asterisk to mark the center of each blob. Because I did not know how to put text on an image using any sort of
        OpenCV function, I had to write my own function to draw numbers onto the image pixel by pixel, digit by digit.
        The blob is marked with asterisk at the center which is denoted in the data table, above the blob, it is marked with
        the RegionIndex followed by the area (i.e. 3:658 for region #3 with an area of 658 pixels)
        The Annotated text is drawn at 128 Intensity on the binary image so that it contrasts with the rest of the other
        binary pixels on the image of Intensities 0 and 255 respectively.
    Findings-
        There was one small blob on the right of the image and I saw it get removed from the binary image. But beyond that,
        there was not much to deviate from what was anticipated and handled. However, a typo in my code led to the algorithm
        detecting all values greater than zero which somehow registered all of the space unoccupied by blobs as one big
        massive blob that dwarfed the Areas of the other regions by several thousands of pixels and put the centroid in
        the middle of the image which happened to overlap the annotation text of another blob which made it hard to read.
        In fact, it is fortunate that the blobs are not arranged such that there were not any other text collisions.


-------
{ 'Area': 423, 'CenterPoint': (13.1371158392435, 20.10401891252955), 'Region#': 1}
{ 'Area': 182, 'CenterPoint': (4.252747252747253, 63.07692307692308), 'Region#': 2}
{ 'Area': 658, 'CenterPoint': (12.571428571428571, 108.3693009118541), 'Region#': 3}
{ 'Area': 433, 'CenterPoint': (9.782909930715935, 154.4503464203233), 'Region#': 4}
{ 'Area': 472, 'CenterPoint': (13.457627118644067, 246.864406779661), 'Region#': 5}
{ 'Area': 276, 'CenterPoint': (15.80072463768116, 197.32608695652175), 'Region#': 6}
{ 'Area': 71, 'CenterPoint': (21.760563380281692, 137.11267605633802), 'Region#': 7}
{ 'Area': 260, 'CenterPoint': (27.85, 218.7076923076923), 'Region#': 8}
{ 'Area': 222, 'CenterPoint': (26.03153153153153, 44.554054054054056), 'Region#': 9}
{ 'Area': 20, 'CenterPoint': (26.25, 0.5), 'Region#': 10}
{ 'Area': 489, 'CenterPoint': (33.24539877300614, 173.96319018404907), 'Region#': 11}
{ 'Area': 635, 'CenterPoint': (41.31181102362205, 73.15748031496064), 'Region#': 12}
{ 'Area': 88, 'CenterPoint': (44.73863636363637, 7.784090909090909), 'Region#': 13}
{ 'Area': 221, 'CenterPoint': (47.06334841628959, 233.14932126696831), 'Region#': 14}
{ 'Area': 444, 'CenterPoint': (54.770270270270274, 138.48873873873873), 'Region#': 15}
{ 'Area': 388, 'CenterPoint': (59.25773195876289, 194.64690721649484), 'Region#': 16}
{ 'Area': 510, 'CenterPoint': (57.53137254901961, 28.427450980392155), 'Region#': 17}
{ 'Area': 415, 'CenterPoint': (73.22168674698796, 98.92771084337349), 'Region#': 18}
{ 'Area': 263, 'CenterPoint': (70.52091254752851, 214.1596958174905), 'Region#': 19}
{ 'Area': 351, 'CenterPoint': (73.01424501424502, 245.36467236467237), 'Region#': 20}
{ 'Area': 153, 'CenterPoint': (72.84967320261438, 167.5032679738562), 'Region#': 21}
{ 'Area': 399, 'CenterPoint': (83.80451127819549, 63.86466165413534), 'Region#': 22}
{ 'Area': 418, 'CenterPoint': (83.66985645933015, 129.77033492822966), 'Region#': 23}
{ 'Area': 247, 'CenterPoint': (86.01619433198381, 33.582995951417004), 'Region#': 24}
{ 'Area': 503, 'CenterPoint': (97.44731610337972, 7.831013916500994), 'Region#': 25}
{ 'Area': 278, 'CenterPoint': (94.92805755395683, 222.51438848920864), 'Region#': 26}
{ 'Area': 673, 'CenterPoint': (99.13521545319465, 174.70579494799406), 'Region#': 27}
{ 'Area': 176, 'CenterPoint': (105.17613636363636, 250.8125), 'Region#': 28}
{ 'Area': 357, 'CenterPoint': (111.30252100840336, 102.82913165266106), 'Region#': 29}
{ 'Area': 538, 'CenterPoint': (122.2100371747212, 37.12081784386617), 'Region#': 30}
{ 'Area': 593, 'CenterPoint': (129.68296795952782, 126.54131534569983), 'Region#': 31}
{ 'Area': 629, 'CenterPoint': (132.07631160572336, 164.79491255961844), 'Region#': 32}
{ 'Area': 184, 'CenterPoint': (122.8586956521739, 62.61413043478261), 'Region#': 33}
{ 'Area': 592, 'CenterPoint': (127.4391891891892, 223.8766891891892), 'Region#': 34}
{ 'Area': 262, 'CenterPoint': (139.67175572519085, 7.103053435114504), 'Region#': 36}
{ 'Area': 891, 'CenterPoint': (162.33670033670035, 89.0246913580247), 'Region#': 37}
{ 'Area': 470, 'CenterPoint': (153.09574468085106, 245.58936170212766), 'Region#': 38}
{ 'Area': 233, 'CenterPoint': (146.62660944206007, 66.79828326180258), 'Region#': 39}
{ 'Area': 164, 'CenterPoint': (156.52439024390245, 188.1341463414634), 'Region#': 40}
{ 'Area': 394, 'CenterPoint': (163.12436548223351, 136.25634517766497), 'Region#': 41}
{ 'Area': 405, 'CenterPoint': (168.82716049382717, 16.150617283950616), 'Region#': 42}
{ 'Area': 236, 'CenterPoint': (166.33898305084745, 213.6864406779661), 'Region#': 43}
{ 'Area': 370, 'CenterPoint': (171.76756756756757, 44.16216216216216), 'Region#': 44}
{ 'Area': 644, 'CenterPoint': (181.61801242236024, 179.36490683229815), 'Region#': 45}
{ 'Area': 374, 'CenterPoint': (184.64705882352942, 232.951871657754), 'Region#': 46}
{ 'Area': 570, 'CenterPoint': (197.3438596491228, 130.2824561403509), 'Region#': 47}
{ 'Area': 64, 'CenterPoint': (200.59375, 253.3125), 'Region#': 48}
{ 'Area': 163, 'CenterPoint': (202.93865030674846, 205.8957055214724), 'Region#': 49}
{ 'Area': 456, 'CenterPoint': (215.3859649122807, 26.05701754385965), 'Region#': 50}
{ 'Area': 612, 'CenterPoint': (213.87908496732027, 102.75), 'Region#': 51}
{ 'Area': 533, 'CenterPoint': (217.39962476547842, 62.1031894934334), 'Region#': 52}
{ 'Area': 203, 'CenterPoint': (225.92118226600985, 3.9113300492610836), 'Region#': 53}
{ 'Area': 555, 'CenterPoint': (227.25765765765766, 234.07207207207207), 'Region#': 54}
{ 'Area': 845, 'CenterPoint': (229.80710059171597, 180.08402366863905), 'Region#': 55}
{ 'Area': 273, 'CenterPoint': (233.1831501831502, 138.03296703296704), 'Region#': 56}
{ 'Area': 208, 'CenterPoint': (240.48557692307693, 46.06730769230769), 'Region#': 57}
{ 'Area': 87, 'CenterPoint': (251.31034482758622, 127.75862068965517), 'Region#': 58}
{ 'Area': 74, 'CenterPoint': (251.27027027027026, 178.7027027027027), 'Region#': 59}
{ 'Area': 50, 'CenterPoint': (251.5, 234.26), 'Region#': 60}
{ 'Area': 47, 'CenterPoint': (251.91489361702128, 73.82978723404256), 'Region#': 61}
-------