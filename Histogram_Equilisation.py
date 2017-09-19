import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import cv2


image = cv2.imread("sampleimage.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Write histogram equalization here
b_g_r_list = cv2.split(img_in)
hist = []
for i in range(0,3,1):
    histr = cv2.calcHist([img_in], [i], None, [256], [0, 256])
    hist.append(histr)

"""b,g,r"""
                        
    cdf_bgr = [hist[0].cumsum(), hist[1].cumsum(), hist[2].cumsum()]
                            
    cde_bgr = []
                                
    for i in range(0,3,1):
        cdf_m = numpy.ma.masked_equal(cdf_bgr[0], 0)
        #print "cdf_m of ",i," = ",cdf_m
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = numpy.ma.filled(cdf_m, 0).astype('uint8')
        #print "cdf of ", i, " = ", cdf
        cde_bgr.append(cdf[b_g_r_list[i]])
                                                    
                                                    
    image_eq = cv2.merge((cde_bgr[0],cde_bgr[1],cde_bgr[2])) # Histogram equalization result

#cv2.imshow("image",image)
cv2.imshow("image_eq",image_eq)
#cv2.imshow("img_eq_internal_func", img_eq_internal_func)
#cv2.imshow("gray_eq",gray_eq)
#cv2.imshow("gray",gray)
cv2.waitKey(0)
