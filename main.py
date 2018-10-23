import os
import re
import time
from czifile import CziFile
from tifffile import imsave

from utils import *
from config import args


def main():

    if not os.path.exists(os.path.join(args.save_dir, args.run_name)):
        os.makedirs(os.path.join(args.save_dir, args.run_name))

    for file in os.listdir(args.input_dir):
        if os.path.splitext(file)[-1] == '.czi':
            round_idx = int(re.compile('R(\d+)').findall(file)[0])

            with CziFile(os.path.join(args.input_dir, file)) as czi:

                image = czi.asarray(illumination_correction=True, args=args)
                image = np.squeeze(image)

                # temp for R2C4
                for i in range(4, 5):

                # for i in range(image.shape[0]):
                    # stretch the histogram of the image
                    if args.stretch:
                        final_image = rescale_histogram(image[i, :, :], percentile=(args.pLow, args.pHigh))
                        config_name = '_'.join(
                            (str(args.freq), str(int(args.a * 100)), str(int(args.b * 100)),
                             str(args.pLow - int(args.pLow))[1:], str(args.pHigh - int(args.pHigh))[1:]))
                    else:
                        final_image = image[i, :, :]
                        config_name = '_'.join(
                            (str(args.freq), str(int(args.a * 100)), str(int(args.b * 100)),
                             str(0), str(0)))
                    # save image
                    filename = 'R{}C{}_'.format(round_idx, i) + config_name + '.tif'
                    fullname = os.path.join(args.save_dir, args.run_name, filename)
                    imsave(fullname, final_image, bigtiff=True)


if __name__ == '__main__':
    start = time.time()
    main()
    write_spec(args)
    print('pipeline finished successfully in {:.2f} secs.'.format(time.time() - start))
