# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:18:34 2015
to use this script, you have to install some packages, run the following command:
sudo apt-get install python-numpy python-h5py python-tifffile 
@author: jingpeng
"""
#%% parameters
import numpy as np
# the file directory
Dir = '/usr/people/bds2/seungmount/Omni/TracerTasks/Piriform_cortex_Corrections/Chunk_07/Chunk_07_EM/'
filename ='chunk_07_em'
tifname = 'chunk_07_em.tif'

# whether the file is gray image
isgray = True

#%% read the data
import h5py
f = h5py.File(Dir + filename )
invol = np.asarray(f['/main'])
f.close()

if isgray:
	outvol = (invol-invol.min()) / (invol.max()-invol.min()) * 255
	outvol = outvol.astype('uint8')
else:
	vol = np.asarray(invol* ((2**24-1)/float(invol.max())), dtype='uint32') 
	outvol = np.zeros( np.append(np.array( invol.shape ), 3), dtype='uint8')

	outvol[:,:,:, 0] = np.remainder( invol, 256)
	outvol[:,:,:, 1] = np.remainder( invol, 25536) / 256
	outvol[:,:,:, 2] = invol / 25536

#%% write as tiff
import tifffile
tifffile.imsave(Dir + tifname, outvol)

