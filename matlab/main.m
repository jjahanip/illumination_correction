clc; clear all; close all;

tic
input_dir = 'D:\Jahandar\Lab\images\50plex\stitched';
output_dir = 'D:\Jahandar\Lab\images\50plex\IL_corrected';
disk_size = 20;           % disk size for morphological opening

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
parfor i=1:size(image_fnames, 1)
    
    % read image and get the histogram of the original image
    t_in = Tiff(fullfile(input_dir, image_fnames(i).name), 'r+');
    im = read(t_in);
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
    
    % write image to disk
    t_out = Tiff(fullfile(output_dir, image_fnames(i).name), 'w');
    setTag(t_out, 'Photometric', getTag(t_in, 'Photometric'))
    setTag(t_out, 'BitsPerSample', getTag(t_in, 'BitsPerSample'))
    setTag(t_out, 'ImageLength', getTag(t_in, 'ImageLength'))
    setTag(t_out, 'ImageWidth', getTag(t_in, 'ImageWidth'))
    setTag(t_out, 'PlanarConfiguration', getTag(t_in, 'PlanarConfiguration'))
    write(t_out,im);
    
    close(t_in);
    close(t_out);
end

toc