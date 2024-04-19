#run this file to create a testset.h5 file from images 
#remember to use images of same size and shape for example all images of 64x64 pixels

import h5py
import cv2
import numpy as np

images =[]
classes = np.array([[b'true'], [b'false']])
paths = ["paths", "to", "images", "here"]
labels =[] #labels here are 0 or 1
for path in paths:
    images.append(cv2.imread(path))

imagedata =  np.concatenate([arr[np.newaxis, ...] for arr in images], axis=0)

with h5py.File('testset.h5','w') as f:
    f.create_dataset('test_set_x', data=imagedata)
    f.create_dataset('test_set_y', data=labels)
    f.create_dataset('list_classes', data=classes)
