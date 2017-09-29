import numpy as np
from resize import interpolation as interp
class interpolation:

    def linear_interpolation(self, pt1, pt2, v):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here

        return (pt1 * (1 - v)) + (pt2 * v)

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, xv,yv):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task

        return interpolation.linear_interpolation(self,interpolation.linear_interpolation(self,pt1, pt2, xv), interpolation.linear_interpolation(self,pt3, pt4, xv),yv)
