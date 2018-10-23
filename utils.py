import os
import numpy as np
from skimage import exposure


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


def write_spec(args):
    """ Write specifications of the run in run folder"""
    config_file = open(os.path.join(args.save_dir, args.run_name, 'config.txt'), 'w')
    config_file.write('run_name: ' + args.run_name + '\n')
    config_file.write('a: ' + str(args.a) + '\n')
    config_file.write('b: ' + str(args.b) + '\n')
    config_file.write('filter: ' + args.filter + '\n')
    config_file.write('freq: ' + str(args.freq) + '\n')
    config_file.write('n: ' + str(args.n) + '\n')
    config_file.write('stretch: ' + str(args.stretch) + '\n')
    config_file.write('pLow: ' + str(args.pLow) + '\n')
    config_file.write('pHigh: ' + str(args.pHigh) + '\n')

    config_file.close()
