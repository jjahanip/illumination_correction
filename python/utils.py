import os
import numpy as np
from skimage import exposure
from scipy.signal import argrelextrema


def rescale_histogram(image, percentile=(.01, .99)):
    """ Return image after stretching or shrinking its intensity levels.
        The desired intensity range of the input and output, `in_range` and
        `out_range` respectively, are used to stretch or shrink the intensity range
        of the input image. See examples below.
        Parameters
        ----------
        image : array
            Image array.
        in_range, out_range : str or 2-tuple, optional
            Min and max intensity values of input and output image.
            The possible values for this parameter are enumerated below.
            'image'
                Use image min/max as the intensity range.
            'dtype'
                Use min/max of the image's dtype as the intensity range.
            dtype-name
                Use intensity range based on desired `dtype`. Must be valid key
                in `DTYPE_RANGE`.
            2-tuple
                Use `range_values` as explicit min/max intensities.
        Returns
        -------
        out : array
            Image array after rescaling its intensity. This image is the same dtype
            as the input image.
    """
    p1, p99 = np.percentile(image, percentile)
    return exposure.rescale_intensity(image, in_range=(p1, p99), out_range='dtype')


def post_processing(image):
    """
    Rescale histogram to dtype and remove autoflourscence of local minimum
    :param image: input image
    :return: corrected image
    """
    # rescale to dtype
    image = exposure.rescale_intensity(image, in_range='image', out_range='dtype')

    #TODO: Check for compatibility in general case (applied just for Homomorphic filter)
    # # remove local minima in histogram
    # hist = np.histogram(image, 512)
    #
    # # minVal is the first local minima in histogram
    # minInd = argrelextrema(hist[0], np.less)
    # minVal = hist[1][minInd[0][0]]
    #
    # # maxVal is the highest intensity in which we have more than 25 occurrence
    # maxInd = np.where(hist[0] > 25)
    # maxVal = hist[1][maxInd[0][-1]]
    #
    # image = exposure.rescale_intensity(image, in_range=(minVal, maxVal), out_range='dtype')

    return image


def write_spec(args):
    """ Write specifications of the run in run folder"""
    config_file = open(os.path.join(args.save_dir, args.run_name, 'config.txt'), 'w')
    config_file.write('run_name: ' + args.run_name + '\n')
    config_file.write('mode: ' + args.mode + '\n')

    if args.mode == 'Homomorphic':
        config_file.write('a: ' + str(args.a) + '\n')
        config_file.write('b: ' + str(args.b) + '\n')
        config_file.write('filter: ' + args.filter + '\n')
        config_file.write('freq: ' + str(args.freq) + '\n')
        config_file.write('n: ' + str(args.n) + '\n')
    elif args.mode == "Morphological_Opening":
        config_file.write('disk_size: ' + str(args.disk_size) + '\n')

    if args.stretch:
        config_file.write('stretch: ' + str(args.stretch) + '\n')
        config_file.write('pLow: ' + str(args.pLow) + '\n')
        config_file.write('pHigh: ' + str(args.pHigh) + '\n')

    if args.gamma_correction:
        config_file.write('gamma_correction: ' + str(args.gamma_correction) + '\n')
        config_file.write('gamma: ' + str(args.gamma) + '\n')

    config_file.close()
