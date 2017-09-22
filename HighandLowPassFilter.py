import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import cv2

input_image1 = cv2.imread("sample.jpeg")
input_image1_rgb = cv2.cvtColor(input_image1, cv2.COLOR_BGR2RGB)


def low_pass_filter(img_in):
    # Write low pass filter here
    img = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)

    f = numpy.fft.fft2(img)
    fshift = numpy.fft.fftshift(f)

    rows, cols = img.shape
    crow, ccol = rows / 2, cols / 2

    # create a mask first, center square is 1, remaining all zeros
    mask = numpy.zeros((rows, cols), numpy.uint8)
    mask[crow - 20:crow + 20, ccol - 20:ccol + 20] = 1
    # apply mask and inverse DFT
    fshift_lpf = fshift * mask
    f_ishift_lpf = numpy.fft.ifftshift(fshift_lpf)
    img_back_lpf = numpy.fft.ifft2(f_ishift_lpf)
    img_back_lpf = numpy.abs(img_back_lpf)

    img_out = img_back_lpf#cv2.merge((img_back_lpf, img_back_lpf, img_back_lpf))  # Low pass filter result

    return True, img_out

def high_pass_filter(img_in):
    # Write high pass filter here
    img = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)

    f = numpy.fft.fft2(img)
    fshift = numpy.fft.fftshift(f)

    rows, cols = img.shape
    crow, ccol = rows / 2, cols / 2

    # create a mask first, center square is 0, remaining all ones
    mask = numpy.ones((rows, cols), numpy.uint8)
    mask[crow - 20:crow + 20, ccol - 20:ccol + 20] = 0
    # apply mask and inverse DFT
    fshift_hpf = fshift * mask
    f_ishift_hpf = numpy.fft.ifftshift(fshift_hpf)
    img_back_hpf = numpy.fft.ifft2(f_ishift_hpf)
    img_back_hpf = numpy.abs(img_back_hpf)

    img_out = img_back_hpf  # High pass filter result

    return True, img_out

succeed1, output_image_hpf = high_pass_filter(input_image1)
succeed2, output_image_lpf = low_pass_filter(input_image1)

plt.subplot(131),plt.imshow(input_image1_rgb)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(output_image_hpf, cmap = 'gray')
plt.title('High pass filter'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(output_image_lpf, cmap = 'gray')
plt.title('low pass filter'), plt.xticks([]), plt.yticks([])
plt.show()