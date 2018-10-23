import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--run_name', type=str, default=r'R2C4', help='Run name')

parser.add_argument('--input_dir', type=str, default=os.getcwd(), help='Input Directory')
parser.add_argument('--save_dir', type=str, default=r'E:\jahandar\illumination_correction\results', help='Save directory')
parser.add_argument('--source_file', type=str, default=r'S1_R2_C1-C11_A1.czi', help='Source CZI file')

parser.add_argument('--a', type=float, default=0.5, help='(a + b * H) * I')
parser.add_argument('--b', type=float, default=2.00, help='(a + b * H) * I')
parser.add_argument('--filter', type=str, default='gaussian', help='HPF type: gaussian | butterworth')
parser.add_argument('--freq', type=int, default=50, help='HPF cut-off frequency')
parser.add_argument('--n', type=int, default=2, help='Butterworth filter order')

parser.add_argument('--stretch', type=bool, default=False, help='Stretch the histogram of image')
parser.add_argument('--pLow', type=float, default=0.1, help='Low percentile of histogram')
parser.add_argument('--pHigh', type=float, default=99.999, help='High percentile of histogram')


args = parser.parse_args()