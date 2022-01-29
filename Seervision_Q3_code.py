#!/usr/bin/env python
# coding: utf-8

# In[33]:


#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread


# In[46]:


#transform sample_img to a pixel_array
sample_img = imread('parrot.jpg')
sample_img


# In[47]:


# sample_img to flatterended_img array containing elements by the following format:
# [red_degree, green_degree, blue_degree, row_index_sample_img, column_index_sample_img] 
flattened_img_array = []
for row_index, rows in enumerate(sample_img):
    for column_index, column in enumerate(rows):
        flattened_img_array.append([column[0],column[1],column[2],row_index, column_index]) 

flattened_img_array = np.array(flattened_img_array)
flattened_img_array


# In[20]:


def median_cut_quantize(img_arr):
    
    r_average = np.mean(img_arr[:,0])
    g_average = np.mean(img_arr[:,1])
    b_average = np.mean(img_arr[:,2])
    
    # replacing the pixels in sample_img by r_average, g_average, b_average
    for data in img_arr:
        sample_img[data[3]][data[4]] = [r_average, g_average, b_average]
    
median_cut_quantize(flattened_img_array)
sample_img


# In[31]:


def split_into_squares(img_arr, depth):
    
    # we end the recursion when depth=0, 
    # then we divided the initial square into 2**depth squares
    if depth == 0:
        median_cut_quantize(img_arr)
        return
    
    #computing each color (R,G,B) range in the initial image through its array
    r_range = np.max(img_arr[:,0]) - np.min(img_arr[:,0])
    g_range = np.max(img_arr[:,1]) - np.min(img_arr[:,1])
    b_range = np.max(img_arr[:,2]) - np.min(img_arr[:,2])
    
    rgb_range = [r_range, g_range, b_range]
    
    highest_range = 0
    
    # 0 index of red, 1  index of green, 2 index of blue
    if max(rgb_range) == r_range:
        highest_range = 0
    elif max(rgb_range) == g_range: 
        highest_range = 1
    elif b_range >= r_range and b_range >= g_range:
        highest_range = 2

    # sort the image pixels by color (red, green or blue) having the highest_range
    # argsort returns the indices that would sort img_arr[:,highest_range]
    img_arr = img_arr[img_arr[:,highest_range].argsort()]
    
    median_index = int((1+len(img_arr))/2)
    
    #split the array into two buckets along the median
    split_into_squares(img_arr[0:median_index], depth-1)
    split_into_squares(img_arr[median_index:], depth-1)


# In[28]:


# 2**(depth) = number of colors we want in the final image
split_into_squares(flattened_img_array, 4)


# In[29]:


plt.imshow(imread('parrot.jpg'))
plt.show()


# In[30]:


plt.imshow(sample_img)
plt.show()

