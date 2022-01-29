# Color Quantization

## What is color quatization ?
In computer graphics, color quantization or color image quantization is quantization applied to color spaces; it is a process that reduces the number of distinct colors used in an image, usually with the intention that the new image should be as visually similar as possible to the original image. Computer algorithms to perform color quantization on bitmaps have been studied since the 1970s. Color quantization is critical for displaying images with many colors on devices that can only display a limited number of colors, usually due to memory limitations, and enables efficient compression of certain types of images.

## Algorithms
Most standard techniques treat color quantization as a problem of clustering points in three-dimensional space, where the points represent colors found in the original image and the three axes represent the three color channels. Almost any three-dimensional clustering algorithm can be applied to color quantization, and vice versa. After the clusters are located, typically the points in each cluster are averaged to obtain the representative color that all colors in that cluster are mapped to. The three color channels are usually red, green, and blue, but another popular choice is the Lab color space, in which Euclidean distance is more consistent with perceptual difference.

The most popular algorithm by far for color quantization, invented by Paul Heckbert in 1979, is the median cut algorithm. This project in an implementation of a version of this algorithm using Python3.

## Results
Find below the initial image of the parrot (108408 color), as well as the resulting image (16 color) after applying the algorithm.

<p align="center" style="margin: 100px 0px 0px 5px;">
  <img src="https://github.com/y-aoub/color_quatization/blob/main/parrot_initial_image.png" width="380" title="hover text">
  
  <img src="https://github.com/y-aoub/color_quatization/blob/main/parrot_final_image.png" style="margin: 0px 0px 0px 0px;" width="380" alt="accessibility text">
</p>

