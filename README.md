# Illumination Correction Pipeline

Illuminatin Correction Pipeline is a tool for correcting non-uniform illumination pattern from Immunohistochemistry (IHC) images taken from __"czi"__ or __"tif"__ files.

# Dependencies:

* numpy
* scipy
* cython
* matplotlib
* scikit-image

# Pipeline
Illumination Correction Pipeline corrects images from `--input_dir` and save them in `--save_dir` under `run_name` folder.

Pipeline runs under two modes:
1. `--mode=Morphological_opening`: Applies morphological opening using a disk with size `--disk_size` on image to extract 
the background and subtract from the original image.
2. `--mode=Homomorphic`: Applies homomorphic with `--filter=gaussian` or `--filter=butterworth` with frequency `--freq`
for non-uniform illumination correction using the following formula:

    $$I_{out} = (a + b \times H) \times I_{in}$$

You can optionally apply __histogram stretching__ and/or __gamma correction__ to the final image.
    
Example:
```bash
python main.py --input_ldir=/path/to/input_data --save_dir=/path/to/output \
               --mode=Homomorphic --a=1 --b=0.5 --freq=100

```
