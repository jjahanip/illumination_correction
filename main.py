import os
from czifile import czi2tif, CziFile
import numpy as np
from tifffile import imsave

input_dir = r'D:\Jahandar\Lab\images\50plex\czi'
source_file = 'S1_R1_C1-C11_A1.czi'

save_dir = r'illumination_corrected'

if not os.path.exists(save_dir):
            os.makedirs(save_dir)

for round_idx, file in enumerate(os.listdir(input_dir)):
    with CziFile(os.path.join(input_dir, file)) as czi:

        image = czi.asarray(illumination_correction=True)
        image = np.squeeze(image)

        for i in range(image.shape[0]):
            filename = 'R{}C{}.tif'.format(round_idx+1, i)
            fullname = os.path.join(save_dir, filename)
            imsave(fullname, image[i, :, :], bigtiff=True)
