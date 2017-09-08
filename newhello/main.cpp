//
//  test.cpp
//  newhello
//
//  Created by Harshad Untwale on 02/09/17.
//  Copyright © 2017 Harshad Untwale. All rights reserved.
//

#include <string.h>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

// Defining a pixel
typedef Point3_<uchar> Pixel;

// function object for inverting pixels
struct Operator {
    void operator()(Pixel &pixel, const int *position) const {
        // Inverting colors
        pixel.x = 255 - pixel.x;
        pixel.y = 255 - pixel.y;
        pixel.z = 255 - pixel.z;
    }
};

int main(int argc, const char *argv[]) {
    cout << "Open CV Version : " << CV_VERSION << endl;
    
    String imgName = "sampleimage.jpg";  //"../../data/sampleimage.jpg";
    
    /* Defining variable for images
     *    img -> input image
     *    new_image -> pixel manipulated image
     *    scaled image -> reduced height and width by 0.5
     */
    Mat img, new_image, scaled_image;
    
    /* to check if image path passed as command line argument */
    if (argc > 1) {
        cout << "image path defined by user where path : " << argv[1] << endl;
        imgName = argv[1];
    }
    
    /* Reading the image (by default image saved in BGR format) */
    img = imread(imgName);
    
    /*image cloned for pixel manipulation */
    new_image = img.clone();  // Mat::zeros( img.size(), img.type() );
    
    if (img.empty()) {
        cout << "image loading failed" << endl;
        cout
        << "Try copying a image in debug folder and name it sampleimage.jpg"
        << endl;
        return -1;
    }
    
    /*
     // naive approach - compute intesive
     // manipulating each pixel value and copying into new image
     // follows column major form
     for( int y = 0; y < img.rows; y++ )
     {
     for( int x = 0; x < img.cols; x++ )
     {
     for( int i=0;i<3;i++)
     new_image.at<Vec3b>(y,x)[i] =
     saturate_cast<uchar>(img.at<Vec3b>(y,x)[i]/2);
     
     }
     }
     */
    
    /* Calling forEach - pixel manipulation */
    new_image.forEach<Pixel>(Operator());
    
    /* code for resizing image */
    Size size(img.cols / 2, img.rows / 2);
    resize(img, scaled_image, size);
    
    /* creating windows */
    namedWindow("InputImage", CV_WINDOW_AUTOSIZE);
    namedWindow("ModifiedImage", CV_WINDOW_AUTOSIZE);
    namedWindow("ScaledImage", CV_WINDOW_AUTOSIZE);
    
    /* Displaying windows */
    imshow("InputImage", img);
    imshow("ModifiedImage", new_image);
    imshow("ScaledImage", scaled_image);
    
    waitKey(0);
    return 0;
}
