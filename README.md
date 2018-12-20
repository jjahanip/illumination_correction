# Illumination Correction Pipeline

Illuminatin Correction Pipeline is a tool for correcting non-uniform illumination pattern from Immunohistochemistry (IHC) images taken from __"czi"__ or __"tif"__ files.

# Matlab
Performs morphological opening on __tif__ images in a parallel manner to speed up the proces.

## Arguments:
|Argument|Discription|
|---|---|
|input_dir|path to the directory containing original images|
|output_dir|path to the directory to save processed images|
|disk_size|size of the morphological structure for morphological opening|


# Python
Performs morphological opening or homomorphic filter on __czi__ files.

## Dependencies:
* numpy
* scipy
* cython
* matplotlib
* scikit-image

## Arguments:
|Argument|Discription|
|---|---|
|input_dir|path to the directory containing original images|
|save_dir|path to the directory to save processed images|
|run_name|optional run name subdirectory in save_dir|
|disk_size|size of the morphological structure for morphological opening|
|mode|filtering mode: "Morphological_opening" or "Homomorphic"|


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
