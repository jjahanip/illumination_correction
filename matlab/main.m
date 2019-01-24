clc; clear all; close all;

tic
input_dir = 'E:\50_plex\tif\pipeline2\registered';
output_dir = 'E:\50_plex\tif\pipeline2\IL_corrected';
disk_size = [20 40];   % disk size for Alternative Sequential Filtering

% if isempty(gcp('nocreate'))
%     myCluster = parcluster('local');
%     parpool(myCluster.NumWorkers)   
% end

% check if output directory exis
if ~exist(output_dir, 'dir')
    mkdir(output_dir)
end

image_fnames = dir(fullfile(input_dir, '*.tif'));
for i=1:size(image_fnames, 1)
    % read image and get the histogram of the original image
    t_in = Tiff(fullfile(input_dir, image_fnames(i).name), 'r+');
    im = read(t_in);
    close(t_in);
    % calculate the background using morphological opening
    background = im;
    for j = 1:length(disk_size)
        % create disk for morphological opening and closing
        se = strel('disk',disk_size(j));
        % Alternative Sequential filter
        background = imopen(background,se);
    end
    
    % extract the background from original image
    im = im - background;
    
    % normalize to 0-65535
    im = double(im);
    im = uint16(im - min(im(:)))*(65535 / (max(im(:)) - min(im(:))));
    
    % write image to disk
    write_bigtiff(im, fullfile(output_dir, image_fnames(i).name));
  
end

fprintf('pipeline finished successfully in %.1f mins.\n', toc/60)