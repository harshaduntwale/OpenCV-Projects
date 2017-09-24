import numpy
import cv2

image = cv2.imread("input2.png", cv2.IMREAD_GRAYSCALE)


def ft(im, newsize=None):
    dft = numpy.fft.fft2(numpy.float32(im), newsize)
    return numpy.fft.fftshift(dft)


def ift(shift):
    f_ishift = numpy.fft.ifftshift(shift)
    img_back = numpy.fft.ifft2(f_ishift)
    img_back = img_back
    return numpy.abs(img_back)


def convolution(img_in):
    # Write convolution codes here
    # img_blur_gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    img_blur_gray = img_in
    gk = cv2.getGaussianKernel(21, 5)
    gk = gk * gk.T

    imf = ft(img_blur_gray, (img_blur_gray.shape[0], img_blur_gray.shape[1]))  # make sure sizes match
    gkf = ft(gk, (img_blur_gray.shape[0], img_blur_gray.shape[1]))  # so we can multiple easily
    imdeconvf = imf * gkf

    finalimage = ift(imdeconvf)

    img_out = finalimage

    return True, img_out


def deconvolution(img_in):
    # Write deconvolution codes here
    # img_blur_gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    img_blur_gray = img_in
    gk = cv2.getGaussianKernel(21, 5)
    gk = gk * gk.T

    imf = ft(img_blur_gray, (img_blur_gray.shape[0], img_blur_gray.shape[1]))  # make sure sizes match
    gkf = ft(gk, (img_blur_gray.shape[0], img_blur_gray.shape[1]))  # so we can multiple easily
    imdeconvf = imf / gkf

    finalimage = ift(imdeconvf)

    img_out = finalimage  # cv2.merge((finalimage,finalimage,finalimage)) # Deconvolution result

    return True, img_out


succeed1, convol_image = convolution(image)
succed2, deconvol_image = deconvolution(convol_image)

cv2.imwrite("convolution.png", convol_image)
cv2.imwrite("deconvolution.png", deconvol_image)
