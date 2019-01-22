function write_bigtiff(image, name)
%WRITE_BIGTIFF writes bigtiff images
    t = Tiff(name, 'w');
    setTag(t, 'Photometric', 1)
    setTag(t, 'BitsPerSample', 16)
    setTag(t, 'ImageLength', size(image, 1))
    setTag(t, 'ImageWidth', size(image, 2))
    setTag(t, 'PlanarConfiguration', 1)
    write(t,image);
    close(t);
end

