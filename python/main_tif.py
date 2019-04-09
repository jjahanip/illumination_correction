import os
import cv2
import time
import argparse
import numpy as np
from tifffile import imread, imsave
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', type=str, default=r'E:\50_plex\tif\pipeline2\registered', help='path to the directory of input images')
parser.add_argument('--save_dir', type=str, default=r'E:\50_plex\tif\pipeline2\il_corrected_python', help='path to the directory to save corrected images')
parser.add_argument('--disk_size', type=int, nargs='+', default=[40, 80], help='Diameters of smallest and largets objects')

args = parser.parse_args()


def main():

    # create dir to save images if not exist
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    # list all images in input dir
    files = os.listdir(args.input_dir)

    for file in files:
        st = time.time()
        # read the image
        im = imread(os.path.join(args.input_dir, file))

        # create a background array similar to original image
        background = np.copy(im)
        for sz in args.disk_size:
            # apply morphological opening with the defined structuring element
            selem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (sz, sz))
            background = cv2.morphologyEx(background, cv2.MORPH_OPEN, selem)

        # subtract the background from image
        im = cv2.subtract(im, background)

        # normalize image to 0-65535 (for uint16 image)
        im_normalized = cv2.normalize(im, None, 0, 65535, cv2.NORM_MINMAX)

        # save processed image to the disk
        imsave(os.path.join(args.save_dir, file), im_normalized, bigtiff=True)
        print('finished in {0:.2f} seconds.'.format(time.time() - st))


if __name__ == '__main__':

    start = time.time()
    main()
    print('*' * 50)
    print('*' * 50)
    print('Intra-channel fluorescence correction pipeline finished successfully in {} seconds.'.format(time.time() - start))


    # TODO: normalization for uint8


