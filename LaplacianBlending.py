import numpy
import cv2


input_image1 = cv2.imread("inputA.jpg")
input_image2 = cv2.imread("inputB.jpg")

def laplacian_pyramid_blending(img_in1, img_in2):
    # Write laplacian pyramid blending codes here
    A = img_in1
    B = img_in2
    A = A[:, :A.shape[0]]
    B = B[:A.shape[0], :A.shape[0]]

    G = A.copy()
    gpA = [G]
    for i in xrange(6):
        G = cv2.pyrDown(G)
        gpA.append(G)
    # generate Gaussian pyramid for B
    G = B.copy()
    gpB = [G]
    for i in xrange(6):
        G = cv2.pyrDown(G)
        gpB.append(G)
    # generate Laplacian Pyramid for A
    lpA = [gpA[5]]
    for i in xrange(5, 0, -1):
        GE = cv2.pyrUp(gpA[i])
        L = cv2.subtract(gpA[i - 1], GE)
        lpA.append(L)
    # generate Laplacian Pyramid for B
    lpB = [gpB[5]]
    for i in xrange(5, 0, -1):
        GE = cv2.pyrUp(gpB[i])
        L = cv2.subtract(gpB[i - 1], GE)
        lpB.append(L)
    # Now add left and right halves of images in each level
    LS = []
    for la, lb in zip(lpA, lpB):
        rows, cols, dpt = la.shape
        ls = numpy.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
        LS.append(ls)
    # now reconstruct
    ls_ = LS[0]
    for i in xrange(1, 6):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(ls_, LS[i])

    img_out = ls_  # Blending result

    return True, img_out

# Laplacian pyramid blending
succeed, output_image = laplacian_pyramid_blending(input_image1, input_image2)
cv2.imwrite("blend.png", output_image)
