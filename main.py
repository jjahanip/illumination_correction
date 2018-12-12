import os
import re
import time
from czifile import CziFile
from tifffile import imsave

from utils import *
from config import args


def main():
    # Create folder to save results
    if not os.path.exists(os.path.join(args.save_dir, args.run_name)):
        os.makedirs(os.path.join(args.save_dir, args.run_name))

    for file in os.listdir(args.input_dir):
        if os.path.splitext(file)[-1] == '.czi':
            round_idx = int(re.compile('R(\d+)').findall(file)[0])

            with CziFile(os.path.join(args.input_dir, file)) as czi:

                image = czi.asarray()
                image = np.squeeze(image)

                for i in range(image.shape[0]):

                    # Post-Processing
                    im = post_processing(image[i, :, :])

                    # stretch the histogram of the image
                    if args.stretch:
                        im = rescale_histogram(im, percentile=(args.pLow, args.pHigh))
                    if args.gamma_correction:
                        im = exposure.adjust_gamma(im, args.gamma)

                    # save image
                    filename = 'R{}C{}'.format(round_idx, i) + '.tif'
                    fullname = os.path.join(args.save_dir, args.run_name, filename)
                    imsave(fullname, im, bigtiff=True)


if __name__ == '__main__':
    start = time.time()
    main()
    write_spec(args)
    print('pipeline finished successfully in {:.2f} secs.'.format(time.time() - start))
