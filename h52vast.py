#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:18:34 2015
to use this script, you have to install some packages, run the following command:
sudo apt-get install python-numpy python-h5py python-tifffile python-tk
@author: jingpeng
"""
#%% parameters
import numpy as np
import tifffile
#%% get filename
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print "filename: {}".format(filename)

#%% read the data
if "h5" in filename or "hdf5" in filename:
    import h5py
    f = h5py.File( filename )
    invol = np.asarray(f['/main'])
    f.close()
elif "tif" in filename:
    invol = tifffile.imread(filename)
else:
    print "invalid data type"
#%% transform
if invol.dtype=='float32':
	# gray image
	outvol = (invol-invol.min()) / (invol.max()-invol.min()) * 255
	outvol = outvol.astype('uint8')
elif invol.dtype=='uint32':
	# RGB image
	vol = np.asarray(invol* ((2**24-1)/float(invol.max())), dtype='uint32')
	outvol = np.zeros( np.append(np.array( invol.shape ), 3), dtype='uint8')

	outvol[:,:,:, 0] = np.remainder( invol, 256)
	outvol[:,:,:, 1] = np.remainder( invol, 25536) / 256
	outvol[:,:,:, 2] = invol / 25536
else:
	print "invalid file, please have a check using hdfview."

#%% write as tiff
import tifffile
filename.replace(".h5", "")
filename.replace(".hdf5", "")
filename.replace(".tiff", "")
filename.replace(".tif", "")
tifffile.imsave(filename+".tif", outvol)
