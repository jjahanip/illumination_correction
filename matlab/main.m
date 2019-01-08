clc; clear all; close all;

tic
input_dir = 'D:\Jahandar\Lab\images\50plex\stitched';
output_dir = 'D:\Jahandar\Lab\images\50plex\IL_corrected';
disk_size = 15;           % disk size for morphological opening

if isempty(gcp('nocreate'))
    myCluster = parcluster('local');
    parpool(myCluster.NumWorkers)
end


% check if output directory exis
if ~exist(output_dir, 'dir')
    mkdir(output_dir)
end

% create disk for morphological opening
se = strel('disk',disk_size);

image_fnames = dir(fullfile(input_dir, '*.tif'));
for i=1:size(image_fnames, 1)
    % read image and get the histogram of the original image
    im = imread(fullfile(input_dir, image_fnames(i).name));
    hgram = imhist(im, 65535);
    
    % calculate the background using morphological opening
    background = imopen(im,se);
    
    % extract the background from original image
    im = im - background + mean(background(:));
    
    % equalize the histogram of corrected image to the original image
    im = histeq(im,hgram);
    
    % normalize to 0-65535
    im = double(im);
    im = uint16(im - min(im(:)))*(65535 / (max(im(:)) - min(im(:))));
    imwrite(im, fullfile(output_dir, image_fnames(i).name));
    
end

toc