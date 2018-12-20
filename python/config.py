import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--run_name', type=str, default=r'Morphological_Opening', help='Run name')
parser.add_argument('--mode', type=str, default=r'Morphological_Opening', help='Homomorphic, Morphological_Opening')

parser.add_argument('--input_dir', type=str, default=r'E:\50_plex\czi', help='Input Directory')
parser.add_argument('--save_dir', type=str, default=r'E:\jahandar\illumination_correction\results', help='Save directory')

# Homomorphic Filter
parser.add_argument('--a', type=float, default=1.0, help='(a + b * H) * I')
parser.add_argument('--b', type=float, default=0.5, help='(a + b * H) * I')
parser.add_argument('--filter', type=str, default='butterworth', help='HPF type: gaussian | butterworth')
parser.add_argument('--freq', type=int, default=50, help='HPF cut-off frequency')
parser.add_argument('--n', type=int, default=2, help='Butterworth filter order')

# Morphological Opening
parser.add_argument('--disk_size', type=int, default=20, help='Size of the disk for morphological opening')

# Histogram Stretching
parser.add_argument('--stretch', type=bool, default=False, help='Stretch the histogram of image')
parser.add_argument('--pLow', type=float, default=0.001, help='Low percentile of histogram')
parser.add_argument('--pHigh', type=float, default=99.999, help='High percentile of histogram')

# Gamma Correction
parser.add_argument('--gamma_correction', type=bool, default=False, help='Apply gamma correction to image')
parser.add_argument('--gamma', type=float, default=0.99, help='Gamma parameter for gamma correction')

args = parser.parse_args()
