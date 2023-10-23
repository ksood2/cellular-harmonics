import os

import numpy as np
from PIL import Image, ImageFilter
from skimage.morphology import thin
from skimage.filters import sobel

def smooth_image(image):
    smoothed_area = image.filter(ImageFilter.ModeFilter(size=9))
    return smoothed_area
def edge_image(im_array):
    edges = sobel(im_array)
    edges = thin(edges)
    return edges

def main():
    input_dir = r"C:\Users\Kyler\Desktop\UROP\Data\Cell Data\immature_area"
    output_dir = r"C:\Users\Kyler\Desktop\UROP\Data\Cell Data\immature_processed"
    for f in os.listdir(input_dir):
        print(f)
        fname, fext = os.path.splitext(f)
        im = Image.open(os.path.join(input_dir, f))
        smoothed_area = smooth_image(im)
        smoothed_area.save(os.path.join(output_dir, fname+"_smoothed"+fext))
        smoothed_edge = edge_image(np.array(smoothed_area))
        smoothed_edge_im = Image.fromarray(smoothed_edge)
        smoothed_edge_im.save(os.path.join(output_dir, fname[:(len(fname)-5)]+"edge_smoothed"+fext))


if __name__ == "__main__":
    main()

